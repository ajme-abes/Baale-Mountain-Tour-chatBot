# 📁 Project Structure

This document provides a comprehensive overview of the Bale Mountains Explorer project structure.

## 🏗️ Root Directory

```
bale-mountains-explorer/
├── 📁 chatbot_backend/          # Django backend application
├── 📁 chatbot-frontend/         # React frontend application
├── 📁 docs/                     # Documentation files
├── 📄 README.md                 # Main project documentation
├── 📄 CONTRIBUTING.md           # Contribution guidelines
├── 📄 CHANGELOG.md              # Version history
├── 📄 LICENSE                   # MIT license
├── 📄 PROJECT_STRUCTURE.md      # This file
└── 📄 .gitignore               # Git ignore rules
```

## 🐍 Backend Structure (`chatbot_backend/`)

```
chatbot_backend/
├── 📁 chatapi/                  # Main Django app
│   ├── 📁 migrations/           # Database migrations
│   ├── 📁 utils/                # Utility modules
│   │   ├── 📄 chat_processor.py # Core NLP processing engine
│   │   ├── 📄 baale_mountain.json # Intents database
│   │   ├── 📄 chatbot_model.keras # Trained ML model
│   │   ├── 📄 vocabulary.pkl    # Word embeddings
│   │   ├── 📄 classes.pkl       # Intent classes
│   │   └── 📄 __init__.py
│   ├── 📄 __init__.py
│   ├── 📄 admin.py              # Django admin configuration
│   ├── 📄 apps.py               # App configuration
│   ├── 📄 models.py             # Database models
│   ├── 📄 tests.py              # Unit tests
│   ├── 📄 urls.py               # App URL patterns
│   └── 📄 views.py              # API views and endpoints
├── 📁 chatbot_backend/          # Django project settings
│   ├── 📄 __init__.py
│   ├── 📄 asgi.py               # ASGI configuration
│   ├── 📄 settings.py           # Django settings
│   ├── 📄 urls.py               # Main URL configuration
│   └── 📄 wsgi.py               # WSGI configuration
├── 📁 templates/                # HTML templates
├── 📁 static/                   # Static files
├── 📁 media/                    # Media files
├── 📄 manage.py                 # Django management script
├── 📄 requirements.txt          # Python dependencies
├── 📄 start_server.py           # Clean server startup script
├── 📄 setup_env.py              # Environment setup script
├── 📄 test_api.py               # API testing script
├── 📄 SETUP_GUIDE.md            # Backend setup guide
└── 📄 db.sqlite3               # SQLite database
```

### 🔧 Backend Key Files

#### `chatapi/utils/chat_processor.py`
- **Purpose**: Core NLP processing engine
- **Features**: Intent classification, response generation, caching
- **Dependencies**: TensorFlow, spaCy, NLTK

#### `chatapi/utils/baale_mountain.json`
- **Purpose**: Intent patterns and responses database
- **Structure**: 15+ intents with patterns and structured responses
- **Format**: JSON with nested response parts

#### `chatapi/views.py`
- **Purpose**: REST API endpoints
- **Endpoints**: `/api/chat/`, `/api/performance/`
- **Features**: Error handling, logging, performance monitoring

#### `chatbot_backend/settings.py`
- **Purpose**: Django configuration
- **Features**: CORS setup, logging, API keys, database config

## ⚛️ Frontend Structure (`chatbot-frontend/`)

```
chatbot-frontend/
├── 📁 public/                   # Public assets
│   ├── 📄 index.html            # Main HTML template
│   ├── 📄 manifest.json         # PWA manifest
│   ├── 📄 favicon.ico           # Favicon
│   └── 📁 icons/                # App icons
├── 📁 src/                      # Source code
│   ├── 📁 components/           # React components
│   │   ├── 📄 Header.js         # Desktop header component
│   │   ├── 📄 MobileHeader.js   # Mobile navigation header
│   │   ├── 📄 ParticleBackground.js # Animated background
│   │   ├── 📄 ImageCarousel.js  # Photo gallery carousel
│   │   ├── 📄 MessageBubble.js  # Chat message component
│   │   ├── 📄 QuickActions.js   # Quick action chips
│   │   ├── 📄 WelcomeMessage.js # Onboarding component
│   │   └── 📄 LoadingSpinner.js # Loading state component
│   ├── 📄 App.js                # Main app component
│   ├── 📄 ChatInterface.js      # Core chat interface
│   ├── 📄 theme.js              # Material-UI theme
│   ├── 📄 index.js              # App entry point
│   ├── 📄 App.css               # Global styles
│   └── 📄 index.css             # Base styles
├── 📄 package.json              # Node.js dependencies
├── 📄 package-lock.json         # Dependency lock file
├── 📄 README.md                 # Frontend documentation
├── 📄 FRONTEND_FEATURES.md      # Feature documentation
└── 📁 build/                    # Production build (generated)
```

