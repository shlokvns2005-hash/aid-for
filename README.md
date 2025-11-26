# 📖 Reading Aid for Dyslexic People

An AI-powered accessibility tool that transforms complex texts into easy-to-read content with text-to-speech capabilities, specifically designed to help individuals with dyslexia.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

### 📤 **Multi-Format Input**
- Upload PDF documents
- Upload images (JPG, PNG, BMP, TIFF)
- Paste text directly into the app

### 🤖 **AI-Powered Text Simplification**
- **T5-small**: Fast, lightweight model (60M parameters)
- **BART**: Higher quality results (139M parameters)
- Automatic Flesch-Kincaid reading level analysis
- Side-by-side text comparison

### 🔊 **Text-to-Speech**
- Adjustable speech rate (50-300 WPM)
- Volume control
- Male/Female voice options
- Save audio as MP3 files

### 📊 **Reading Analysis**
- Reading level metrics
- Complexity assessment
- Before/after improvement tracking
- Word and sentence statistics

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Tesseract OCR

### Installation

**1. Install Tesseract OCR**

```bash
# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki

# Linux
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract
```

**2. Clone and Setup**

```bash
# Clone the repository
git clone <repository-url>
cd aid-for

# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
.\env\Scripts\activate
# Linux/macOS:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**3. Run the Application**

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
aid-for/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── config.py                   # Configuration settings
│
├── src/modules/
│   ├── ocr_extractor.py       # OCR text extraction
│   ├── text_simplifier.py     # AI text simplification
│   └── text_to_speech.py      # Text-to-speech conversion
│
├── uploads/                    # Uploaded files directory
├── output/                     # Generated audio files
│
└── docs/                       # Additional documentation
    ├── QUICKSTART.md
    ├── SETUP.md
    └── ARCHITECTURE.md
```

## 💻 Usage

### Basic Workflow

1. **Upload Content**
   - Navigate to the "📤 Upload & Extract" tab
   - Choose your input method (PDF, Image, or Text)
   - Upload or paste your content

2. **Simplify Text**
   - Go to the "✏️ Simplify" tab
   - Select your preferred AI model (T5-small or BART)
   - Click "Simplify Text"
   - Download the simplified version

3. **Listen to Audio**
   - Switch to the "🔊 Listen" tab
   - Adjust voice settings in the sidebar
   - Play audio or save as MP3

4. **Analyze Results**
   - Check the "📊 Analysis" tab
   - View reading level improvements
   - Compare original vs simplified statistics

### Code Example

```python
from src.modules.ocr_extractor import OCRExtractor
from src.modules.text_simplifier import TextSimplifier
from src.modules.text_to_speech import TextToSpeech

# Extract text from PDF
ocr = OCRExtractor()
text = ocr.extract_from_pdf("document.pdf")

# Simplify using AI
simplifier = TextSimplifier(model_type="t5")
simple_text = simplifier.simplify_text(text)

# Convert to speech
tts = TextToSpeech(rate=150)
tts.save_to_file(simple_text, "output.mp3")
```

## ⚙️ Configuration

Customize the application through the sidebar:

- **AI Model**: Choose between T5-small (faster) or BART (better quality)
- **Speech Rate**: Adjust from 50-300 words per minute
- **Voice Gender**: Select male or female voice
- **Target Reading Level**: Set complexity target
- **Max Sentence Length**: Control output sentence length

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Web Framework** | Streamlit |
| **OCR Engine** | Tesseract |
| **AI Models** | T5-small, BART (Hugging Face Transformers) |
| **ML Framework** | PyTorch |
| **Text-to-Speech** | pyttsx3 |
| **Language** | Python 3.8+ |

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Tesseract not found" | Install Tesseract and add to system PATH |
| Slow first run | AI models are downloading (5-10 minutes) |
| PDF extraction fails | Try converting to image format first |
| Audio not working | Check system volume, install espeak on Linux |
| Memory error | Close other applications, restart Streamlit |

For detailed troubleshooting, see [SETUP.md](SETUP.md)

## 📊 Performance

| Operation | Typical Time |
|-----------|--------------|
| Model Loading (first time) | 30-60 seconds |
| OCR (1 page) | 1-5 minutes |
| Text Simplification (1000 words) | 10-30 seconds |
| Text-to-Speech | Real-time |

## 🎯 Use Cases

- **Students**: Simplify textbooks and academic papers
- **Accessibility**: Make content accessible for dyslexic readers
- **Language Learners**: Simplify texts for non-native speakers
- **Content Creators**: Generate accessible versions of content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgments

- **Tesseract OCR** - Google's open-source OCR engine
- **Hugging Face** - For T5 and BART models
- **Streamlit** - For the web framework
- **pyttsx3** - For text-to-speech functionality

## 📚 Additional Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started in 1 minute
- [Setup Guide](SETUP.md) - Detailed installation instructions
- [Architecture](ARCHITECTURE.md) - Technical design details
- [Developer Guide](DEVELOPER_GUIDE.md) - Best practices for contributors

## 💬 Support

For questions, issues, or feature requests, please open an issue on GitHub.

---

**Made with ❤️ to help dyslexic readers access and understand complex texts**

*Version 1.0.0 | Last Updated: November 2024*