#!/usr/bin/env python3
"""
Minimal Django startup script for deployment
Avoids any imports that might trigger spaCy dependencies
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Set environment variables for deployment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_backend.settings')
os.environ['USE_SIMPLE_PROCESSOR'] = 'true'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize Django
django.setup()

# Get WSGI application
application = get_wsgi_application()

if __name__ == "__main__":
    print("🚀 Minimal Django startup for deployment")
    print("Using SimpleProcessor (no ML dependencies)")
    
    # Test that SimpleProcessor works
    try:
        from chatapi.utils.simple_processor import SimpleProcessor
        processor = SimpleProcessor()
        result = processor.get_response("test")
        print(f"✅ SimpleProcessor working: {result['confidence'] > 0}")
    except Exception as e:
        print(f"❌ SimpleProcessor test failed: {e}")
        sys.exit(1)
    
    print("✅ Ready for deployment!")