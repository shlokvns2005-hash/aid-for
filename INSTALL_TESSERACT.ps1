# Tesseract OCR Installation Script for Windows
# This script helps you install Tesseract OCR

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Tesseract OCR Installation Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Tesseract is already installed
$tesseractPath = "C:\Program Files\Tesseract-OCR\tesseract.exe"
if (Test-Path $tesseractPath) {
    Write-Host "✅ Tesseract is already installed at: $tesseractPath" -ForegroundColor Green
    & $tesseractPath --version
    exit 0
}

Write-Host "❌ Tesseract is not installed." -ForegroundColor Yellow
Write-Host ""
Write-Host "Installation Options:" -ForegroundColor Cyan
Write-Host "1. Download installer manually (Recommended)" -ForegroundColor White
Write-Host "2. Install using Chocolatey (if you have it)" -ForegroundColor White
Write-Host "3. Skip (run app without OCR support)" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Select option (1-3)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Opening download page in browser..." -ForegroundColor Green
        Start-Process "https://github.com/UB-Mannheim/tesseract/wiki"
        Write-Host ""
        Write-Host "📋 Instructions:" -ForegroundColor Cyan
        Write-Host "1. Download: tesseract-ocr-w64-setup-5.3.3.20231005.exe (or latest)" -ForegroundColor White
        Write-Host "2. Run the installer" -ForegroundColor White
        Write-Host "3. During installation, note the installation path" -ForegroundColor White
        Write-Host "4. Make sure to check 'Add to PATH' option" -ForegroundColor White
        Write-Host "5. After installation, restart PowerShell and run: tesseract --version" -ForegroundColor White
        Write-Host ""
        Write-Host "After installation, run the app with: streamlit run app.py" -ForegroundColor Green
    }
    "2" {
        Write-Host ""
        Write-Host "Checking for Chocolatey..." -ForegroundColor Yellow
        if (Get-Command choco -ErrorAction SilentlyContinue) {
            Write-Host "✅ Chocolatey found. Installing Tesseract..." -ForegroundColor Green
            choco install tesseract -y
            Write-Host ""
            Write-Host "✅ Installation complete!" -ForegroundColor Green
            Write-Host "Verify with: tesseract --version" -ForegroundColor Cyan
        } else {
            Write-Host "❌ Chocolatey is not installed." -ForegroundColor Red
            Write-Host "Install Chocolatey from: https://chocolatey.org/install" -ForegroundColor Yellow
            Write-Host "Or choose option 1 for manual installation." -ForegroundColor Yellow
        }
    }
    "3" {
        Write-Host ""
        Write-Host "⚠️ Running without Tesseract OCR" -ForegroundColor Yellow
        Write-Host "You can still use the app with text paste functionality." -ForegroundColor White
        Write-Host "PDF and Image upload will not work." -ForegroundColor White
        Write-Host ""
        Write-Host "To run the app: streamlit run app.py" -ForegroundColor Green
        Write-Host "Use the 'Paste Text' option in the app." -ForegroundColor Cyan
    }
    default {
        Write-Host "Invalid option. Exiting." -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Activate virtual environment: .\env\Scripts\activate" -ForegroundColor White
Write-Host "2. Run the app: streamlit run app.py" -ForegroundColor White
Write-Host "3. Open browser: http://localhost:8501" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
