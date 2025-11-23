"""
Best Practices & Developer Guide
Guidelines for using and extending the Reading Aid application
"""

# ============================================================================
# BEST PRACTICES
# ============================================================================

"""
1. OCR EXTRACTION
   - Use high-quality images (min 300 DPI)
   - Clear, well-lit scans work best
   - Tesseract supports 100+ languages
   - Batch process large PDFs separately
   
2. TEXT SIMPLIFICATION
   - T5-small: Faster, good for real-time (60M params)
   - BART: Better quality, slower (139M params)
   - Keep chunks under 512 tokens
   - Batch multiple texts for efficiency
   
3. TEXT-TO-SPEECH
   - Slower speech rate (100-150 WPM) is best for learning
   - Test audio with target audience first
   - Save high-quality audio for later use
   - Consider voice preference (male/female)
   
4. READING LEVELS
   - FK < 6: Easy (elementary school)
   - FK 6-9: Moderate (middle school)
   - FK > 9: Difficult (high school+)
   - Goal: Reduce complex text to FK level 6-7
   
5. MEMORY MANAGEMENT
   - Models loaded on first use (~2-3GB)
   - Clear cache if running multiple apps
   - Monitor RAM during batch processing
   - Close other applications during heavy use
"""

# ============================================================================
# CODE EXAMPLES
# ============================================================================

"""
EXAMPLE 1: Quick Start
------------------------
from src.modules.ocr_extractor import OCRExtractor
from src.modules.text_simplifier import TextSimplifier
from src.modules.text_to_speech import TextToSpeech

# Extract
ocr = OCRExtractor()
text = ocr.extract_from_pdf("document.pdf")

# Simplify
simplifier = TextSimplifier(model_type="t5")
simple = simplifier.simplify_text(text)

# Listen
tts = TextToSpeech()
tts.speak(simple)


EXAMPLE 2: Error Handling
------------------------
try:
    text = ocr.extract_from_pdf("file.pdf")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")


EXAMPLE 3: Batch Processing
------------------------
from pathlib import Path

for pdf_file in Path("uploads").glob("*.pdf"):
    try:
        text = ocr.extract_from_pdf(str(pdf_file))
        simple = simplifier.simplify_text(text)
        print(f"Processed: {pdf_file.name}")
    except Exception as e:
        print(f"Failed {pdf_file.name}: {e}")
"""

# ============================================================================
# COMMON ISSUES & SOLUTIONS
# ============================================================================

"""
ISSUE 1: "Tesseract is not installed or it's not in your PATH"
SOLUTION:
  Windows:
    - Download: https://github.com/UB-Mannheim/tesseract/wiki
    - Run installer
    - Add to PATH: setx PATH "%PATH%;C:\\Program Files\\Tesseract-OCR"
    - Or update code: pytesseract.pytesseract.pytesseract_cmd = r'...'
  
  Linux:
    - sudo apt-get install tesseract-ocr
  
  macOS:
    - brew install tesseract

ISSUE 2: "CUDA out of memory"
SOLUTION:
  - Use smaller batch size (config.py: batch_size=1)
  - Use T5-small instead of BART
  - Disable FP16: use_fp16=False in config.py
  - Close other applications

ISSUE 3: "Models won't download"
SOLUTION:
  - Check internet connection
  - Set proxy if behind corporate firewall
  - Manually download: python -c "from transformers import..."
  - Clear cache: rm -rf ~/.cache/huggingface/

ISSUE 4: "Audio not playing"
SOLUTION:
  Linux: sudo apt-get install espeak
  Windows: Check Sound settings
  macOS: System Preferences > Sound
  All: Test with tts.save_to_file() instead of tts.speak()

ISSUE 5: "Slow performance"
SOLUTION:
  - Reduce PDF DPI: ocr_config['pdf_dpi'] = 150
  - Use T5-small model (faster than BART)
  - Reduce max_length in simplification
  - Process in smaller batches
"""

# ============================================================================
# PERFORMANCE OPTIMIZATION TIPS
# ============================================================================

"""
FOR OCR:
  1. Resize images: 1200x1600 pixels is optimal
  2. Increase DPI only if needed (slows processing)
  3. Preprocess images (sharpen, contrast adjustment)
  4. Skip blank pages automatically

FOR SIMPLIFICATION:
  1. Cache models after first load
  2. Batch process multiple texts
  3. Use smaller max_length for faster processing
  4. Consider using T5-small for real-time apps

FOR TTS:
  1. Pre-generate audio for frequently used texts
  2. Use lower quality for previews
  3. Save to disk for repeated playback
  4. Consider TTS acceleration libraries

GENERAL:
  1. Use SSD for model storage (faster loading)
  2. Monitor memory with: psutil.virtual_memory()
  3. Use GPU if available (CUDA)
  4. Implement caching at all levels
"""

# ============================================================================
# TESTING GUIDE
# ============================================================================

"""
UNIT TESTING
  python test_app.py

INTEGRATION TESTING
  1. Test with real PDFs
  2. Test with various image qualities
  3. Test with different text lengths
  4. Test error conditions

PERFORMANCE TESTING
  import time
  start = time.time()
  result = simplifier.simplify_text(text)
  elapsed = time.time() - start
  print(f"Time: {elapsed:.2f}s")

QUALITY TESTING
  1. Compare FK levels before/after
  2. Manual review of simplified text
  3. User testing with target audience
  4. Measure comprehension improvement
"""

