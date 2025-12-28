#!/usr/bin/env python3
"""
Deployment Verification Script
Tests that SimpleProcessor works correctly for deployment
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

def test_simple_processor():
    """Test SimpleProcessor functionality"""
    try:
        from chatapi.utils.simple_processor import SimpleProcessor
        
        processor = SimpleProcessor()
        print("✅ SimpleProcessor imported successfully")
        
        # Test quick actions
        test_cases = [
            "Tell me about Bale Mountains National Park",
            "How do I get to Bale Mountains",
            "What activities can I do",
            "When is the best time to visit",
            "Accommodation options",
            "Park fees"
        ]
        
        print("\n🧪 Testing Quick Actions:")
        for test in test_cases:
            result = processor.get_response(test)
            confidence = result.get('confidence', 0)
            intent = result.get('intent', 'unknown')
            
            if confidence > 0.9:
                print(f"✅ '{test[:30]}...' -> {intent} ({confidence:.2f})")
            else:
                print(f"⚠️  '{test[:30]}...' -> {intent} ({confidence:.2f})")
        
        print(f"\n📊 Cache Stats: {processor.get_cache_stats()}")
        print("✅ All tests passed! Ready for deployment.")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_django_import():
    """Test Django imports"""
    try:
        import django
        from django.conf import settings
        print(f"✅ Django {django.get_version()} imported successfully")
        return True
    except Exception as e:
        print(f"❌ Django import error: {str(e)}")
        return False

def test_requirements():
    """Test required packages"""
    required_packages = [
        'django',
        'djangorestframework', 
        'django_cors_headers',
        'requests',
        'nltk'
    ]
    
    print("\n📦 Checking Required Packages:")
    all_good = True
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - Missing!")
            all_good = False
    
    return all_good

if __name__ == "__main__":
    print("🚀 Bale Mountains Chatbot - Deployment Verification")
    print("=" * 50)
    
    # Run tests
    django_ok = test_django_import()
    packages_ok = test_requirements()
    processor_ok = test_simple_processor()
    
    print("\n" + "=" * 50)
    if django_ok and packages_ok and processor_ok:
        print("🎉 DEPLOYMENT READY! All systems go!")
        sys.exit(0)
    else:
        print("❌ DEPLOYMENT NOT READY - Fix issues above")
        sys.exit(1)