# chatapi/views.py
import logging
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .utils.chat_processor import ChatProcessor
from django.conf import settings
import requests

logger = logging.getLogger(__name__)

class ChatView(APIView):
    """
    Handles GET requests for API documentation and POST requests for chat processing
    """
    http_method_names = ['get', 'post']

    def get(self, request):
        """
        GET endpoint for API documentation
        """
        try:
            return Response({
                "message": "Bale Mountains National Park Chat API",
                "documentation": {
                    "POST /api/chat/": {
                        "description": "Process chat messages",
                        "parameters": {
                            "message": "String containing user query"
                        },
                        "example_request": {
                            "message": "What's the history of Bale Mountains?"
                        }
                    }
                }
            })
        except Exception as e:
            logger.error(f"GET Error: {str(e)}", exc_info=True)
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        """
        POST endpoint for processing chat messages
        """
        try:
            # Validate input
            message = request.data.get('message', '').strip()
            if not message:
                return Response(
                    {"error": "Message cannot be empty"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            logger.info(f"Processing message: {message[:50]}...")
            
            # Process message
            processor = ChatProcessor()
            response = processor.get_response(message)
            
            # Ensure response format matches frontend expectations
            formatted_response = {
                "parts": response.get("parts", []),
                "confidence": response.get("confidence", 0.0),
                "intent": response.get("intent", "unknown"),
                "response_text": response.get("parts", [{}])[0].get("content", "") if response.get("parts") else "No response generated."
            }

            return Response(formatted_response)

        except Exception as e:
            logger.error(f"POST Error: {str(e)}", exc_info=True)
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
@api_view(['GET'])
def weather_api(request):
    """Weather endpoint handler"""
    try:
        location = request.GET.get('location', 'Bale Mountains')
        processor = ChatProcessor()
        weather_data = processor._get_weather(location)

        if weather_data:
            return Response(weather_data)

        return Response(
            {"error": "Weather data unavailable"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )

    except Exception as e:
        logger.error(f"Weather API error: {str(e)}", exc_info=True)
        return Response(
            {"error": "Internal server error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
   

"""
# chatapi/views.py
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.chat_processor import ChatProcessor
from chatapi.views import ChatView  # ← Should match exactly


logger = logging.getLogger(__name__)

class ChatView(APIView):
    http_method_names = ['get', 'post']  # Allow both GET and POST

    def get(self, request):
        ##Provide API documentation for developers
        return Response({
            "message": "Chat API Endpoint",
            "instructions": "Send a POST request with JSON payload containing 'message'",
            "example_request": {
                "message": "Hello, how are you?"
            },
            "example_response": {
                "response": "I'm just a chatbot, but I'm functioning well!",
                "confidence": 0.92
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):
        ##Handle chat message processing
        try:
            message = request.data.get('message', '').strip()
            if not message:
                logger.warning("Received empty message request")
                return Response(
                    {"error": "Message cannot be empty", "code": "empty_message"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            logger.info(f"Processing message: {message[:50]}")  # Log first 50 chars
            processor = ChatProcessor()
            response = processor.get_response(message)
            
            # Standardize response format
            return Response({
                "success": True,
                "response": response,
                "meta": {
                    "length": len(response),
                    "processed_chars": len(message)
                }
            })

        except Exception as e:
            logger.error(f"API Error: {str(e)}", exc_info=True)
            return Response(
                {
                    "success": False,
                    "error": "Internal server error",
                    "code": "server_error",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
"""