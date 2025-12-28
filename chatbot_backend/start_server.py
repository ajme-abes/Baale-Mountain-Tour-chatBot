#!/usr/bin/env python3
"""
Clean startup script for the Django chatbot backend.
This script sets environment variables and starts the Django development server.
"""

import os
import sys
import subprocess
import warnings

def setup_clean_environment():
    """Set up a clean environment with suppressed warnings."""
    
    # Suppress TensorFlow warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    
    # Suppress Python warnings
    warnings.filterwarnings('ignore', category=FutureWarning)
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    warnings.filterwarnings('ignore', category=UserWarning)
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_backend.settings')

def start_server():
    """Start the Django development server with clean output."""
    
    print("🏔️  Starting Bale Mountains Chatbot Backend...")
    print("=" * 50)
    
    setup_clean_environment()
    
    try:
        # Run Django development server
        subprocess.run([
            sys.executable, 
            "manage.py", 
            "runserver", 
            "127.0.0.1:8000"
        ], check=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Server failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()