### 🎨 Frontend Key Files

#### `src/ChatInterface.js`
- **Purpose**: Main chat interface component
- **Features**: Message handling, API communication, state management
- **Dependencies**: Axios, Material-UI, Framer Motion

#### `src/components/ImageCarousel.js`
- **Purpose**: Interactive photo gallery
- **Features**: Auto-rotation, navigation controls, smooth transitions
- **Images**: 6 stunning Bale Mountains photos

#### `src/components/MessageBubble.js`
- **Purpose**: Chat message rendering
- **Features**: Rich content support, animations, timestamps
- **Content Types**: Text, tables, lists, timelines, sections

#### `src/theme.js`
- **Purpose**: Material-UI theme configuration
- **Features**: Custom colors, typography, component overrides
- **Design**: Nature-inspired color palette

## 🗄️ Data Structure

### Intent Database Schema (`baale_mountain.json`)

```json
{
  "intents": [
    {
      "tag": "intent_name",
      "patterns": [
        "user input pattern 1",
        "user input pattern 2"
      ],
      "responses": [
        {
          "parts": [
            {
              "type": "header|text|list|table|section|timeline",
              "content": "response content"
            }
          ]
        }
      ]
    }
  ]
}
```

### Response Types

#### Text Response
```json
{
  "type": "text",
  "content": "Simple text response"
}
```

#### List Response
```json
{
  "type": "list",
  "content": [
    "List item 1",
    "List item 2"
  ]
}
```

#### Table Response
```json
{
  "type": "table",
  "columns": ["Column 1", "Column 2"],
  "rows": [
    ["Row 1 Col 1", "Row 1 Col 2"],
    ["Row 2 Col 1", "Row 2 Col 2"]
  ]
}
```

#### Section Response
```json
{
  "type": "section",
  "title": "Section Title",
  "content": [
    {
      "type": "text",
      "content": "Section content"
    }
  ]
}
```

## 🔄 Data Flow

### Request Flow
```
User Input → React Component → Axios → Django View → ChatProcessor → ML Model → Response
```

### Response Flow
```
ML Model → Intent Classification → Response Generation → JSON API → React Rendering → UI Display
```

## 🚀 Deployment Structure

### Development
```
Local Development:
├── Backend: http://localhost:8000
├── Frontend: http://localhost:3000
└── Database: SQLite (local file)
```

### Production
```
Production Deployment:
├── Backend: Django + Gunicorn + Nginx
├── Frontend: React Build + CDN
├── Database: PostgreSQL/MySQL
└── Caching: Redis (optional)
```

## 📦 Dependencies

### Backend Dependencies
- **Django 5.2**: Web framework
- **Django REST Framework**: API framework
- **TensorFlow 2.18**: Machine learning
- **spaCy 3.8**: Natural language processing
- **NLTK 3.9**: Text processing
- **NumPy**: Numerical computing
- **Requests**: HTTP client

### Frontend Dependencies
- **React 18.3**: UI framework
- **Material-UI 5.16**: Component library
- **Framer Motion 12.4**: Animation library
- **Axios 1.8**: HTTP client
- **React Draggable**: Drag functionality

## 🔧 Configuration Files

### Backend Configuration
- `settings.py`: Django settings
- `requirements.txt`: Python dependencies
- `manage.py`: Django management
- `start_server.py`: Custom startup script

### Frontend Configuration
- `package.json`: Node.js dependencies
- `public/manifest.json`: PWA configuration
- `src/theme.js`: UI theme configuration

## 📝 Documentation Files

- `README.md`: Main project documentation
- `CONTRIBUTING.md`: Contribution guidelines
- `CHANGELOG.md`: Version history
- `PROJECT_STRUCTURE.md`: This file
- `LICENSE`: MIT license
- `SETUP_GUIDE.md`: Backend setup guide
- `FRONTEND_FEATURES.md`: Frontend feature documentation

---

This structure provides a scalable, maintainable architecture for the Bale Mountains Explorer project, with clear separation of concerns and comprehensive documentation.