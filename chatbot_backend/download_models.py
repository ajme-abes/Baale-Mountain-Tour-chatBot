#!/usr/bin/env python3
"""
Model Download Script for Bale Mountains Explorer

This script downloads the required ML models that are too large for GitHub.
Run this after cloning the repository to set up the AI models.
"""

import os
import sys
import requests
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_file(url, local_path, description):
    """Download a file with progress indication"""
    try:
        logger.info(f"Downloading {description}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\rProgress: {progress:.1f}%", end='', flush=True)
        
        print()  # New line after progress
        logger.info(f"✅ {description} downloaded successfully")
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to download {description}: {str(e)}")
        return False

def main():
    """Main function to download all required models"""
    logger.info("🏔️ Bale Mountains Explorer - Model Download Script")
    logger.info("=" * 60)
    
    base_dir = Path(__file__).parent
    
    # Model URLs (you'll need to host these somewhere accessible)
    models = [
        {
            'url': 'https://your-storage-url.com/tf_model.h5',  # Replace with actual URL
            'path': base_dir / 'bert_baale_model' / 'tf_model.h5',
            'description': 'TensorFlow BERT Model (418MB)'
        },
        # Add more models as needed
    ]
    
    # Create directories if they don't exist
    for model in models:
        model['path'].parent.mkdir(parents=True, exist_ok=True)
    
    # Download models
    success_count = 0
    for model in models:
        if model['path'].exists():
            logger.info(f"⏭️  {model['description']} already exists, skipping...")
            success_count += 1
            continue
            
        if download_file(model['url'], model['path'], model['description']):
            success_count += 1
    
    # Summary
    logger.info("=" * 60)
    if success_count == len(models):
        logger.info("🎉 All models downloaded successfully!")
        logger.info("You can now run the chatbot with: python start_server.py")
    else:
        logger.warning(f"⚠️  {len(models) - success_count} models failed to download")
        logger.info("Please check the URLs and try again")
    
    return success_count == len(models)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)