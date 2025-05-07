import json
import numpy as np 
import nltk 
import random
import spacy
import pickle
import logging
import requests
from datetime import datetime 
from pathlib import Path
from tensorflow.keras.models import load_model 
from django.conf import settings

logger = logging.getLogger(__name__)

class ChatProcessor:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.lemmatizer = nltk.WordNetLemmatizer()
        self.nlp = spacy.load("en_core_web_lg")
        self.CULTURAL_KEYWORDS = {"museum", "gallery", "exhibit", "art", "history", "heritage"}
        self.CULTURAL_TEMPLATE = self.nlp("Visit a museum or art gallery")
        self.translation_cache = {}
        try:
            self._download_nltk_resources()
            self._load_artifacts()
            self._verify_compatibility()
            logger.info("ChatProcessor initialized successfully")
        except Exception as e:
            logger.critical(f"Initialization failed: {str(e)}", exc_info=True)
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
            # Pre-process input
            cleaned_input = text.strip().lower()
        
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
                       return {
                          'parts': [{'type': 'text', 'content': processed_content}],
                          'confidence': 1.0,  # Max confidence for direct match
                          'intent': intent_tag
                        }
        
            # 2. Process other intents
            detected_lang = self._detect_language(text)
            if detected_lang != 'en':
               text = self._translate_text(text, target_lang='en')
               
            bow = self.create_bow(text)
            predictions = self.model.predict(np.array([bow], dtype=np.float32))[0]
            results = sorted(
                ((i, float(conf)) for i, conf in enumerate(predictions) if conf > threshold),
                key=lambda x: x[1], reverse=True
            )
        
            if not results:
               return self._fallback_response()
        
            top_idx, top_conf = results[0]
            intent_tag = self.classes[top_idx]
        
            # Special handling for regular greetings
            if intent_tag == 'greeting':
              for intent in self.intents.get('intents', []):
                  if intent.get('tag') == 'greeting':
                      response = random.choice(intent.get('responses', []))
                      return {
                          'parts': [response],  # Directly use greeting response
                          'confidence': top_conf,
                          'intent': intent_tag
                        }
        
            for intent in self.intents.get('intents', []):
                if intent.get('tag') == intent_tag:
                   response = random.choice(intent.get('responses', []))
                   processed_parts = []
                
                   for part in response.get('parts', []):
                       processed_part = self.process_response_part(part)
                       processed_parts.append(processed_part)
                
                   return {
                    'parts': processed_parts,
                    'confidence': top_conf,
                    'intent': intent_tag
                    }
                
            return self._fallback_response()
    
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}", exc_info=True)
            return self._error_response()
    
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