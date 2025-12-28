#!/usr/bin/env python3
"""
Simple test script to verify the chatbot API is working correctly.
"""

import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_api_health():
    """Test if the API is responding"""
    try:
        response = requests.get(f"{BASE_URL}/api/chat/", timeout=5)
        if response.status_code == 200:
            print("✅ API is healthy")
            return True
        else:
            print(f"❌ API returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ API connection failed: {e}")
        return False

def test_performance():
    """Test performance endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/api/performance/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Performance endpoint working")
            print(f"   Cache stats: {data.get('cache_stats', {})}")
            return True
        else:
            print(f"❌ Performance endpoint returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Performance endpoint failed: {e}")
        return False

def test_chat_response(message):
    """Test a chat message"""
    try:
        start_time = time.time()
        response = requests.post(
            f"{BASE_URL}/api/chat/",
            json={"message": message},
            timeout=10
        )
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"✅ Chat response received in {response_time:.0f}ms")
            print(f"   Intent: {data.get('intent', 'unknown')}")
            print(f"   Confidence: {data.get('confidence', 0):.2f}")
            return True
        else:
            print(f"❌ Chat request failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Chat request failed: {e}")
        return False

def main():
    print("🏔️  Testing Bale Mountains Chatbot API")
    print("=" * 50)
    
    # Test API health
    if not test_api_health():
        print("\n❌ API health check failed. Make sure the server is running.")
        return
    
    # Test performance endpoint
    test_performance()
    
    # Test common queries
    test_queries = [
        "Hello",
        "Tell me about Bale Mountains National Park",
        "How do I get to Bale Mountains?",
        "What are the accommodation options?",
        "What activities can I do in the park?"
    ]
    
    print(f"\n🧪 Testing {len(test_queries)} common queries...")
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Testing: '{query}'")
        test_chat_response(query)
    
    print("\n✅ All tests completed!")
    print("\n💡 Tips for faster responses:")
    print("   - Repeated queries will be cached")
    print("   - First query may be slower due to model loading")
    print("   - Check /api/performance/ for cache statistics")

if __name__ == "__main__":
    main()