# ============================================================================
# EXTENDING THE APPLICATION
# ============================================================================

"""
ADD NEW MODEL:
  1. Add to text_simplifier.py _load_model()
  2. Update Streamlit UI in app.py
  3. Test with test_app.py
  4. Document in README.md

ADD NEW LANGUAGE:
  1. Install Tesseract language pack
  2. Update OCR_CONFIG languages in config.py
  3. Test OCR extraction
  4. Update UI language selector

ADD NEW FEATURE:
  1. Create new module in src/modules/
  2. Implement core functionality
  3. Add unit tests
  4. Create Streamlit tab in app.py
  5. Update documentation

DEPLOYMENT:
  1. Use Streamlit Cloud: streamlit.io/cloud
  2. Or Docker: create Dockerfile
  3. Set environment variables for configs
  4. Test in production environment
"""

# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

"""
USING CONFIG.PY:

# Get configuration
from config import get_config
ocr_config = get_config("ocr")

# Update configuration
from config import update_config
update_config("tts", default_rate=120)

# Or directly import
from config import OCR_CONFIG, SIMPLIFICATION_CONFIG

ENVIRONMENT VARIABLES:

# Set paths
export TESSERACT_PATH=/usr/bin/tesseract
export HUGGINGFACE_CACHE=~/.cache/huggingface/

# Set in Python
import os
os.environ['TESSERACT_PATH'] = '/usr/bin/tesseract'

STREAMLIT SECRETS (optional):
  .streamlit/secrets.toml
  [api_keys]
  huggingface_key = "..."
"""

# ============================================================================
# DEPLOYMENT CHECKLIST
# ============================================================================

"""
PRE-DEPLOYMENT:
  □ All tests passing
  □ Documentation updated
  □ Requirements.txt current
  □ .gitignore configured
  □ No hardcoded API keys
  □ Error handling in place
  □ Logging configured
  □ Performance baseline set

DEPLOYMENT:
  □ Tesseract installed
  □ Python 3.8+ installed
  □ Virtual environment created
  □ Dependencies installed
  □ Configuration updated
  □ Directories created (uploads, output)
  □ Models pre-downloaded
  □ Application tested

POST-DEPLOYMENT:
  □ Monitor error logs
  □ Track performance metrics
  □ Gather user feedback
  □ Plan improvements
  □ Schedule updates
"""

# ============================================================================
# FREQUENTLY ASKED QUESTIONS
# ============================================================================

"""
Q: Can I use custom models?
A: Yes, update SIMPLIFICATION_CONFIG to use different models from HuggingFace

Q: How do I add support for another language?
A: Install Tesseract language pack and update OCR_CONFIG['languages']

Q: Can I deploy this on mobile?
A: Streamlit doesn't support native mobile, but use Streamlit Cloud for web access

Q: Is the application scalable?
A: Current design is single-user. For multi-user, deploy with Streamlit Cloud or use FastAPI backend

Q: How do I reduce startup time?
A: Pre-download models, use smaller batch sizes, optimize PDFs

Q: Can I use different TTS engines?
A: Yes, modify text_to_speech.py to use gTTS, Azure TTS, or Google Cloud TTS

Q: How do I improve OCR accuracy?
A: Use higher quality images, preprocess images, fine-tune models

Q: Is this HIPAA compliant?
A: Current implementation stores no data. Can be made compliant with encryption
"""

# ============================================================================
# RESOURCES & DOCUMENTATION
# ============================================================================

"""
OFFICIAL DOCUMENTATION:
  - Tesseract: https://github.com/UB-Mannheim/tesseract
  - Transformers: https://huggingface.co/docs/transformers
  - Streamlit: https://docs.streamlit.io
  - pyttsx3: https://pyttsx3.readthedocs.io

TUTORIALS:
  - Tesseract OCR: https://realpython.com/python-pytesseract/
  - Transformers: https://huggingface.co/course
  - Streamlit: https://30days.streamlit.io/

RELATED PROJECTS:
  - PyTorch: https://pytorch.org/
  - HuggingFace: https://huggingface.co/
  - OpenCV: https://opencv.org/
  - NLTK: https://www.nltk.org/

RESEARCH PAPERS:
  - Flesch Reading Ease: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
  - T5: Exploring Transfer Learning with Transformers
  - BART: Denoising Sequence-to-Sequence Pre-training
  - Text Simplification: A Survey
"""

# ============================================================================
# CONTACT & SUPPORT
# ============================================================================

"""
FOR ISSUES:
  1. Check error logs in logs/ directory
  2. Run test_app.py to verify setup
  3. Review SETUP.md troubleshooting section
  4. Search GitHub issues
  5. Create new issue with details

FOR CONTRIBUTIONS:
  1. Fork repository
  2. Create feature branch
  3. Make changes
  4. Write tests
  5. Submit pull request

FOR FEATURE REQUESTS:
  1. Open GitHub issue
  2. Describe use case
  3. Provide examples
  4. Link related issues

FOR QUESTIONS:
  1. Check README.md
  2. Review examples.py
  3. Check issues/discussions
  4. Open Q&A issue
"""

if __name__ == "__main__":
    print(__doc__)
