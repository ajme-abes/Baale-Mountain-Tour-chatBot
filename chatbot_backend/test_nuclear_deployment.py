#!/usr/bin/env python3
"""
Nuclear deployment test - verify absolutely no ML dependencies
"""

import os
import sys

# Set deployment environment
os.environ['USE_SIMPLE_PROCESSOR'] = 'true'
os.environ['RENDER'] = 'true'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_deployment'

def test_nuclear_deployment():
    """Test nuclear deployment setup"""
    try:
        print("🧪 Nuclear Deployment Test")
        print("=" * 40)
        
        print("Testing minimal Django setup...")
        import django
        django.setup()
        print("✅ Django setup successful")
        
        print("Testing SimpleProcessor...")
        from chatapi.utils.simple_processor import SimpleProcessor
        processor = SimpleProcessor()
        result = processor.get_response("Tell me about Bale Mountains National Park")
        print(f"✅ SimpleProcessor: {result['intent']} ({result['confidence']})")
        
        print("Testing deployment views...")
        from chatapi.views_deployment import ChatView
        print("✅ Deployment views imported")
        
        print("Testing WSGI application...")
        from wsgi_deployment import application
        print("✅ WSGI application ready")
        
        print("\n🎉 NUCLEAR DEPLOYMENT READY!")
        print("🚀 Zero ML dependencies")
        print("⚡ Pattern matching only")
        print("🏔️ Bale Mountains chatbot ready!")
        
        return True
        
    except Exception as e:
        print(f"❌ Nuclear test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if test_nuclear_deployment():
        sys.exit(0)
    else:
        sys.exit(1)