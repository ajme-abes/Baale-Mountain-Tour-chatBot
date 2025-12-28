# chatapi/views.py
import logging
import os
import warnings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Import SimpleProcessor for deployment (lightweight)
try:
    from .utils.simple_processor import SimpleProcessor as ChatProcessor
    PROCESSOR_TYPE = "SimpleProcessor"
except ImportError:
    # Fallback to full ChatProcessor for local development
    from .utils.chat_processor import ChatProcessor
    PROCESSOR_TYPE = "ChatProcessor"

from django.conf import settings
import requests

# Suppress warnings
warnings.filterwarnings('ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

logger = logging.getLogger(__name__)

# Initialize processor once to avoid repeated initialization
try:
    chat_processor = ChatProcessor()
    logger.info(f"{PROCESSOR_TYPE} initialized successfully in views")
except Exception as e:
    logger.error(f"Failed to initialize {PROCESSOR_TYPE}: {str(e)}")
    chat_processor = None

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
                "status": "online",
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
            # Check if ChatProcessor is available
            if chat_processor is None:
                logger.error("ChatProcessor not initialized")
                return Response(
                    {
                        "text": "I'm sorry, but the chat service is currently unavailable. Please try again later.",
                        "error": "Service initialization failed"
                    },
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
            
            # Validate input
            message = request.data.get('message', '').strip()
            if not message:
                return Response(
                    {"error": "Message cannot be empty"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            logger.info(f"Processing message: {message[:50]}...")
            
            # Process the message
            response_data = chat_processor.get_response(message)
            
            logger.info("Message processed successfully")
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"POST Error: {str(e)}", exc_info=True)
            return Response(
                {
                    "text": "I apologize, but I encountered an error while processing your request. Please try again.",
                    "error": "Processing failed"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PerformanceView(APIView):
    """
    Performance monitoring endpoint
    """
    def get(self, request):
        try:
            if chat_processor:
                cache_stats = chat_processor.get_cache_stats()
                return Response({
                    "status": "healthy",
                    "cache_stats": cache_stats,
                    "processor_available": True
                })
            else:
                return Response({
                    "status": "unhealthy",
                    "processor_available": False
                }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            logger.error(f"Performance check failed: {str(e)}")
            return Response({
                "status": "error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def weather_api(request):
    """Weather endpoint handler"""
    try:
        location = request.GET.get('location', 'Bale Mountains')
        if chat_processor:
            # Try to get weather data if processor supports it
            if hasattr(chat_processor, '_get_weather'):
                weather_data = chat_processor._get_weather(location)
                if weather_data:
                    return Response(weather_data)
        
        # Fallback weather response
        return Response({
            "location": location,
            "temperature": "15-25°C",
            "condition": "Cool mountain climate",
            "note": "Weather data from local climate patterns"
        })

    except Exception as e:
        logger.error(f"Weather API error: {str(e)}", exc_info=True)
        return Response(
            {"error": "Weather service unavailable"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )