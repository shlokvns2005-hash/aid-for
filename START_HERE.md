# 🚀 START HERE - Reading Aid for Dyslexic People

## ⚡ Quick Start (2 minutes)

### Step 1: Run the Application
Open PowerShell and type:
```powershell
cd d:\aid-for
python app_lite.py
```

### Step 2: Select an Option
- **Option 1**: Extract text from a PDF or image
- **Option 2**: Simplify text  
- **Option 3**: Convert text to speech
- **Option 4**: Full pipeline (extract → simplify → speech)
- **Option 5**: Exit

**That's it!** The application is ready to use.

---

## 📋 What's Currently Available

✅ **Working Now (No setup needed)**
- Text-to-speech conversion
- Basic text simplification
- Reading level analysis

⏳ **Requires Tesseract OCR installation (5 min)**
- Extract text from PDF files
- Extract text from images (JPG, PNG, BMP)

❌ **Requires advanced packages (optional)**
- Web interface (Streamlit)
- AI-powered text simplification (T5 model)

---

## 🔧 Installation - Optional but Recommended

### Install Tesseract OCR (Enables PDF/Image Processing)

**Windows:**

1. Download installer: 
   https://github.com/UB-Mannheim/tesseract/releases/download/v5.3.0/tesseract-ocr-w64-setup-v5.3.0.20230101.exe

2. Run the installer and note the installation path (e.g., `C:\Program Files\Tesseract-OCR`)

3. Configure in Python - Edit `src/modules/ocr_extractor.py` and add this at the top of the file:

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

4. Verify installation:
```powershell
python test_setup.py
```

---

## 🎯 Common Tasks

### Extract Text from a PDF
```
$ python app_lite.py
Select option (1-5): 1
Enter PDF/Image file path: C:\Users\YourName\Downloads\document.pdf
```

### Simplify Complex Text
```
Select option (1-5): 2
Enter text to simplify: Your text here...
```
Shows reading level: Easy, Normal, Advanced, or Very Advanced

### Listen to Text Being Read
```
Select option (1-5): 3
Enter text for speech: Your text here...
```
Your computer will read the text aloud!

### Complete Workflow (Extract → Simplify → Listen)
```
Select option (1-5): 4
Enter PDF/Image file path: document.pdf
```
- Extracts text
- Simplifies it
- Shows reading level
- Optionally reads it aloud

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **INSTALL_AND_RUN.md** | Detailed setup and usage guide |
| **QUICKSTART.md** | 5-minute setup guide |
| **ARCHITECTURE.md** | Technical system design |
| **DEVELOPER_GUIDE.md** | For developers extending the project |
| **examples.py** | Code examples |

---

## ✨ Features

### Core Functionality
- 📄 Extract text from PDFs and images
- ✏️ Simplify complex text automatically
- 🔊 Convert text to speech
- 📊 Calculate reading difficulty levels
- 💾 Save simplified text and audio

### Advanced Features (with Streamlit)
- 🌐 Web-based interface
- 🤖 AI-powered text simplification
- 📈 Advanced reading metrics
- 🎨 Customizable display options

---

## 🛠️ Troubleshooting

### "pytesseract not found" Error
**Solution:** Install Tesseract OCR (see Installation section above)

### "Module not found" Error  
**Solution:** Make sure you're in the right directory:
```powershell
cd d:\aid-for
python app_lite.py
```

### TTS not working
**Solution:** Install Windows audio support:
```powershell
python -m pip install --upgrade pip
pip install comtypes pywin32
```

### Need advanced features?
**Solution:** The web interface with AI models requires large packages. If installation fails:
- Use Python 3.11 or 3.12 instead (Python 3.14 has limited support)
- Or stick with the CLI version which works great!

---

## 💡 Pro Tips

1. **Save text for later:** Copy simplified text from the CLI and paste into a file
2. **Adjust speech speed:** In app_lite.py, change `rate=150` to any value 50-300
3. **Use different voices:** In app_lite.py, change `voice_id=0` to 0, 1, 2, etc.
4. **Batch process:** Use Python scripts with the modules directly

---

## 🎓 Learning by Example

### Example 1: Simple Text-to-Speech
```python
from src.modules.text_to_speech import TextToSpeech

tts = TextToSpeech(rate=150)
tts.speak("Hello, this is the reading aid application!")
```

### Example 2: Extract and Simplify
```python
from src.modules.ocr_extractor import OCRExtractor

ocr = OCRExtractor()
text = ocr.extract_from_pdf('mydocument.pdf')
print(text)
```

### Example 3: Check Reading Level
```python
text = "The quick brown fox jumps over the lazy dog."
words = len(text.split())
sentences = text.count('.') + 1

grade_level = (0.39 * words / sentences + 11.8 - 15.59)
print(f"Grade Level: {grade_level:.1f}")
```

---

## 🚀 Next Steps

### Immediate (Now)
1. ✅ Run `python app_lite.py` to test basic functionality
2. Try option 3 to hear text-to-speech in action

### Soon (5 minutes)
1. Install Tesseract OCR (see Installation section)
2. Try extracting text from a PDF (option 1)

### Later (Optional)
1. Install Streamlit for the web interface: `pip install streamlit torch transformers`
2. Run `streamlit run app.py` for the full web experience

---

## 📞 Getting Help

**Problem:** App won't start
- Check you're in the right directory: `cd d:\aid-for`
- Python must be installed: `python --version`

**Problem:** Missing packages
- Reinstall: `pip install pytesseract pillow pdf2image numpy pyttsx3 comtypes`

**Problem:** Tesseract errors
- Download and install Tesseract from: https://github.com/UB-Mannheim/tesseract/releases

**Problem:** Something else
- Check INSTALL_AND_RUN.md for detailed troubleshooting
- Look at examples.py for code examples

---

## ✅ Verification Checklist

- [ ] Python installed (`python --version` shows 3.11+)
- [ ] In correct directory (`cd d:\aid-for`)
- [ ] Core packages installed (run `python app_lite.py` - it should start)
- [ ] Can see the menu (options 1-5)
- [ ] Can try option 3 (text-to-speech)
- [ ] Optional: Install Tesseract for PDF extraction
- [ ] Optional: Install Streamlit for web interface

---

## 🎉 You're All Set!

**Your Reading Aid application is ready to use.**

Start with:
```powershell
python app_lite.py
```

Enjoy helping students with dyslexia learn more effectively! 📚✨

---

### Quick Command Reference

```bash
# Start the CLI application
python app_lite.py

# Start the web interface (if installed)
streamlit run app.py

# Run tests
python test_setup.py
python test_app.py

# See code examples
python examples.py

# Install all packages
pip install -r requirements.txt
```

---

**Version:** 1.0  
**Status:** ✅ Production Ready  
**Platform:** Windows 10/11  
**Python:** 3.11+ (tested with 3.14.0)  

**Questions?** Check the documentation files or see `INSTALL_AND_RUN.md` for detailed help.
