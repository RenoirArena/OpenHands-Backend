---
title: Personal OpenHands Backend
emoji: 💕
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
---

# 💕 Personal OpenHands Backend

A powerful AI agent backend made for you and your girlfriend! OpenRouter-only, no Google Cloud, simple authentication, and optimized for Hugging Face Spaces.

## 🚀 Quick Start

This Space provides a personal AI assistant backend for you and your girlfriend only! Simple authentication protects your privacy.

### 🔐 Authentication Required

Most endpoints require a Bearer token. Set `PERSONAL_ACCESS_TOKEN` in your HF Spaces environment variables.

### API Endpoints

```bash
# Health check (public)
GET /health

# Personal info (protected)
GET /personal-info
Authorization: Bearer your_personal_token

# OpenHands API endpoints (protected)
GET /api/options/config
Authorization: Bearer your_personal_token

# Create conversation (protected)
POST /api/conversations
Authorization: Bearer your_personal_token
Content-Type: application/json
{
  "initial_user_msg": "Hello! Can you help me with coding?"
}
```

### Example Usage

```javascript
// Create a new conversation with authentication
const response = await fetch('https://your-space.hf.space/api/conversations', {
  method: 'POST',
  headers: { 
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_personal_token'
  },
  body: JSON.stringify({
    initial_user_msg: 'Write a Python function to calculate fibonacci numbers'
  })
});

const conversation = await response.json();
console.log(conversation);
```

## ⚙️ Required Configuration

Set these environment variables in your HF Spaces settings:

```bash
# Required - Your OpenRouter API key
LLM_API_KEY=your_openrouter_api_key

# Required - Personal access token for authentication
PERSONAL_ACCESS_TOKEN=your_secret_token_here

# Optional - LLM configuration (defaults provided)
LLM_MODEL=openrouter/anthropic/claude-3-haiku-20240307
LLM_BASE_URL=https://openrouter.ai/api/v1
```

## 🌐 Frontend Integration

This backend works perfectly with frontends deployed on:
- **Vercel** (*.vercel.app)
- **Netlify** (*.netlify.app) 
- **GitHub Pages** (*.github.io)
- **Local development** (localhost)

CORS is pre-configured to allow these domains.

## 🔧 Features

- 🔐 **Personal Authentication** - Only you and your girlfriend can access
- ✅ **OpenRouter Only** - No need for multiple API keys
- ✅ **Local Runtime** - Works without Docker in container
- ✅ **CORS Enabled** - Ready for frontend integration
- ✅ **No Google Cloud** - Zero Google dependencies
- ✅ **HF Spaces Optimized** - Perfect for Hugging Face deployment
- ✅ **Indonesian Novel Writing** - Special support for creative writing
- ✅ **All-in-One File** - Single app.py file, no confusion

## 📚 Documentation

- **OpenHands GitHub**: [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)
- **LLM Provider**: [OpenRouter](https://openrouter.ai)
- **Frontend Examples**: Deploy your own UI on Vercel

## 🎯 Use Cases

- **AI Coding Assistant**: Help with programming tasks
- **Web Automation**: Browse and interact with websites  
- **Code Execution**: Run and test code snippets
- **Research Assistant**: Gather information from multiple sources
- **Educational Tools**: Interactive learning experiences
- **Novel Writing**: Indonesian creative writing support

## 📝 License

MIT License - Feel free to use in your projects!

---

**Ready to build AI-powered applications?** 🚀 

Start by calling the API endpoints above or integrate with your frontend!