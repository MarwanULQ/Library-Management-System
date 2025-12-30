#!/usr/bin/env bash

# Stop script if any command fails
set -e

echo "🚀 Starting Library Management System..."

# Activate virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "❌ Virtual environment not found. Please create it first."
    exit 1
fi

# Start backend (FastAPI)
echo "🔧 Starting backend (FastAPI)..."
uvicorn src.library_management.main:app --reload &

# Give backend time to start
sleep 2

# Start frontend (Streamlit)
echo "🎨 Starting frontend (Streamlit)..."
streamlit run src/library_management/ui/app.py

# Wait for background processes
wait
