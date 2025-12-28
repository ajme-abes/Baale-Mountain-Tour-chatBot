#!/usr/bin/env python3
"""
Environment setup script for the chatbot backend.
This script sets up necessary environment variables and suppresses warnings.
"""

import os
import sys
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_environment():
    """Set up environment variables to suppress warnings and optimize performance."""
    
    # TensorFlow environment variables
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress INFO and WARNING messages
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN optimizations
    os.environ['PYTHONWARNINGS'] = 'ignore'  # Suppress Python warnings
    
    logger.info("Environment variables set successfully")
    
    # Check if spaCy model is installed
    try:
        import spacy
        spacy.load("en_core_web_lg")
        logger.info("spaCy model 'en_core_web_lg' is available")
    except OSError:
        logger.warning("spaCy model 'en_core_web_lg' not found. Attempting to download...")
        try:
            subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_lg"], check=True)
            logger.info("spaCy model downloaded successfully")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to download spaCy model: {e}")
            return False
    except ImportError:
        logger.error("spaCy is not installed. Please install it with: pip install spacy")
        return False
    
    return True

def check_dependencies():
    """Check if all required dependencies are installed."""
    required_packages = [
        'django',
        'djangorestframework',
        'django-cors-headers',
        'tensorflow',
        'nltk',
        'spacy',
        'numpy',
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            logger.info(f"✓ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            logger.error(f"✗ {package} is missing")
    
    if missing_packages:
        logger.error(f"Missing packages: {', '.join(missing_packages)}")
        logger.info("Install missing packages with: pip install " + " ".join(missing_packages))
        return False
    
    logger.info("All dependencies are installed")
    return True

if __name__ == "__main__":
    logger.info("Setting up chatbot backend environment...")
    
    if not check_dependencies():
        logger.error("Dependency check failed. Please install missing packages.")
        sys.exit(1)
    
    if not setup_environment():
        logger.error("Environment setup failed.")
        sys.exit(1)
    
    logger.info("Environment setup completed successfully!")
    logger.info("You can now run: python manage.py runserver")