#!/usr/bin/env python3
"""
Setup script for Bale Mountains Chatbot
Helps users install the right dependencies for their environment
"""

import sys
import subprocess
import os

def install_requirements(requirements_file):
    """Install requirements from specified file"""
    try:
        print(f"Installing requirements from {requirements_file}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print(f"✅ Successfully installed requirements from {requirements_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def setup_nltk():
    """Download required NLTK data"""
    try:
        import nltk
        print("Downloading NLTK data...")
        nltk.download('punkt', quiet=True)
        print("✅ NLTK data downloaded successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")
        return False

def main():
    print("🚀 Bale Mountains Chatbot Setup")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('requirements.txt'):
        print("❌ Error: requirements.txt not found!")
        print("Please run this script from the chatbot_backend directory")
        sys.exit(1)
    
    print("Choose your setup type:")
    print("1. 🚀 Deployment/Production (lightweight, no ML models)")
    print("2. 💻 Development (full ML capabilities)")
    print("3. 🔧 Custom (choose your own requirements file)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        # Production setup
        print("\n🚀 Setting up for deployment/production...")
        success = install_requirements("requirements.txt")
        if success:
            setup_nltk()
            print("\n✅ Production setup complete!")
            print("Your chatbot will use SimpleProcessor with pattern matching.")
            print("Response time: ~200-300ms, Memory usage: <100MB")
        
    elif choice == "2":
        # Development setup
        print("\n💻 Setting up for development...")
        if os.path.exists("requirements-dev.txt"):
            success = install_requirements("requirements-dev.txt")
            if success:
                setup_nltk()
                print("\n✅ Development setup complete!")
                print("Your chatbot will use ChatProcessor with ML models.")
                print("Don't forget to run: python download_models.py")
        else:
            print("❌ requirements-dev.txt not found!")
            print("Installing basic requirements instead...")
            install_requirements("requirements.txt")
    
    elif choice == "3":
        # Custom setup
        requirements_file = input("Enter requirements file name: ").strip()
        if os.path.exists(requirements_file):
            install_requirements(requirements_file)
            setup_nltk()
        else:
            print(f"❌ File {requirements_file} not found!")
    
    else:
        print("❌ Invalid choice!")
        sys.exit(1)
    
    print("\n🎉 Setup complete! You can now run:")
    print("python manage.py runserver")

if __name__ == "__main__":
    main()