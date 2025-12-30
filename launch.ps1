Write-Host "🚀 Starting Library Management System..."

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "❌ Virtual environment not found. Please create it first."
    exit 1
}

# Start backend
Write-Host "🔧 Starting backend (FastAPI)..."
Start-Process powershell -ArgumentList "uvicorn src.library_management.main:app --reload"

# Wait a bit
Start-Sleep -Seconds 2

# Start frontend
Write-Host "🎨 Starting frontend (Streamlit)..."
streamlit run src/library_management/ui/app.py
