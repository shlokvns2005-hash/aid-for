# Quick Start Guide

## One-Minute Setup

### Windows
```bash
# 1. Install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

### Linux/macOS
```bash
# 1. Install Tesseract
sudo apt-get install tesseract-ocr  # Linux
brew install tesseract              # macOS

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

## Features Overview

### 📤 Upload & Extract
- Upload PDF or image files
- Paste text directly
- Automatic text extraction using OCR

### ✏️ Simplify
- Choose T5-small (faster) or BART (better quality)
- Automatic Flesch-Kincaid analysis
- Side-by-side text comparison

### 🔊 Listen
- Adjustable speech rate (50-300 WPM)
- Volume control
- Male/Female voice options
- Save audio to MP3

### 📊 Analysis
- Reading level metrics
- Complexity assessment
- Improvement tracking

## File Formats

**Input:**
- PDF (.pdf)
- Images (.jpg, .jpeg, .png, .bmp, .tiff)
- Plain text (paste in app)

**Output:**
- Simplified text (.txt)
- Audio file (.mp3)

## Models

- **OCR**: Tesseract (free, open-source)
- **T5-small**: 60M parameters, lightweight
- **BART**: Facebook's transformer, better quality
- **TTS**: pyttsx3 (offline, no API key needed)

## Keyboard Shortcuts (in Streamlit)

- `R` - Rerun
- `C` - Clear cache
- `Shift + P` - Print to console

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "Tesseract not found" | Install Tesseract, add to PATH |
| Slow processing | Use smaller PDFs, use T5-small model |
| Audio not working | Install espeak (Linux) or check Windows sound |
| Memory issues | Restart Streamlit, close other apps |

## Performance Tips

1. **For OCR**: Use clear, high-contrast images
2. **For Simplification**: Start with small text chunks
3. **For TTS**: Pre-process long texts into paragraphs
4. **General**: Close other applications to free up RAM

## Example Usage

```
Input: Complex academic paper PDF
   ↓
Extract: 5000 words of dense academic text
   ↓
Simplify: Using T5 → 3000 words of simple English
   ↓
Listen: 5-10 minute audio file
   ↓
Output: Easy-to-read text + MP3 file
```

## Getting Help

1. Check SETUP.md for detailed installation
2. Run `python test_app.py` for module testing
3. Check app console for error messages
4. Ensure all dependencies are installed: `pip list`

## Next Steps

After setup:
1. Test with sample PDF or image
2. Try both T5-small and BART models
3. Adjust speech rate to your preference
4. Explore analysis tab for reading levels

---

**Ready to help dyslexic readers!** 📖✨
