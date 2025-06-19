# Final optimized Dockerfile for Hugging Face Spaces
# Fixes all import issues and dependency conflicts
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create necessary directories with proper permissions
RUN mkdir -p /tmp/openhands /tmp/cache /tmp/workspace /tmp/file_store && \
    chmod -R 777 /tmp/openhands /tmp/cache /tmp/workspace /tmp/file_store

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for HF Spaces
ENV PYTHONPATH=/app
ENV OPENHANDS_RUNTIME=local
ENV PORT=7860
ENV HOST=0.0.0.0
ENV CORS_ALLOWED_ORIGINS=*
ENV FILE_STORE_PATH=/tmp/file_store
ENV CACHE_DIR=/tmp/cache
ENV WORKSPACE_BASE=/tmp/workspace

# Memory-based storage to avoid file permission issues
ENV SETTINGS_STORE_TYPE=memory
ENV SECRETS_STORE_TYPE=memory
ENV CONVERSATION_STORE_TYPE=memory
ENV FILE_STORE=memory
ENV SESSION_STORE_TYPE=memory

# Disable features that might cause issues
ENV DISABLE_SECURITY=true
ENV OPENHANDS_DISABLE_AUTH=true
ENV DISABLE_FILE_LOGGING=true
ENV DISABLE_PERSISTENT_SESSIONS=true
ENV SERVE_FRONTEND=false

# Set default LLM configuration
ENV LLM_MODEL=openrouter/anthropic/claude-3-haiku-20240307
ENV LLM_BASE_URL=https://openrouter.ai/api/v1

# Expose port (HF Spaces requires 7860)
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:7860/health || exit 1

# Run the main application
CMD ["python", "app.py"]