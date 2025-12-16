# 🚀 How to Run This Project - Complete Guide

## ✅ Current Status

Your project is **almost ready** to run! Here's what's already set up:

- ✅ Virtual environment exists (`env/`)
- ✅ All Python packages installed (streamlit, transformers, torch, etc.)
- ✅ AI models (T5-small, BART) are working
- ✅ Project structure is complete
- ❌ **Tesseract OCR needs to be installed** (required for PDF/Image text extraction)

---

## 📋 Prerequisites Checklist

- [x] Python 3.12.8 installed
- [x] Virtual environment created
- [x] Python dependencies installed
- [ ] **Tesseract OCR installed** ← **YOU NEED THIS**

---

## 🔧 Step 1: Install Tesseract OCR (REQUIRED)

### Windows Installation

**Option A: Using Installer (Recommended)**

1. **Download Tesseract Installer:**
   - Go to: https://github.com/UB-Mannheim/tesseract/wiki
   - Download: `tesseract-ocr-w64-setup-5.3.3.20231005.exe` (or latest version)

2. **Install Tesseract:**
   - Run the installer
   - **IMPORTANT:** During installation, note the installation path
   - Default path: `C:\Program Files\Tesseract-OCR\`
   - Make sure to check "Add to PATH" option

3. **Verify Installation:**
   ```powershell
   tesseract --version
   ```
   
   If this doesn't work, you need to add Tesseract to PATH manually.

**Option B: Using Chocolatey (If you have it)**

```powershell
choco install tesseract
```

### Adding Tesseract to PATH (If needed)

If `tesseract --version` doesn't work:

1. Open System Properties → Environment Variables
2. Under "System variables", find "Path"
3. Click "Edit" → "New"
4. Add: `C:\Program Files\Tesseract-OCR`
5. Click OK and restart PowerShell

---

## 🚀 Step 2: Run the Application

Once Tesseract is installed, follow these steps:

### 1. Activate Virtual Environment

```powershell
cd d:\aid-for
.\env\Scripts\activate
```

You should see `(env)` in your prompt.

### 2. Verify All Dependencies

```powershell
python -c "import streamlit, pytesseract, transformers, torch; print('✅ All packages OK')"
```

### 3. Verify Tesseract

```powershell
python -c "import pytesseract; print(pytesseract.get_tesseract_version())"
```

### 4. Run the Streamlit App

```powershell
streamlit run app.py
```

The app will automatically open in your browser at: **http://localhost:8501**

---

## 🎯 Step 3: Use the Application

### Tab 1: 📤 Upload & Extract
1. Choose input method:
   - **Upload PDF** - Extract text from PDF documents
   - **Upload Image** - Extract text from images (JPG, PNG, etc.)
   - **Paste Text** - Directly paste text

2. Upload your file or paste text
3. Text will be extracted automatically

### Tab 2: ✏️ Simplify
1. Select AI model in sidebar:
   - **T5-small** - Faster (60M parameters)
   - **BART** - Better quality (139M parameters)

2. Click "🤖 Simplify Text"
3. View side-by-side comparison
4. Download simplified text

### Tab 3: 🔊 Listen
1. Adjust settings in sidebar:
   - Speech rate (50-300 WPM)
   - Volume (0.0-1.0)
   - Voice gender (Male/Female)

2. Click "▶️ Play Audio" to listen
3. Click "💾 Save Audio" to download MP3

### Tab 4: 📊 Analysis
- View reading level statistics
- Compare original vs simplified text
- See Flesch-Kincaid scores
- Track improvement metrics

---

## ⚙️ Configuration Options

### Sidebar Settings

**AI Model Settings:**
- T5-small: Fast, good quality
- BART: Slower, excellent quality

**Text-to-Speech Settings:**
- Speech Rate: 50-300 WPM (default: 150)
- Volume: 0.0-1.0 (default: 1.0)
- Voice: Male or Female

**Simplification Settings:**
- Target Reading Level: Easy/Moderate/Difficult
- Max Sentence Length: 50-200 words

---

## 🧪 Testing the Application

### Quick Test Scripts

```powershell
# Test transformers (T5 and BART)
python verify_transformers.py

# Comprehensive tests
python test_transformers.py

# Test app workflow
python test_app_workflow.py

