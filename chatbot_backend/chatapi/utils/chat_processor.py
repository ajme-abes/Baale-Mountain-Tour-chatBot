import json
import numpy as np 
import nltk 
import random
import spacy
import pickle
import logging
import requests
import os
import warnings
from datetime import datetime 
from pathlib import Path

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress INFO and WARNING messages
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations to avoid warnings
warnings.filterwarnings('ignore', category=FutureWarning)  # Suppress FutureWarnings

from tensorflow.keras.models import load_model 
from django.conf import settings

logger = logging.getLogger(__name__)

class ChatProcessor:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.lemmatizer = nltk.WordNetLemmatizer()
        
        # Load spaCy model with error handling
        try:
            self.nlp = spacy.load("en_core_web_lg")
            logger.info("spaCy model 'en_core_web_lg' loaded successfully")
        except OSError as e:
            logger.error(f"Failed to load spaCy model: {str(e)}")
            logger.info("Attempting to download en_core_web_lg model...")
            try:
                import subprocess
                subprocess.run(["python", "-m", "spacy", "download", "en_core_web_lg"], check=True)
                self.nlp = spacy.load("en_core_web_lg")
                logger.info("spaCy model downloaded and loaded successfully")
            except Exception as download_error:
                logger.error(f"Failed to download spaCy model: {str(download_error)}")
                # Fallback to smaller model
                try:
                    self.nlp = spacy.load("en_core_web_sm")
                    logger.warning("Using fallback model 'en_core_web_sm'")
                except:
                    logger.critical("No spaCy model available. Please install en_core_web_lg or en_core_web_sm")
                    raise
        
        self.CULTURAL_KEYWORDS = {"museum", "gallery", "exhibit", "art", "history", "heritage"}
        self.CULTURAL_TEMPLATE = self.nlp("Visit a museum or art gallery")
        self.translation_cache = {}
        
        # Add response caching for faster responses
        self.response_cache = {}
        self.bow_cache = {}
        
        try:
            self._download_nltk_resources()
            self._load_artifacts()
            self._verify_compatibility()
            logger.info("ChatProcessor initialized successfully")
        except Exception as e:
            logger.critical(f"Initialization failed: {str(e)}", exc_info=True)
            raise
            raise
        
    def _translate_text(self, text, target_lang='en'):
        cache_key = f"{text}-{target_lang}"
        if cache_key in self.translation_cache:
            return self.translation_cache[cache_key]
        try:
            url = "https://translation.googleapis.com/language/translate/v2"
            params = {
                'q': text,
                'target': target_lang,
                'key': settings.GOOGLE_TRANSLATE_API_KEY
            }
            response = requests.post(url, params=params)
            translated = response.json()['data']['translations'][0]['translatedText']
            self.translation_cache[cache_key] = translated
            return translated
        except Exception as e:
            logger.error(f"Translation failed: {str(e)}")
            return text

    def _download_nltk_resources(self):
        resources = {
            'punkt': 'tokenizers/punkt',
            'wordnet': 'corpora/wordnet'
        }
        for name, path in resources.items():
            try:
                nltk.data.find(path)
            except LookupError:
                nltk.download(name, quiet=True)

    def _load_artifacts(self):
        try:
            vocab_path = self.BASE_DIR / 'chatapi/utils/vocabulary.pkl'
            with open(vocab_path, 'rb') as f:
                self.words = pickle.load(f)
            classes_path = self.BASE_DIR / 'chatapi/utils/classes.pkl'
            with open(classes_path, 'rb') as f:
                self.classes = pickle.load(f)
            model_path = self.BASE_DIR / 'chatapi/utils/chatbot_model.keras'
            self.model = load_model(str(model_path))
            intents_path = self.BASE_DIR / 'chatapi/utils/baale_mountain.json'
            with open(intents_path, 'r', encoding='utf-8-sig') as f:
                self.intents = json.load(f)
        except Exception as e:
            logger.error(f"Failed to load artifacts: {str(e)}")
            raise RuntimeError("Initialization failed - check server logs")

    def _verify_compatibility(self):
        if not hasattr(self.model, 'input_shape'):
            raise ValueError("Invalid model format")
        expected_features = self.model.input_shape[1]
        actual_features = len(self.words)
        if expected_features != actual_features:
            raise ValueError(
                f"Model expects {expected_features} features, "
                f"but vocabulary has {actual_features} words. "
                "Retrain model with current data!"
            )

    def clean_text(self, text):
        text = text.lower().strip()
        tokens = nltk.word_tokenize(text)
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def create_bow(self, text):
        tokens = self.clean_text(text)
        return [1 if word in tokens else 0 for word in self.words]
    
    def _replace_placeholders(self, response):
        placeholders = {
            "{time_of_day}": self._get_time_of_day()
        }
        for placeholder, value in placeholders.items():
            response = response.replace(placeholder, value)
        return response

    def _get_time_of_day(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 18:
            return "afternoon"
        else:
            return "evening"
    

    def _validate_intent_structure(self, intent):
        required_keys = ['tag', 'patterns', 'responses']
        if not all(key in intent for key in required_keys):
            raise ValueError(f"Invalid intent structure: {intent.get('tag')}")
        
        for response in intent['responses']:
            if 'parts' not in response:
                raise ValueError(f"Response missing 'parts' in intent: {intent['tag']}")
                
            for part in response['parts']:
                if 'type' not in part:
                    raise ValueError(f"Response part missing 'type' in intent: {intent['tag']}")
    def process_response_part(self, part):
        processed = part.copy()
        
        # Handle content replacement and recursion
        if 'content' in processed:
            if isinstance(processed['content'], str):
                processed['content'] = self._replace_placeholders(processed['content'])
            elif isinstance(processed['content'], list):
                processed['content'] = [self.process_response_part(item) if isinstance(item, dict) else item 
                                      for item in processed['content']]
        
        # Process nested items
        for key in ['items', 'options', 'activities']:
            if key in processed:
                processed[key] = [self.process_response_part(item) if isinstance(item, dict) else 
                                 self._replace_placeholders(item) if isinstance(item, str) else item 
                                 for item in processed[key]]
        
        return processed
    
    

    def get_response(self, text, threshold=0.7):
        try:
            # Check cache first for faster responses
            cache_key = text.strip().lower()
            if cache_key in self.response_cache:
                logger.info("Returning cached response")
                return self.response_cache[cache_key]
            
            # Pre-process input
            cleaned_input = cache_key
            
            # Quick action pattern matching for common queries
            quick_action_responses = self._handle_quick_actions(cleaned_input)
            if quick_action_responses:
                self.response_cache[cache_key] = quick_action_responses
                return quick_action_responses
        
            # First check for time-based greetings
            time_based_patterns = next(
                (intent['patterns'] 
                for intent in self.intents.get('intents', [])
                if intent.get('tag') == 'time_based_greeting'),
                []
            )
        
            if any(pattern in cleaned_input for pattern in time_based_patterns):
               # Handle time-based greeting directly
               intent_tag = 'time_based_greeting'
               for intent in self.intents.get('intents', []):
                   if intent.get('tag') == intent_tag:
                       response = random.choice(intent.get('responses', []))
                       processed_content = self._replace_placeholders(response['content'])
                       result = {
                          'parts': [{'type': 'text', 'content': processed_content}],
                          'confidence': 1.0,  # Max confidence for direct match
                          'intent': intent_tag
                        }
                       # Cache the result
                       self.response_cache[cache_key] = result
                       return result
        
            # 2. Process other intents with caching
            detected_lang = self._detect_language(text)
            if detected_lang != 'en':
               text = self._translate_text(text, target_lang='en')
               
            # Use cached BOW if available
            bow_key = text.lower().strip()
            if bow_key in self.bow_cache:
                bow = self.bow_cache[bow_key]
            else:
                bow = self.create_bow(text)
                self.bow_cache[bow_key] = bow
                
            predictions = self.model.predict(np.array([bow], dtype=np.float32))[0]
            results = sorted(
                ((i, float(conf)) for i, conf in enumerate(predictions) if conf > threshold),
                key=lambda x: x[1], reverse=True
            )
        
            if not results:
               result = self._fallback_response()
               self.response_cache[cache_key] = result
               return result
        
            top_idx, top_conf = results[0]
            intent_tag = self.classes[top_idx]
        
            # Special handling for regular greetings
            if intent_tag == 'greeting':
              for intent in self.intents.get('intents', []):
                  if intent.get('tag') == 'greeting':
                      response = random.choice(intent.get('responses', []))
                      result = {
                          'parts': [response],  # Directly use greeting response
                          'confidence': top_conf,
                          'intent': intent_tag
                        }
                      # Cache the result
                      self.response_cache[cache_key] = result
                      return result
        
            for intent in self.intents.get('intents', []):
                if intent.get('tag') == intent_tag:
                   response = random.choice(intent.get('responses', []))
                   processed_parts = []
                
                   for part in response.get('parts', []):
                       processed_part = self.process_response_part(part)
                       processed_parts.append(processed_part)
                
                   result = {
                    'parts': processed_parts,
                    'confidence': top_conf,
                    'intent': intent_tag
                    }
                   
                   # Cache the result
                   self.response_cache[cache_key] = result
                   return result
                
            result = self._fallback_response()
            self.response_cache[cache_key] = result
            return result
    
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}", exc_info=True)
            return self._error_response()
    
    def _handle_quick_actions(self, cleaned_input):
        """Handle specific quick action queries with direct pattern matching"""
        
        # Park Information
        if any(phrase in cleaned_input for phrase in [
            "tell me about bale mountains national park",
            "tell me about bale mountains",
            "tell me about baale mountain",
            "park information",
            "about the park"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'Bale Mountains National Park Information'
                }, {
                    'type': 'text',
                    'content': 'Bale Mountains National Park is known for its diverse ecosystems, rare wildlife like the Ethiopian wolf, and stunning landscapes such as the Sanetti Plateau and Harenna Forest. It\'s perfect for wildlife enthusiasts and nature lovers.'
                }],
                'confidence': 0.95,
                'intent': 'place_info'
            }
        
        # How to Get There
        if any(phrase in cleaned_input for phrase in [
            "how do i get to bale mountains",
            "how do i get to baale mountain",
            "how to get there",
            "directions to bale mountains",
            "how to reach the park"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'How to Get to Bale Mountains National Park'
                }, {
                    'type': 'text',
                    'content': 'There are three main routes to reach Bale Mountains National Park:'
                }, {
                    'type': 'section',
                    'title': 'Route 1: Via Addis Ababa - Shashemene - Goba',
                    'content': [{
                        'type': 'list',
                        'content': [
                            'Distance: 460km from Addis Ababa',
                            'Travel time: 6-8 hours by car',
                            'Road condition: Mostly paved, good condition',
                            'Best for: Most travelers, good road access'
                        ]
                    }]
                }, {
                    'type': 'note',
                    'content': '💡 Tip: Goba town serves as the main gateway to the park with accommodation and supplies available.'
                }],
                'confidence': 0.95,
                'intent': 'getting_there'
            }
        
        # Accommodation Options
        if any(phrase in cleaned_input for phrase in [
            "accommodation options",
            "where can i stay",
            "lodging",
            "hotels",
            "places to stay"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'Accommodation Options'
                }, {
                    'type': 'text',
                    'content': 'There are several accommodation options available for visitors to Bale Mountains National Park:'
                }, {
                    'type': 'list',
                    'content': [
                        'Bale Mountain Lodge - Luxury eco-lodge with stunning views',
                        'Goba Hotels - Various budget to mid-range options in Goba town',
                        'Camping - Designated camping areas within the park',
                        'Community Lodges - Local community-run accommodations'
                    ]
                }],
                'confidence': 0.95,
                'intent': 'lodging'
            }
        
        # Activities
        if any(phrase in cleaned_input for phrase in [
            "what activities can i do",
            "activities in the park",
            "what can i do",
            "park activities"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'Activities in Bale Mountains National Park'
                }, {
                    'type': 'text',
                    'content': 'The park offers a wide range of activities for nature enthusiasts:'
                }, {
                    'type': 'list',
                    'content': [
                        'Wildlife viewing (Ethiopian wolves, mountain nyala, etc.)',
                        'Bird watching (over 280 species recorded)',
                        'Hiking and trekking on various trails',
                        'Photography of landscapes and wildlife',
                        'Cultural visits to local communities',
                        'Horseback riding',
                        'Camping under the stars'
                    ]
                }],
                'confidence': 0.95,
                'intent': 'activities_within_park'
            }
        
        # Best Time to Visit
        if any(phrase in cleaned_input for phrase in [
            "when is the best time to visit",
            "best time to go",
            "when to visit",
            "best season"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'Best Time to Visit Bale Mountains'
                }, {
                    'type': 'text',
                    'content': 'The best time to visit depends on your preferences:'
                }, {
                    'type': 'section',
                    'title': 'Dry Season (October - March)',
                    'content': [{
                        'type': 'list',
                        'content': [
                            'Best for wildlife viewing',
                            'Clear skies and good visibility',
                            'Easier road access',
                            'Ideal for photography'
                        ]
                    }]
                }, {
                    'type': 'section',
                    'title': 'Wet Season (April - September)',
                    'content': [{
                        'type': 'list',
                        'content': [
                            'Lush green landscapes',
                            'Wildflowers in bloom',
                            'Bird migration season',
                            'Some roads may be challenging'
                        ]
                    }]
                }],
                'confidence': 0.95,
                'intent': 'when_to_go'
            }
        
        # Park Fees
        if any(phrase in cleaned_input for phrase in [
            "park fees",
            "entrance fees",
            "how much does it cost",
            "park entrance fee"
        ]):
            return {
                'parts': [{
                    'type': 'header',
                    'content': 'Bale Mountains National Park Fees'
                }, {
                    'type': 'text',
                    'content': 'Park entrance fees vary by visitor type:'
                }, {
                    'type': 'table',
                    'columns': ['Visitor Type', 'Daily Fee'],
                    'rows': [
                        ['Foreign Tourist', '200 ETB'],
                        ['Domestic Tourist', '50 ETB'],
                        ['Student (with ID)', '25 ETB'],
                        ['Local Community', '10 ETB']
                    ]
                }, {
                    'type': 'note',
                    'content': '💡 Additional fees may apply for camping, guides, and special activities.'
                }],
                'confidence': 0.95,
                'intent': 'park_fees'
            }
        
        return None
    
    def _detect_language(self, text):
        non_latin = any(ord(c) > 127 for c in text)
        return 'am' if non_latin else 'en'

    def _fallback_response(self):
        return {
            'parts': [{'type': 'text', 'content': "Could you please rephrase that?"}],
            'confidence': 0.0,
            'intent': 'unknown'
        }

    def _error_response(self):
        return {
            'parts': [{'type': 'text', 'content': "I'm having trouble understanding that."}],
            'confidence': 0.0,
            'intent': 'error'
        }
    
    def clear_cache(self):
        """Clear response and BOW caches to free memory"""
        self.response_cache.clear()
        self.bow_cache.clear()
        logger.info("Caches cleared")
    
    def get_cache_stats(self):
        """Get cache statistics for monitoring"""
        return {
            'response_cache_size': len(self.response_cache),
            'bow_cache_size': len(self.bow_cache)
        }