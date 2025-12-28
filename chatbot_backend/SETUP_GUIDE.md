# 🏔️ Bale Mountains Chatbot Backend - Setup Guide

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
cd chatbot_backend
pip install -r requirements.txt
```

### 2. Download spaCy Model
```bash
python -m spacy download en_core_web_lg
```

### 3. Run Setup Script (Optional)
```bash
python setup_env.py
```

### 4. Start the Server
```bash
# Option 1: Clean startup (recommended)
python start_server.py

# Option 2: Standard Django
python manage.py runserver
```

## 🔧 Troubleshooting

### spaCy Model Error
If you see: `Can't find model 'en_core_web_lg'`

**Solution:**
```bash
python -m spacy download en_core_web_lg
```

### TensorFlow Warnings
The setup automatically suppresses TensorFlow warnings. If you still see them:

**Manual fix:**
```bash
# Windows
set TF_CPP_MIN_LOG_LEVEL=2
set TF_ENABLE_ONEDNN_OPTS=0

# Linux/Mac
export TF_CPP_MIN_LOG_LEVEL=2
export TF_ENABLE_ONEDNN_OPTS=0
```

### Missing Dependencies
```bash
pip install django djangorestframework django-cors-headers
pip install tensorflow nltk spacy numpy requests
```

## 📁 Project Structure
```
chatbot_backend/
├── chatapi/
│   ├── utils/
│   │   ├── chat_processor.py    # Main NLP processing
│   │   ├── chatbot_model.keras  # Trained model
│   │   ├── vocabulary.pkl       # Word embeddings
│   │   ├── classes.pkl          # Intent classes
│   │   └── baale_mountain.json  # Intents database
│   ├── views.py                 # API endpoints
│   └── models.py                # Database models
├── chatbot_backend/
│   ├── settings.py              # Django settings
│   └── urls.py                  # URL routing
├── manage.py                    # Django management
├── start_server.py              # Clean startup script
├── setup_env.py                 # Environment setup
└── requirements.txt             # Dependencies
```

## 🌐 API Endpoints

### GET /api/chat/
Returns API documentation and status

### POST /api/chat/
Process chat messages
```json
{
  "message": "What's the history of Bale Mountains?"
}
```

## 🎯 Features
- ✅ Intent-based conversation system
- ✅ 15+ intent categories
- ✅ Multilingual support (Amharic/English)
- ✅ Rich response formatting
- ✅ Error handling and fallbacks
- ✅ Confidence scoring
- ✅ Translation support

## 🔍 Monitoring
The server logs all requests and errors. Check the console output for:
- Request processing status
- Error messages
- Model loading status
- Performance metrics

## 🚨 Common Issues

1. **Port already in use**: Change port with `python manage.py runserver 8001`
2. **Model loading slow**: First load takes time, subsequent requests are fast
3. **Memory usage**: TensorFlow models use significant RAM (2-4GB normal)

## 📞 Support
If you encounter issues:
1. Check the console logs
2. Verify all dependencies are installed
3. Ensure spaCy model is downloaded
4. Try the setup script: `python setup_env.py`