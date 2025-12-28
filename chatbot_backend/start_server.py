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
    
    # Check if we're on Render (production)
    if os.environ.get('RENDER'):
        print("🚀 Starting production server on Render...")
        try:
            # Use Gunicorn for production
            subprocess.run([
                sys.executable, 
                "-m", "gunicorn",
                "--bind", f"0.0.0.0:{os.environ.get('PORT', '8000')}",
                "--workers", "2",
                "--timeout", "120",
                "chatbot_backend.wsgi:application"
            ], check=True)
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Server failed to start: {e}")
            sys.exit(1)
    else:
        # Development server
        try:
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