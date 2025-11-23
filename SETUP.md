# Setup Guide - Reading Aid for Dyslexic People

## Installation Steps

### 1. Install Tesseract OCR

**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer (default: C:\Program Files\Tesseract-OCR)
3. Add to PATH or update path in code

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/macOS)
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Pre-download Models

```bash
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('t5-small')"
python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('facebook/bart-base')"
```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open at: http://localhost:8501

## Configuration (Optional)

Edit `app.py` to change default settings:
- Speech rate (default: 150 WPM)
- Volume (default: 1.0)
- Default model (default: T5-small)

## Troubleshooting

### Tesseract Not Found
```python
# Add this to app.py if needed
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Models Not Downloading
- Check internet connection
- Models cache to ~/.cache/huggingface/
- First run may take 5-10 minutes

### Audio Not Working
- Linux: `sudo apt-get install espeak`
- Check volume settings
- Try different voice option

## Usage Workflow

1. **Upload/Input**: Select PDF, image, or paste text
2. **Extract**: OCR converts to text
3. **Simplify**: AI simplifies the text (T5 or BART)
4. **Listen**: TTS converts to speech
5. **Download**: Save text or audio

## Performance Tips

- Use high-quality images for OCR
- Keep PDFs under 50 pages for faster processing
- Use T5-small for faster simplification
- Enable speech caching for repeated text
