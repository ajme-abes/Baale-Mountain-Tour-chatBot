# 🤝 Contributing to Bale Mountains Explorer

Thank you for your interest in contributing to the Bale Mountains Explorer project! This document provides guidelines and information for contributors.

## 🌟 Ways to Contribute

- 🐛 **Bug Reports** - Help us identify and fix issues
- 💡 **Feature Requests** - Suggest new features and improvements
- 📝 **Documentation** - Improve docs, tutorials, and examples
- 🔧 **Code Contributions** - Submit bug fixes and new features
- 🎨 **Design** - UI/UX improvements and design suggestions
- 🌍 **Translations** - Help make the app multilingual
- 🧪 **Testing** - Write tests and improve test coverage

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Git
- Basic knowledge of Django and React

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/ajme-abes/Baale-Mountain-Tour-chatBot.git
   cd bale-mountains-explorer
   ```

2. **Backend Setup**
   ```bash
   cd chatbot_backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python -m spacy download en_core_web_lg
   python start_server.py
   ```

3. **Frontend Setup**
   ```bash
   cd chatbot-frontend
   npm install
   npm start
   ```

## 📋 Development Guidelines

### 🐍 Python/Django Code Standards

- **Style**: Follow PEP 8
- **Formatting**: Use Black (`black .`)
- **Imports**: Use isort (`isort .`)
- **Type Hints**: Add type hints for new functions
- **Docstrings**: Use Google-style docstrings

```python
def process_message(message: str, confidence_threshold: float = 0.7) -> Dict[str, Any]:
    """Process a user message and return a response.
    
    Args:
        message: The user's input message
        confidence_threshold: Minimum confidence for intent classification
        
    Returns:
        Dictionary containing response parts, confidence, and intent
        
    Raises:
        ValueError: If message is empty or invalid
    """
    pass
```

### ⚛️ React/JavaScript Code Standards

- **Style**: ESLint + Prettier configuration
- **Components**: Use functional components with hooks
- **Props**: Use TypeScript-style prop validation
- **Naming**: PascalCase for components, camelCase for functions

```javascript
const MessageBubble = ({ message, index }) => {
  const [isVisible, setIsVisible] = useState(false);
  
  useEffect(() => {
    // Component logic
  }, [message]);
  
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      {/* Component JSX */}
    </motion.div>
  );
};
```

### 🎨 UI/UX Guidelines

- **Design System**: Follow Material-UI theme
- **Accessibility**: WCAG AA compliance
- **Responsive**: Mobile-first approach
- **Performance**: Optimize images and animations
- **Consistency**: Use existing components when possible

## 🔄 Contribution Workflow

### 1. Create an Issue
Before starting work, create an issue to discuss:
- Bug reports with reproduction steps
- Feature requests with use cases
- Questions about implementation

### 2. Branch Naming
Use descriptive branch names:
```bash
feature/add-voice-integration
bugfix/fix-mobile-navigation
docs/update-api-documentation
refactor/optimize-chat-processor
```

### 3. Commit Messages
Follow conventional commit format:
```bash
feat: add voice input support
fix: resolve mobile navigation issue
docs: update API documentation
refactor: optimize chat processor performance
test: add unit tests for message handling
```

### 4. Pull Request Process

1. **Create PR** with descriptive title and description
2. **Link Issues** using "Closes #123" or "Fixes #456"
3. **Add Screenshots** for UI changes
4. **Update Documentation** if needed
5. **Ensure Tests Pass** and add new tests
6. **Request Review** from maintainers

#### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Refactoring

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🧪 Testing Guidelines

### Backend Testing
```bash
# Run API tests
python test_api.py

# Run Django tests
python manage.py test

# Check code coverage
coverage n --source='.' manage.py test
coverage report
```

### Frontend Tes``bash
# Run unit tests
npm test

# Run with coverage
npm test -- --coverage

# Run end-to-end tests
npm run test:e2e
```

### Test s
- **Unit Tests**: For new functions and components
- **Integration Tests**: For API endpoints
- **Manual Testing**: For UI changes
- **Performance Tests**: For optimization changes

## 📝 Documentation Standards

### Code Documentation
- **Inline Comments**: Explain complex logic
- **Function Docs**: Document parameters and return values
- **API Docs**: Update OpenAPI specifications
- **README Updates**: Keep installation and usage current

### Writing Style
- **Clear and Concise**: Easy to understandxamples**: Include comples
- **Screenshots**: Visual aids for UI features
- **Links**: Reference related documentation

## 🐛 Bug Report Guidelines

### Required Information
- **Environment**: OS, Python/Node versions, browser
- **Steps to Reproduce**: Detailed reproduction steps
- **Expected Behavior**:  happen
- **Actual Behavior**: What actually happens
- **Screenshots**: Visual evidenable
- **Logs**: Relevant error messages or logs

### Bug Report Template
```markdown
**Environment:**
- OS: Windows 11
- Python: 3.12.0
- Node: 18.17.0
- Browser: Chrome 120.0

**Steps to Reproduce:**
1. Go to chat interface
2. Click on "Park Information"
3. Observe the error

**Expected Behavior:**
Should display park information

**Actual Behavior:**
Shows "Could you please rephrase that?"
hots:**
[Attots]

**l Context:**
Any other relevant information
```

## 💡 Feature Request Guidelines

### Required Information
- **Problem Statement**: What problem does this solve?
- **Proposed Solution**: How should it work?
- **Alternatives**: Other solutions considered
- **Use Cases**: Who would use this feature?
- **Priority**: How important is this feature?

## 🎯 Areas for Contribution

### 🔥 High Priority
- Performance optimizations
- Mobile experience improvements
- Accessibility enhancements
- Test coverage improvements
- Documentation updates

### 🚀 New Features
- Voice integration
- Real-time weather data
- Booking system integration
- User account system
- Offline mode support

### 🐛 Known Issues
Check our [Issues](https://github.com/ajme-abes/Baale-Mountain-Tour-chatBot/issues) page for current bugs and feature requests.

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** - Contributors section
- **CHANGELOG.md** - Release notes
- **GitHub** - Contributor graphs and statistics
- **Social Media** - Feature announcements

## 📞 Getting Help

- **GitHub Discussions**: For questions and ideas
- **Issues**: For bugs and feature requests
- **Email**: ajmelabes@gmaail.com


## 📄 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Bale Mountains Explorer! 🏔️**