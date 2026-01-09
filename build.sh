#!/bin/bash
# Simple build script for Render deployment

echo "🚀 Starting Bale Mountains Chatbot build..."

cd chatbot_backend

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Build complete - ready for deployment!"