# Live demonstration
python demo_transformers.py
```

### Manual Testing

1. **Test with Sample Text:**
   - Go to "Paste Text" tab
   - Paste: "The mitochondria is the powerhouse of the cell, responsible for producing adenosine triphosphate through cellular respiration."
   - Click "Simplify Text"
   - Expected: Simpler version of the text

2. **Test with Image:**
   - Upload any image with text
   - Should extract text automatically

---

## 🐛 Troubleshooting

### Issue: "Tesseract not found"
**Solution:**
- Install Tesseract (see Step 1)
- Add to PATH
- Restart PowerShell

### Issue: "Models are slow to load"
**Solution:**
- First time: Models download from Hugging Face (1-3 minutes)
- Subsequent runs: Models load from cache (5-10 seconds)
- Be patient on first run!

### Issue: "Streamlit won't start"
**Solution:**
```powershell
# Make sure virtual environment is activated
.\env\Scripts\activate

# Check if port 8501 is in use
netstat -ano | findstr :8501

# If in use, kill the process or use different port
streamlit run app.py --server.port 8502
```

### Issue: "AI models not simplifying text"
**Solution:**
```powershell
# Restart Streamlit
# Press Ctrl+C in terminal
streamlit run app.py

# Or clear cache in the app (press 'C')
```

### Issue: "Audio not playing"
**Solution:**
- Check system volume
- Try saving audio first, then play the file
- Ensure pyttsx3 is installed: `pip show pyttsx3`

---

## 📊 Performance Expectations

| Operation | First Run | Subsequent Runs |
|-----------|-----------|-----------------|
| Model Download | 1-3 minutes | N/A (cached) |
| Model Loading | 30-60 seconds | 5-10 seconds |
| OCR (1 page) | 1-5 seconds | 1-5 seconds |
| Simplification (1000 words) | 10-30 seconds | 10-30 seconds |
| Text-to-Speech | Real-time | Real-time |

---

## 🎨 Features Overview

### ✅ Full Pipeline
1. **OCR Extraction** - PDF/Image → Text (Tesseract)
2. **AI Simplification** - Complex → Simple (T5/BART)
3. **Text-to-Speech** - Text → Audio (pyttsx3)
4. **Analysis** - Reading level metrics (Flesch-Kincaid)

### ✅ Supported Formats

**Input:**
- PDF files (.pdf)
- Images (.jpg, .jpeg, .png, .bmp, .tiff)
- Plain text (paste directly)

**Output:**
- Simplified text (.txt)
- Audio files (.mp3)

---

## 💡 Tips for Best Results

### For OCR:
- Use high-quality, clear images
- Ensure good contrast between text and background
- Avoid handwritten text (OCR works best with printed text)

### For Simplification:
- **T5-small**: Use for academic/scientific text, faster
- **BART**: Use for complex legal/technical text, better quality
- Start with smaller text chunks to test

### For Text-to-Speech:
- Adjust speech rate to your preference
- Use headphones for better audio quality
- Save audio for offline listening

---

## 🔄 Quick Start Commands

```powershell
# Navigate to project
cd d:\aid-for

# Activate environment
.\env\Scripts\activate

# Run the app
streamlit run app.py
```

**That's it!** The app will open at: http://localhost:8501

---

## 📞 Need Help?

### Check These Files:
- `TRANSFORMERS_STATUS.md` - AI models status
- `README.md` - Project overview
- `QUICKSTART.md` - Quick setup guide
- `SETUP.md` - Detailed setup instructions

### Run Diagnostics:
```powershell
# Check environment
python check_environment.py

# Verify transformers
python verify_transformers.py

# Test complete workflow
python test_app_workflow.py
```

---

## ✨ What Makes This Project Special

- 🎯 **Designed for Dyslexic Readers** - Accessibility-first design
- 🤖 **AI-Powered** - State-of-the-art T5 and BART models
- 🔊 **Text-to-Speech** - Listen to simplified text
- 📊 **Reading Analysis** - Track improvement with metrics
- 🎨 **User-Friendly** - Clean, intuitive Streamlit interface
- 🆓 **100% Free** - No API keys, runs locally

---

**Status**: 🟢 **READY TO RUN** (after installing Tesseract)

**App URL**: http://localhost:8501

**Made with ❤️ to help dyslexic readers access and understand complex texts**
