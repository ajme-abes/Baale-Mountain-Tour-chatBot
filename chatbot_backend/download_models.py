#!/usr/bin/env python3
"""
Download script for large ML models.
This script downloads the required BERT models for the chatbot.
"""

import os
import requests
import zipfile
from pathlib import Path

def download_models():
    """Download required ML models for the chatbot."""
    
    base_dir = Path(__file__).parent
    models_dir = base_dir / "models"
    models_dir.mkdir(exist_ok=True)
    
    print("🤖 Downloading Bale Mountains Chatbot Models...")
    
    # Model URLs (you would host these on Google Drive, Dropbox, etc.)
    models = {
        "bert_baale_model.zip": "https://your-storage-url/bert_baale_model.zip",
        "bert_baale_tokenizer.zip": "https://your-storage-url/bert_baale_tokenizer.zip"
    }
    
    for model_name, url in models.items():
        model_path = models_dir / model_name
        extract_path = base_dir / model_name.replace('.zip', '')
        
        if extract_path.exists():
            print(f"✅ {model_name} already exists")
            continue
            
        print(f"📥 Downloading {model_name}...")
        
        # Download model (placeholder - replace with actual URLs)
        print(f"⚠️  Please manually download {model_name} from your storage")
        print(f"   Expected location: {extract_path}")
    
    print("\n💡 Setup Instructions:")
    print("1. Download the BERT models from your cloud storage")
    print("2. Extract them to the chatbot_backend directory")
    print("3. Ensure the following directories exist:")
    print("   - bert_baale_model/")
    print("   - bert_baale_tokenizer/")
    print("\n🚀 Then run: python start_server.py")

if __name__ == "__main__":
    download_models()