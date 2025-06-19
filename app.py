#!/usr/bin/env python3
"""
🎯 Personal OpenHands Backend - ALL-IN-ONE VERSION
💕 Made for you and your girlfriend - NO Google Cloud needed!

This is the ONLY file you need:
❌ NO Google Cloud Storage
❌ NO Docker complexity
❌ NO Multiple files confusion
✅ Pure OpenHands AI agents
✅ OpenRouter ONLY
✅ Simple authentication
✅ HF Spaces optimized
✅ Everything in ONE file
"""

import os
import sys
import logging
import traceback
import uvicorn
from pathlib import Path
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Simple authentication for personal use
security = HTTPBearer()

def verify_personal_access(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Simple authentication for personal use - you and your girlfriend only"""
    # Get the personal access token from environment
    personal_token = os.getenv("PERSONAL_ACCESS_TOKEN", "your-secret-token-here")
    
    if credentials.credentials != personal_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid personal access token. Only you and your girlfriend can access this!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials

def setup_personal_environment():
    """Setup environment for OpenRouter-only personal use."""
    logger.info("🎯 Setting up Personal OpenHands Backend for OpenRouter...")
    
    # Core HF Spaces configuration
    os.environ.setdefault("PORT", "7860")
    os.environ.setdefault("HOST", "0.0.0.0")
    os.environ.setdefault("OPENHANDS_RUNTIME", "local")  # Use local runtime, not docker
    os.environ.setdefault("CORS_ALLOWED_ORIGINS", "*")
    
    # Essential environment variables for personal use
    os.environ.setdefault('OPENHANDS_DISABLE_AUTH', 'true')
    os.environ.setdefault('DISABLE_SECURITY', 'true')
    os.environ.setdefault('WORKSPACE_BASE', '/tmp/workspace')
    os.environ.setdefault('RUNTIME', 'local')  # Use local runtime, no Docker
    os.environ.setdefault('SANDBOX_TYPE', 'local')
    os.environ.setdefault('FILE_STORE', 'local')  # Local file storage, no Google Cloud
    os.environ.setdefault('FILE_STORE_PATH', '/tmp/openhands_storage')
    
    # Use memory-based storage to avoid file permission issues
    os.environ["SETTINGS_STORE_TYPE"] = "memory"
    os.environ["SECRETS_STORE_TYPE"] = "memory"
    os.environ["CONVERSATION_STORE_TYPE"] = "memory"
    os.environ["SESSION_STORE_TYPE"] = "memory"
    
    # Disable file-based features that might cause issues
    os.environ["DISABLE_FILE_LOGGING"] = "true"
    os.environ["DISABLE_PERSISTENT_SESSIONS"] = "true"
    os.environ["SERVE_FRONTEND"] = "false"
    os.environ["SECURITY_CONFIRMATION_MODE"] = "false"
    
    # Set reasonable defaults for personal usage
    os.environ.setdefault("MAX_ITERATIONS", "30")
    os.environ.setdefault("DEFAULT_AGENT", "CodeActAgent")
    
    # OpenRouter-specific configuration
    os.environ.setdefault('LLM_BASE_URL', 'https://openrouter.ai/api/v1')
    os.environ.setdefault('LLM_MODEL', 'openrouter/anthropic/claude-3-haiku-20240307')
    
    # Set OpenRouter API key from environment (user will set this in HF Spaces)
    if not os.environ.get('LLM_API_KEY'):
        logger.warning("⚠️  LLM_API_KEY not set! Please set your OpenRouter API key in HF Spaces environment variables.")
        logger.info("💡 Go to HF Spaces Settings → Environment Variables → Add:")
        logger.info("💡 LLM_API_KEY = your_openrouter_api_key")
        logger.info("💡 PERSONAL_ACCESS_TOKEN = your_secret_token")
    else:
        logger.info("✅ OpenRouter API key found!")
    
    # Create necessary directories
    directories = ["/tmp/openhands", "/tmp/cache", "/tmp/workspace", "/tmp/file_store", "/tmp/openhands_storage"]
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    logger.info("✅ Personal environment configured for OpenRouter!")

def check_personal_dependencies():
    """Check only essential dependencies for personal use."""
    logger.info("🔍 Checking personal dependencies...")
    missing_deps = []
    
    try:
        import fastapi
        logger.info("✅ FastAPI available")
    except ImportError:
        missing_deps.append("fastapi")
    
    try:
        import uvicorn
        logger.info("✅ Uvicorn available")
    except ImportError:
        missing_deps.append("uvicorn")
    
    try:
        import litellm
        logger.info("✅ LiteLLM available")
    except ImportError:
        missing_deps.append("litellm")
    
    # Check optional dependencies
    try:
        import docker
        logger.info("⚠️  Docker available (not needed for personal use)")
    except ImportError:
        logger.info("✅ Docker not available (perfect for personal use)")
    
    try:
        import google.cloud
        logger.info("⚠️  Google Cloud available (not needed for personal use)")
    except ImportError:
        logger.info("✅ Google Cloud not available (perfect for personal use)")
    
    if missing_deps:
        logger.error(f"❌ Missing essential dependencies: {missing_deps}")
        return False
    
    return True

def main():
    """Main entry point for personal OpenHands backend."""
    print("=" * 60)
    print("🎯 Personal OpenHands Backend Starting...")
    print("💕 Made for you and your girlfriend!")
    print("🚀 No Google Cloud, No Docker, No Complexity!")
    print("🔐 Simple authentication for privacy!")
    print("=" * 60)
    
    try:
        # Setup personal environment
        setup_personal_environment()
        
        # Check dependencies
        if not check_personal_dependencies():
            logger.error("❌ Missing essential dependencies")
            sys.exit(1)
        
        logger.info("📦 Importing OpenHands app...")
        
        # Import OpenHands app
        from openhands.server.app import app
        
        logger.info("✅ OpenHands app imported successfully!")
        logger.info("🎉 Personal backend ready!")
        
        # Add CORS for your frontend
        from fastapi.middleware.cors import CORSMiddleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allow all origins for personal use
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Add health check (public endpoint)
        @app.get("/health")
        async def health_check():
            return {
                "status": "healthy",
                "message": "Personal OpenHands Backend is running!",
                "features": [
                    "AI Agents (CodeActAgent, BrowsingAgent, etc.)",
                    "Novel Writing (Indonesian)",
                    "File Operations",
                    "No Google Cloud needed",
                    "No Docker needed"
                ],
                "auth_required": "Bearer token required for protected endpoints",
                "setup_instructions": {
                    "step1": "Set LLM_API_KEY in HF Spaces environment variables",
                    "step2": "Set PERSONAL_ACCESS_TOKEN for authentication",
                    "step3": "Use Bearer token in Authorization header"
                }
            }
        
        # Add personal info endpoint (protected)
        @app.get("/personal-info")
        async def personal_info(token: str = Depends(verify_personal_access)):
            return {
                "title": "Personal OpenHands Backend",
                "description": "Made for you and your girlfriend 💕",
                "setup": "OpenRouter-only configuration",
                "features": {
                    "ai_agents": [
                        "CodeActAgent - Complete coding assistant",
                        "BrowsingAgent - Web research",
                        "ReadOnlyAgent - Safe code review",
                        "LocAgent - Targeted code generation"
                    ],
                    "novel_writing": [
                        "Indonesian language support",
                        "7 creative templates",
                        "Character development",
                        "Plot structure",
                        "Dialogue writing"
                    ],
                    "file_operations": [
                        "view - Display files",
                        "create - Create new files", 
                        "str_replace - Edit content",
                        "insert - Add content"
                    ]
                },
                "llm_setup": {
                    "provider": "OpenRouter only",
                    "api_key_needed": "Your OpenRouter API key",
                    "models_available": "All OpenRouter models (Claude, GPT, etc.)",
                    "no_separate_keys": "No need for OpenAI or Anthropic keys"
                },
                "minimal_dependencies": [
                    "Only LiteLLM for OpenRouter",
                    "No OpenAI package",
                    "No Anthropic package", 
                    "No Google Cloud Storage",
                    "No Docker containers",
                    "No E2B sandboxes",
                    "Pure local + OpenRouter"
                ]
            }
        
        # Get configuration
        port = int(os.getenv("PORT", 7860))
        host = os.getenv("HOST", "0.0.0.0")
        
        # Startup information
        print("\n" + "="*60)
        print("🎯 Personal OpenHands Backend for HF Spaces")
        print("="*60)
        print(f"🚀 Server: {host}:{port}")
        print(f"🔑 LLM API Key: {'✅ Set' if os.getenv('LLM_API_KEY') else '❌ Missing'}")
        print(f"🔐 Personal Token: {'✅ Set' if os.getenv('PERSONAL_ACCESS_TOKEN') else '❌ Missing'}")
        print(f"🤖 LLM Model: {os.getenv('LLM_MODEL', 'Not configured')}")
        print(f"🏃 Runtime: {os.getenv('OPENHANDS_RUNTIME', 'local')}")
        print("📡 API Endpoints available at /docs")
        print("🔐 Protected endpoints require Bearer token")
        print("="*60 + "\n")
        
        logger.info("🚀 Starting Personal OpenHands Backend...")
        logger.info("💕 Perfect for your personal AI assistant!")
        
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level="info",
            access_log=True
        )
        
        return app
        
    except ImportError as e:
        logger.error(f"❌ Import error: {e}")
        logger.error("💡 This usually means a dependency is missing.")
        logger.error("💡 For personal use, check requirements_personal.txt")
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    app = main()