# Project Components

## Core Application

### `app.py`
Main Streamlit application with complete user interface. Contains:
- Tab 1: Upload & Extract (PDF/Image/Text)
- Tab 2: Simplify (AI-powered text simplification)
- Tab 3: Listen (Text-to-Speech playback)
- Tab 4: Analysis (Reading level metrics)

Run with: `streamlit run app.py`

## Modules

### `src/modules/ocr_extractor.py`
Handles optical character recognition (OCR):
- `OCRExtractor` class for text extraction
- Methods: `extract_from_pdf()`, `extract_from_image()`, `extract_text()`
- Uses Tesseract OCR engine

### `src/modules/text_simplifier.py`
Simplifies complex text using AI models:
- `TextSimplifier` class supporting T5-small and BART
- Methods: `simplify_text()`, `simplify_sentences()`, `split_and_simplify()`
- Flesch-Kincaid reading level calculation

### `src/modules/text_to_speech.py`
Converts text to audio:
- `TextToSpeech` class using pyttsx3
- Methods: `speak()`, `save_to_file()`, voice/rate control
- Support for male/female voices

## Configuration & Setup

### `requirements.txt`
Python package dependencies:
- streamlit: Web UI framework
- pytesseract: OCR wrapper
- pdf2image: PDF to image conversion
- transformers: AI models (T5, BART)
- torch: PyTorch deep learning
- pyttsx3: Text-to-speech
- And other utilities

### `config.py`
Advanced configuration file (for developers):
- OCR settings
- Model parameters
- TTS configuration
- Performance tuning
- Feature flags

### `config.json`
Project metadata and structure information

### `.streamlit/config.toml`
Streamlit theme and server configuration

## Documentation

### `README.md`
Project overview and features

### `SETUP.md`
Detailed installation and troubleshooting guide

### `QUICKSTART.md`
One-minute quick start guide

### `ARCHITECTURE.md` (This file)
Component descriptions and relationships

## Testing & Development

### `test_app.py`
Testing utilities:
- `test_simplification()`: Test both models
- `test_reading_levels()`: Verify FK calculation
- Sample test cases

Run with: `python test_app.py`

## Directory Structure

```
uploads/        → Temporary uploaded files
output/         → Generated audio and output files
logs/           → Application logs
.streamlit/     → Streamlit configuration
src/modules/    → Python modules (OCR, Simplification, TTS)
```

## Data Flow

```
1. USER INPUT
   ↓
   PDF / Image / Text
   ↓
2. OCR EXTRACTION
   ↓
   Raw extracted text
   ↓
3. TEXT SIMPLIFICATION
   ↓
   AI model processes text (T5/BART)
   ↓
   Simple, readable text
   ↓
4. READING LEVEL ANALYSIS
   ↓
   Flesch-Kincaid metrics
   ↓
5. TEXT-TO-SPEECH
   ↓
   Audio generation (pyttsx3)
   ↓
6. OUTPUT
   ↓
   Simple Text + Audio File
```

## API Reference

### OCRExtractor

```python
from src.modules.ocr_extractor import OCRExtractor

ocr = OCRExtractor(tesseract_path=None)
text = ocr.extract_from_pdf("document.pdf")
text = ocr.extract_from_image("image.jpg")
text = ocr.extract_text("file.pdf")  # Auto-detect
```

### TextSimplifier

```python
from src.modules.text_simplifier import TextSimplifier

simplifier = TextSimplifier(model_type="t5")  # or "bart"
simple_text = simplifier.simplify_text(text, max_length=100)
sentences = simplifier.simplify_sentences(sentence_list)
level = simplifier.calculate_flesch_kincaid_level(text)
```

### TextToSpeech

```python
from src.modules.text_to_speech import TextToSpeech

tts = TextToSpeech(rate=150, volume=1.0, voice_id=0)
tts.speak(text)  # Play audio
tts.save_to_file(text, "output.mp3")  # Save audio
tts.set_rate(200)
tts.set_volume(0.8)
tts.set_voice(1)  # Female voice
voices = tts.list_voices()
```

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| UI | Streamlit | Web interface |
| OCR | Tesseract | Text extraction |
| Simplification | T5/BART | AI text processing |
| NLP | Transformers | Model framework |
| Deep Learning | PyTorch | Model backend |
| TTS | pyttsx3 | Audio generation |
| Language | Python 3.8+ | Core language |

## Performance Considerations

- **OCR**: 1-5 minutes per page depending on image quality
- **Simplification**: 10-30 seconds per 1000 words
- **TTS**: Real-time or faster depending on text length
- **Memory**: ~4GB for model loading

## Security Notes

- No data is stored after session ends
- All processing is local (no cloud upload)
- User files are temporary and auto-deleted
- No API keys required (offline operation)

## Future Enhancements

- Multi-language support
- Custom vocabulary/abbreviations
- Spaced repetition for learning
- User preferences/profiles
- Cloud storage integration
- Mobile app version
- Advanced NLP features
