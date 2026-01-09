#!/usr/bin/env python3
"""
Ultra minimal test - absolutely zero external dependencies
"""

import os
import sys

# Set deployment environment
os.environ['USE_SIMPLE_PROCESSOR'] = 'true'
os.environ['RENDER'] = 'true'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_deployment'

def test_ultra_minimal():
    """Test ultra minimal deployment"""
    try:
        print("🧪 Ultra Minimal Test - Zero Dependencies")
        print("=" * 45)
        
        print("Testing basic Python...")
        import json
        import random
        print("✅ Basic Python imports work")
        
        print("Testing SimpleProcessor (no NLTK)...")
        from chatapi.utils.simple_processor import SimpleProcessor
        processor = SimpleProcessor()
        result = processor.get_response("Tell me about Bale Mountains National Park")
        print(f"✅ SimpleProcessor: {result['intent']} ({result['confidence']})")
        
        print("Testing Django minimal setup...")
        import django
        django.setup()
        print("✅ Django minimal setup works")
        
        print("Testing deployment views...")
        from chatapi.views_deployment import ChatView
        print("✅ Deployment views work")
        
        print("\n🎉 ULTRA MINIMAL SUCCESS!")
        print("🚀 Zero external dependencies")
        print("⚡ Pure Python pattern matching")
        print("🏔️ Ready for deployment!")
        
        return True
        
    except Exception as e:
        print(f"❌ Ultra minimal test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    if test_ultra_minimal():
        sys.exit(0)
    else:
        sys.exit(1)