# Project Structure Summary

## 📦 Complete File Listing

### Core Application Files
- **app.py** - Main Streamlit application with complete UI
- **config.py** - Advanced configuration (developer settings)
- **config.json** - Project metadata and structure

### Python Modules (src/modules/)
- **ocr_extractor.py** - OCR/text extraction (Tesseract)
- **text_simplifier.py** - AI text simplification (T5/BART)
- **text_to_speech.py** - Text-to-speech conversion (pyttsx3)

### Documentation
- **README.md** - Project overview
- **SETUP.md** - Installation and troubleshooting
- **QUICKSTART.md** - One-minute quick start
- **ARCHITECTURE.md** - Technical architecture
- **STRUCTURE.md** - This file

### Testing & Examples
- **test_app.py** - Unit tests for modules
- **examples.py** - Example usage patterns

### Configuration
- **.streamlit/config.toml** - Streamlit theme config
- **.gitignore** - Git ignore file

### Dependencies
- **requirements.txt** - Python package dependencies

### Directories
- **uploads/** - Temporary file uploads
- **output/** - Generated output files
- **logs/** - Application logs (created on first run)

---

## 🎯 What Each Component Does

### Input Pipeline
```
User Input (PDF/Image/Text)
    ↓
1. OCR Extraction (ocr_extractor.py)
   - Extracts text from images using Tesseract
   - Converts PDFs to images then extracts text
    ↓
2. Text Simplification (text_simplifier.py)
   - Uses T5-small or BART to simplify text
   - Calculates Flesch-Kincaid reading level
    ↓
3. Analysis Module
   - Compares original vs simplified
   - Shows improvement metrics
    ↓
4. Text-to-Speech (text_to_speech.py)
   - Converts text to audio using pyttsx3
   - Supports voice selection and rate control
    ↓
Output (Simple Text + Audio)
```

---

## 📋 Quick Reference

| File | Purpose | Language |
|------|---------|----------|
| app.py | Main application | Python + Streamlit |
| ocr_extractor.py | OCR module | Python |
| text_simplifier.py | AI simplification | Python (Transformers) |
| text_to_speech.py | TTS module | Python |
| config.py | Settings & config | Python |
| test_app.py | Testing suite | Python |
| examples.py | Usage examples | Python |

---

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Tesseract**
   - Windows: Download installer
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

3. **Run Application**
   ```bash
   streamlit run app.py
   ```

4. **Test Installation**
   ```bash
   python test_app.py
   ```

---

## 💡 Key Features

✅ **OCR**: Extract text from PDFs and images
✅ **Simplification**: T5-small and BART models
✅ **Analysis**: Flesch-Kincaid reading levels
✅ **TTS**: Multiple voice options
✅ **Download**: Save text and audio files
✅ **Responsive**: Mobile-friendly UI
✅ **Offline**: No API keys required

---

## 🔧 Customization

### Change Default Model
Edit line in **app.py**:
```python
model_map = {"T5-small": "t5", "BART": "bart"}
```

### Adjust Speech Settings
Edit **config.py** `TTS_CONFIG`:
```python
"default_rate": 150,  # Words per minute
"default_volume": 1.0,  # 0.0-1.0
```

### Configure Tesseract Path (Windows)
In **ocr_extractor.py**:
```python
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📚 File Dependencies

```
app.py
├── src/modules/ocr_extractor.py
├── src/modules/text_simplifier.py
├── src/modules/text_to_speech.py
└── Streamlit library

test_app.py
└── src/modules/text_simplifier.py

examples.py
├── src/modules/ocr_extractor.py
├── src/modules/text_simplifier.py
├── src/modules/text_to_speech.py
└── config.py
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Add to Python path in app.py: `sys.path.insert(0, 'src')` |
| Tesseract error | Install Tesseract, update path in ocr_extractor.py |
| Memory error | Reduce chunk_size in config.py or close other apps |
| Model download fails | Check internet, models cached after first run |

---

## 📊 Architecture Overview

```
┌─────────────────────────────────┐
│   Streamlit Web Interface       │
│  (app.py - 4 Tabs)              │
└────────────┬────────────────────┘
             │
        ┌────┴─────┬────────────────┬────────────┐
        │           │                │            │
        ▼           ▼                ▼            ▼
   ┌────────┐  ┌─────────┐  ┌──────────┐  ┌──────┐
   │  OCR   │  │ Simplif │  │ Analysis │  │ TTS  │
   │Module  │  │  Module │  │ Module   │  │Module│
   └────────┘  └─────────┘  └──────────┘  └──────┘
        │           │                │            │
   Tesseract   T5/BART         FK Level       pyttsx3
```

---

## 📱 User Workflow

1. **Upload** - Choose PDF, image, or paste text
2. **Extract** - OCR converts to text
3. **Simplify** - AI makes text easier to read
4. **Listen** - TTS creates audio version
5. **Download** - Save text and/or audio
6. **Analyze** - View reading level improvements

---

## 🎓 Learning Resources

- **Tesseract**: https://github.com/UB-Mannheim/tesseract/wiki
- **T5**: https://huggingface.co/docs/transformers/model_doc/t5
- **BART**: https://huggingface.co/docs/transformers/model_doc/bart
- **Streamlit**: https://docs.streamlit.io
- **pyttsx3**: https://pyttsx3.readthedocs.io

---

## 📈 Performance Metrics

- **OCR Speed**: 1-5 min/page (depends on quality)
- **Simplification**: 10-30 sec/1000 words
- **TTS Speed**: Real-time or faster
- **Memory**: ~4GB for model loading
- **Startup**: ~30-60 seconds (first run)

---

## 🔐 Security & Privacy

✅ No cloud uploads - all processing local
✅ No data storage between sessions
✅ No API keys required
✅ No user account needed
✅ Temporary files auto-deleted

---

Generated: 2024-11-24
Project: Reading Aid for Dyslexic People
Version: 1.0.0
