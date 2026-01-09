# 🏔️ Bale Mountains Explorer - AI Travel Chatbot

A modern, intelligent travel chatbot for exploring Ethiopia's stunning Bale Mountains National Park. Built with Django REST API backend and React frontend.

## 🌟 Live Demo

- **Frontend**: [Bale Mountains Explorer](https://baale-mountain-tour-chatbot.netlify.app)
- **Backend API**: [API Documentation](https://bale-mountains-backend.onrender.com)

## 📸 Screenshots

![Bale Mountains Chatbot](https://via.placeholder.com/800x400/2E7D32/FFFFFF?text=Bale+Mountains+Explorer)

### ✨ Key Features

- 🤖 **Advanced AI Chatbot** - Powered by pattern matching for natural language understanding
- � **vBeautiful Modern UI** - Glass morphism design with smooth animations
- 📱 **Fully Responsive** - Optimized for desktop, tablet, and mobile devices
- ⚡ **Lightning Fast** - Optimized performance with caching and smart responses
- 🌍 **Multi-language Support** - Available in multiple languages
- 🎯 **Smart Quick Actions** - Pre-defined buttons for common queries
- 📊 **Real-time Analytics** - Track user interactions and popular queries
- 🔒 **Secure & Private** - No personal data stored, privacy-first approach

## 🏗️ Architecture

### Frontend Stack
```
React 18.3 + Material-UI 5.16 + Framer Motion 12.4
├── Modern Component Architecture
├── Glass Morphism Design System
├── Responsive Grid Layout
├── Smooth Page Transitions
└── Progressive Web App (PWA)
```

### Backend Stack
```
Django 5.2 + Django REST Framework 3.15
├── Pattern-based Intent Recognition
├── Response Caching System
├── RESTful API Design
├── CORS Configuration
└── Production-Ready Deployment
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- Git

### Backend Setup
```bash
# Clone repository
git clone https://github.com/ajme-abes/Baale-Mountain-Tour-chatBot.git
cd Baale-Mountain-Tour-chatBot

# Setup backend
cd chatbot_backend
pip install -r requirements.txt
python manage.py runserver
```

### Frontend Setup
```bash
# Setup frontend
cd chatbot-frontend
npm install
npm start
```

## 📁 Project Structure

```
Baale-Mountain-Tour-chatBot/
├── 📂 chatbot_backend/          # Django REST API
│   ├── 📂 chatapi/              # Main API app
│   │   ├── 📂 utils/            # Core processing logic
│   │   │   ├── simple_processor.py    # Pattern matching engine
│   │   │   └── baale_mountain.json   # Intent database
│   │   ├── views.py             # API endpoints
│   │   └── urls.py              # URL routing
│   ├── 📂 chatbot_backend/      # Django project settings
│   ├── requirements.txt         # Python dependencies
│   └── manage.py               # Django management
├── 📂 chatbot-frontend/         # React frontend
│   ├── 📂 src/                  # Source code
│   │   ├── 📂 components/       # React components
│   │   ├── ChatInterface.js     # Main chat component
│   │   ├── theme.js            # Material-UI theme
│   │   └── App.js              # Root component
│   ├── 📂 public/              # Static assets
│   └── package.json            # Node dependencies
├── 📂 docs/                    # Documentation
├── render.yaml                 # Render deployment config
├── netlify.toml               # Netlify deployment config
└── README.md                  # This file
```

## 🎯 Features Deep Dive

### 🤖 Intelligent Chat System
- **Pattern Recognition**: Advanced text matching for accurate intent detection
- **Context Awareness**: Maintains conversation context for better responses
- **Quick Actions**: Pre-defined buttons for common tourist queries
- **Multi-turn Conversations**: Supports follow-up questions and clarifications

### 🎨 Modern UI/UX
- **Glass Morphism**: Trendy translucent design with backdrop blur effects
- **Smooth Animations**: Framer Motion powered transitions and micro-interactions
- **Responsive Design**: Seamless experience across all device sizes
- **Dark/Light Themes**: Automatic theme switching based on user preference

### ⚡ Performance Optimizations
- **Response Caching**: Intelligent caching system for faster responses
- **Lazy Loading**: Components and images load on demand
- **Code Splitting**: Optimized bundle sizes for faster initial load
- **CDN Integration**: Static assets served from global CDN

## 🌍 Deployment

### Free Hosting Options

#### Option 1: Render + Netlify (Recommended)
- **Backend**: Deploy to [Render](https://render.com) (750 hours/month free)
- **Frontend**: Deploy to [Netlify](https://netlify.com) (100GB bandwidth/month free)

#### Option 2: Railway + Vercel
- **Backend**: Deploy to [Railway](https://railway.app) ($5 credit/month)
- **Frontend**: Deploy to [Vercel](https://vercel.com) (unlimited static sites)

### Environment Variables

#### Backend (.env)
```bash
DEBUG=false
DJANGO_SETTINGS_MODULE=chatbot_backend.settings
```

#### Frontend (.env)
```bash
REACT_APP_API_URL=https://your-backend-url.com
```

## *Park Information**: Comprehensive details about Bale Mountains National Park
- **Travel Directions**: Three detailed routes with distances and travel times
-## Adding New ons**:s
1. Edit `chatbot_backend/chatapi/utils/baale_mountain.json`
2. Add new intent with patterns and responses
3. Test with the chat interface

### Customizing UI
1. Modify theme in `chatbot-frontend/src/theme.js`
2. Update components in `chatbot-frontend/src/components/`
3. Add new animations in component files

### API Endpoints
- `GET /api/chat/` - API documentatiin
- `POST /api/chat/` - Process chat messages
- `GET /api/performance/` - Performance metrics
- `GET /api/weather/` - Weather information

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSEfile for details.

## 🙏 Acknowledgments

- **Bale Mountains National Park** - For the inspiration and natural beauty
- **Ethiopian Tourism** - For promoting sustainable tourism
- **Open Source Community** - For the amazing tools and libraries

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/ajme-abes/Baale-Mountain-Tour-chatBot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ajme-abes/Baale-Mountain-Tour-chatBot/discussions)
- **Email**: [Contact Us](mailto:demuxml@gmial.com.com)

---

**Made with ❤️ for Ethiopian Tourism and Nature Conservation**