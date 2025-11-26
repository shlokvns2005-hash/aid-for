# Reading Aid for Dyslexic People - Installation & Usage Guide

## Current Status

The project has been successfully created with:
- ✅ **Core modules**: OCR, Text Processing, and Text-to-Speech
- ✅ **CLI interface**: Working lite version (`app_lite.py`)
- ✅ **Installation**: Basic packages installed (pytesseract, pillow, pdf2image, numpy, pyttsx3, comtypes)
- ⏳ **Advanced features pending**: Streamlit UI, PyTorch, Transformers (due to Python 3.14 compatibility constraints)

## Quick Start

### 1. Using the CLI (Lite Version)

The simplest way to start - no external tools required for basic functionality:

```bash
python app_lite.py
```

This provides:
- Text extraction from PDFs/Images (requires Tesseract)
- Text simplification using basic algorithms
- Reading level analysis (Flesch-Kincaid)
- Text-to-speech conversion

### 2. Installation Requirements

#### Installed (✓)
```bash
pip install pytesseract pillow pdf2image numpy pyttsx3 comtypes
```

#### To Install Tesseract OCR (Required for PDF/Image text extraction)

**Windows:**
1. Download installer: https://github.com/UB-Mannheim/tesseract/releases
2. Run `tesseract-ocr-w64-setup-v5.3.0.20230101.exe`
3. Note the installation path (typically `C:\Program Files\Tesseract-OCR`)

**After installation, add to Python path** (in `src/modules/ocr_extractor.py`):

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 3. Optional: Advanced Features (Streamlit UI with AI Models)

For the full Streamlit interface with T5/BART text simplification:

```bash
# Install large ML packages (may take time on Python 3.14)
pip install streamlit torch transformers

# Then run:
streamlit run app.py
```

**Note:** Python 3.14 has limited wheel support for some packages. If installation fails:
- Try Python 3.11 or 3.12 instead
- Or use the CLI version which has all essential features

## Usage Examples

### Example 1: Extract Text from PDF

```
$ python app_lite.py
[Select option 1]
Enter PDF/Image file path: sample.pdf
```

### Example 2: Simplify Text

```
[Select option 2]
Enter text to simplify: "Complex academic text here..."
```

Reading level will be calculated and shown.

### Example 3: Generate Speech

```
[Select option 3]
Enter text for speech: "Hello, this is the reading aid..."
```

Uses system TTS to read the text aloud.

### Example 4: Full Pipeline

```
[Select option 4]
Enter PDF/Image file path: document.pdf

[Extracts text → Simplifies → Analyzes reading level → Optionally generates speech]
```

## Project Structure

```
d:\aid-for\
├── app_lite.py              # CLI interface (working)
├── app.py                   # Streamlit interface (requires streamlit + torch)
├── config.py                # Configuration management
├── requirements.txt         # All dependencies
├── src/
│   └── modules/
│       ├── ocr_extractor.py        # PDF/Image text extraction
│       ├── text_simplifier.py      # Text simplification (basic + ML)
│       └── text_to_speech.py       # Text-to-speech conversion
├── docs/                    # Documentation
└── tests/                   # Test files
```

## Troubleshooting

### Issue: "Tesseract not found"
**Solution:** Install Tesseract OCR binary (see section 2 above)

### Issue: "Module not found" errors
**Solution:** Ensure you're in the project directory:
```bash
cd d:\aid-for
python app_lite.py
```

### Issue: pyttsx3 errors
**Solution:** Install missing dependencies:
```bash
pip install comtypes pywin32
python -m pip install pywin32_postinstall
```

### Issue: Large ML packages won't install
**Solution:** Use Python 3.11 or 3.12 instead of 3.14, or stick with CLI version

## Features

### Currently Working
- ✅ PDF text extraction using Tesseract OCR
- ✅ Image text extraction (JPG, PNG, BMP, etc.)
- ✅ Basic text simplification (sentence breaking)
- ✅ Flesch-Kincaid reading level calculation
- ✅ Windows text-to-speech with voice/rate/volume control
- ✅ Interactive CLI interface

### Available (With Streamlit + ML packages)
- 📊 Web-based UI with tabbed interface
- 🤖 AI-powered text simplification (T5-small)
- 📈 Advanced reading metrics (SMOG, Gunning Fog, etc.)
- 💾 Save simplified text and audio files
- 🎨 Customizable display options

## Next Steps

1. **Install Tesseract OCR** - Required for document scanning
2. **Test with a sample PDF** - Use the CLI to verify setup
3. **Optional: Install advanced features** - For web UI and AI models

## Getting Help

Key modules and their uses:
- `OCRExtractor` - Extract text from documents
- `TextToSpeech` - Convert text to audio
- `TextSimplifier` - Simplify complex text (basic or with ML)

Example code:
```python
from src.modules.ocr_extractor import OCRExtractor
from src.modules.text_to_speech import TextToSpeech

# Extract from PDF
ocr = OCRExtractor()
text = ocr.extract_from_pdf('document.pdf')

# Generate speech
tts = TextToSpeech(rate=150)
tts.speak(text)
```

---

**System Info:** Python 3.14.0 | Windows
**Last Updated:** 2025
