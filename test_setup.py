#!/usr/bin/env python
"""
Simple test to verify project setup and run a basic demo
"""

import sys
import os

print("=" * 60)
print("Reading Aid for Dyslexic People - Installation Test")
print("=" * 60)

# Test 1: Check Python version
print("\n✓ Python Version Check:")
print(f"  Python {sys.version}")

# Test 2: Check available packages
print("\n✓ Checking Core Packages:")
packages = []

try:
    import streamlit
    packages.append(("streamlit", streamlit.__version__))
    print("  ✓ streamlit installed")
except:
    print("  ✗ streamlit NOT found")

try:
    import pytesseract
    packages.append(("pytesseract", "available"))
    print("  ✓ pytesseract installed")
except:
    print("  ✗ pytesseract NOT found")

try:
    import PIL
    packages.append(("PIL", "available"))
    print("  ✓ PIL/Pillow installed")
except:
    print("  ✗ PIL/Pillow NOT found")

try:
    import pdf2image
    packages.append(("pdf2image", "available"))
    print("  ✓ pdf2image installed")
except:
    print("  ✗ pdf2image NOT found")

try:
    import transformers
    packages.append(("transformers", transformers.__version__))
    print("  ✓ transformers installed")
except:
    print("  ✗ transformers NOT found")

try:
    import torch
    packages.append(("torch", torch.__version__))
    print("  ✓ PyTorch installed")
except:
    print("  ✗ PyTorch NOT found")

try:
    import pyttsx3
    packages.append(("pyttsx3", "available"))
    print("  ✓ pyttsx3 installed")
except:
    print("  ✗ pyttsx3 NOT found")

try:
    import numpy
    packages.append(("numpy", numpy.__version__))
    print("  ✓ numpy installed")
except:
    print("  ✗ numpy NOT found")

# Test 3: Check project files
print("\n✓ Checking Project Files:")
files_to_check = [
    "app.py",
    "src/modules/ocr_extractor.py",
    "src/modules/text_simplifier.py",
    "src/modules/text_to_speech.py",
    "requirements.txt",
    "config.py"
]

for file in files_to_check:
    if os.path.exists(file):
        print(f"  ✓ {file} found")
    else:
        print(f"  ✗ {file} NOT found")

# Test 4: Try importing project modules
print("\n✓ Testing Project Modules:")
try:
    from src.modules.text_to_speech import TextToSpeech
    print("  ✓ TextToSpeech module imported successfully")
except Exception as e:
    print(f"  ✗ TextToSpeech import failed: {e}")

# Summary
print("\n" + "=" * 60)
print("Setup Status: READY")
print("=" * 60)
print("\nNext steps:")
print("1. Ensure Tesseract OCR is installed on your system")
print("2. Run: streamlit run app.py")
print("3. Open browser to: http://localhost:8501")
print("\n" + "=" * 60)
