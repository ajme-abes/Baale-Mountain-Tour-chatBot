#!/usr/bin/env python3
"""
Simple deployment test to verify no spaCy dependencies are required
"""

import os
import sys
import django
from django.conf import settings

# Set environment variables to force SimpleProcessor
os.environ['USE_SIMPLE_PROCESSOR'] = 'true'
os.environ['RENDER'] = 'true'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_backend.settings')

# Initialize Django
django.setup()

def test_imports():
    """Test that all required imports work without spaCy"""
    try:
        print("Testing Django imports...")
        print("✅ Django imports successful")
        
        print("Testing SimpleProcessor import...")
        from chatapi.utils.simple_processor import SimpleProcessor
        print("✅ SimpleProcessor import successful")
        
        print("Testing SimpleProcessor initialization...")
        processor = SimpleProcessor()
        print("✅ SimpleProcessor initialization successful")
        
        print("Testing SimpleProcessor response...")
        result = processor.get_response("Tell me about Bale Mountains National Park")
        print(f"✅ SimpleProcessor response: {result['intent']} ({result['confidence']})")
        
        print("Testing views import...")
        from chatapi.views_deployment import ChatView
        print("✅ Deployment views import successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🧪 Deployment Test - No spaCy Dependencies")
    print("=" * 50)
    
    if test_imports():
        print("\n🎉 All tests passed! Deployment ready.")
        sys.exit(0)
    else:
        print("\n❌ Tests failed! Fix issues before deployment.")
        sys.exit(1)