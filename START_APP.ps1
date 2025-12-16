# Quick Start Script for Reading Aid Application
# This script activates the environment and runs the app

param(
    [switch]$SkipTesseract,
    [switch]$Help
)

if ($Help) {
    Write-Host "Usage: .\START_APP.ps1 [options]" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Options:" -ForegroundColor Yellow
    Write-Host "  -SkipTesseract    Skip Tesseract check (run without OCR)" -ForegroundColor White
    Write-Host "  -Help             Show this help message" -ForegroundColor White
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\START_APP.ps1                  # Normal start with all checks" -ForegroundColor White
    Write-Host "  .\START_APP.ps1 -SkipTesseract   # Start without Tesseract" -ForegroundColor White
    exit 0
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 Reading Aid for Dyslexic People" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".\env\Scripts\activate.ps1")) {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv env
    Write-Host "✅ Virtual environment created!" -ForegroundColor Green
}

# Check Tesseract (unless skipped)
if (-not $SkipTesseract) {
    Write-Host "Checking Tesseract OCR..." -ForegroundColor Yellow
    try {
        $tesseractVersion = tesseract --version 2>&1
        Write-Host "✅ Tesseract is installed" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️ Tesseract is not installed or not in PATH" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Options:" -ForegroundColor Cyan
        Write-Host "1. Install Tesseract now (opens download page)" -ForegroundColor White
        Write-Host "2. Continue without Tesseract (text paste only)" -ForegroundColor White
        Write-Host "3. Exit" -ForegroundColor White
        Write-Host ""
        $choice = Read-Host "Select option (1-3)"
        
        switch ($choice) {
            "1" {
                Write-Host "Opening Tesseract download page..." -ForegroundColor Green
                Start-Process "https://github.com/UB-Mannheim/tesseract/wiki"
                Write-Host ""
                Write-Host "Please install Tesseract and run this script again." -ForegroundColor Yellow
                exit 0
            }
            "2" {
                Write-Host "⚠️ Continuing without Tesseract. PDF/Image upload will not work." -ForegroundColor Yellow
            }
            "3" {
                Write-Host "Exiting..." -ForegroundColor Red
                exit 0
            }
            default {
                Write-Host "Invalid option. Exiting." -ForegroundColor Red
                exit 1
            }
        }
    }
}

Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\env\Scripts\Activate.ps1

Write-Host "✅ Virtual environment activated" -ForegroundColor Green
Write-Host ""

# Check if dependencies are installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$streamlitInstalled = python -c "import streamlit" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ Dependencies not installed. Installing..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed!" -ForegroundColor Green
}
else {
    Write-Host "✅ Dependencies are installed" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Streamlit App..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📖 App will open at: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Tips:" -ForegroundColor Yellow
Write-Host "  - Use Paste Text tab if Tesseract is not installed" -ForegroundColor White
Write-Host "  - First run may take 1-3 minutes to download AI models" -ForegroundColor White
Write-Host "  - Press Ctrl+C to stop the server" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Run the app
streamlit run app.py
