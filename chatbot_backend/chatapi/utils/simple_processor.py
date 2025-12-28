import json
import random
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

class SimpleProcessor:
    """
    Lightweight chat processor for deployment without heavy ML dependencies.
    Uses pattern matching instead of ML models for intent recognition.
    """
    
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.response_cache = {}
        
        try:
            self._load_intents()
            logger.info("SimpleProcessor initialized successfully")
        except Exception as e:
            logger.error(f"SimpleProcessor initialization failed: {str(e)}")
            self.intents = {"intents": []}
    
    def _load_intents(self):
        """Load intents from JSON file"""
        try:
            intents_path = self.BASE_DIR / 'chatapi/utils/baale_mountain.json'
            with open(intents_path, 'r', encoding='utf-8-sig') as f:
                self.intents = json.load(f)
            logger.info("Intents loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load intents: {str(e)}")
            # Fallback intents
            self.intents = {
                "intents": [
                    {
                        "tag": "greeting",
                        "patterns": ["hello", "hi", "hey"],
                        "responses": [{"type": "text", "content": "Hello! How can I help you with Bale Mountains?"}]
                    },
                    {
                        "tag": "fallback",
                        "patterns": [],
                        "responses": [{"type": "text", "content": "I'd be happy to help you learn about Bale Mountains National Park!"}]
                    }
                ]
            }
    
    def get_response(self, text, threshold=0.7):
        """
        Get response using pattern matching instead of ML models
        """
        try:
            # Check cache first
            cache_key = text.strip().lower()
            if cache_key in self.response_cache:
                return self.response_cache[cache_key]
            
            # Clean input
            cleaned_input = cache_key
            
            # Quick action pattern matching
            quick_response = self._handle_quick_actions(cleaned_input)
            if quick_response:
                self.response_cache[cache_key] = quick_response
                return quick_response
            
            # Pattern matching for intents
            best_intent = self._match_intent(cleaned_input)
            
            if best_intent:
                response = random.choice(best_intent.get('responses', []))
                result = {
                    'parts': response.get('parts', [response]) if 'parts' in response else [response],
                    'confidence': 0.85,
                    'intent': best_intent.get('tag', 'unknown')
                }
                self.response_cache[cache_key] = result
                return result
            
            # Fallback response
            result = self._fallback_response()
            self.response_cache[cache_key] = result
            return result
            
        except Exception as e:
            logger.error(f"Response generation failed: {str(e)}")
            return self._error_response()
    
    def _match_intent(self, text):
        """Match intent using simple pattern matching"""
        best_match = None
        best_score = 0
        
        for intent in self.intents.get('intents', []):
            patterns = intent.get('patterns', [])
            score = 0
            
            for pattern in patterns:
                pattern_lower = pattern.lower()
                # Simple keyword matching
                if pattern_lower in text:
                    score += 1
                # Partial matching
                elif any(word in text for word in pattern_lower.split()):
                    score += 0.5
            
            if score > best_score:
                best_score = score
                best_match = intent
        
        return best_match if best_score > 0 else None
    
    def _handle_quick_actions(self, cleaned_input):
        """Handle specific quick action queries with direct responses"""
        
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
                    'type': 'list',
                    'content': [
                        'Route 1: Via Addis Ababa - Shashemene - Goba (460km, 6-8 hours)',
                        'Route 2: Via Addis Ababa - Dodola - Adaba (380km, 5-7 hours)',
                        'Route 3: Via Addis Ababa - Ziway - Shashemene (450km, 6-7 hours)'
                    ]
                }, {
                    'type': 'text',
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
                    'content': 'There are several accommodation options available for visitors:'
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
                    'type': 'text',
                    'content': '💡 Additional fees may apply for camping, guides, and special activities.'
                }],
                'confidence': 0.95,
                'intent': 'park_fees'
            }
        
        return None
    
    def _fallback_response(self):
        """Fallback response for unknown queries"""
        return {
            'parts': [{
                'type': 'text',
                'content': "I'd be happy to help you learn about Bale Mountains National Park! You can ask me about park information, how to get there, accommodations, activities, best times to visit, or park fees."
            }],
            'confidence': 0.5,
            'intent': 'fallback'
        }
    
    def _error_response(self):
        """Error response"""
        return {
            'parts': [{
                'type': 'text',
                'content': "I'm having trouble processing your request right now. Please try asking about Bale Mountains National Park information, directions, or activities."
            }],
            'confidence': 0.0,
            'intent': 'error'
        }
    
    def clear_cache(self):
        """Clear response cache"""
        self.response_cache.clear()
        logger.info("Cache cleared")
    
    def get_cache_stats(self):
        """Get cache statistics"""
        return {
            'response_cache_size': len(self.response_cache),
            'bow_cache_size': 0  # Not used in simple processor
        }