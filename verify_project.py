#!/usr/bin/env python3
"""
Project Verification Script
Comprehensive check of all components
"""

import sys
from pathlib import Path

print('='*80)
print('READING AID FOR DYSLEXIC PEOPLE - COMPREHENSIVE PROJECT CHECK')
print('='*80)
print()

# 1. Python Version
print('1 PYTHON ENVIRONMENT')
print('-' * 80)
print(f'   Python Version: {sys.version.split()[0]}')
print()

# 2. Core Packages
print('2 CORE PACKAGES STATUS')
print('-' * 80)

packages = {
    'pytesseract': 'PDF/Image OCR',
    'PIL': 'Image Processing',
    'pdf2image': 'PDF to Image Conversion',
    'numpy': 'Numerical Computing',
    'pyttsx3': 'Text-to-Speech Engine',
    'comtypes': 'Windows COM Integration'
}

installed_core = 0
for pkg, description in packages.items():
    try:
        __import__(pkg if pkg != 'PIL' else 'PIL')
        print(f'   [OK] {pkg:20} - {description}')
        installed_core += 1
    except ImportError:
        print(f'   [NO] {pkg:20} - {description}')

print(f'\n   Status: {installed_core}/{len(packages)} installed\n')

# 3. Optional Packages
print('3 OPTIONAL PACKAGES')
print('-' * 80)

optional = {
    'streamlit': 'Web Interface',
    'torch': 'PyTorch (ML)',
    'transformers': 'HuggingFace'
}

for pkg, description in optional.items():
    try:
        __import__(pkg)
        print(f'   [OK] {pkg:20} - {description}')
    except ImportError:
        print(f'   [NO] {pkg:20} - {description} (optional)')

print()

# 4. Module Import Test
print('4 MODULE IMPORT TEST')
print('-' * 80)

sys.path.insert(0, str(Path('.') / 'src'))

modules_ok = True
try:
    from modules.text_to_speech import TextToSpeech
    print('   [OK] TextToSpeech module imports successfully')
except Exception as e:
    print(f'   [NO] TextToSpeech: {str(e)[:40]}')
    modules_ok = False

try:
    from modules.ocr_extractor import OCRExtractor
    print('   [OK] OCRExtractor module imports successfully')
except Exception as e:
    print(f'   [NO] OCRExtractor: {str(e)[:40]}')
    modules_ok = False

try:
    from modules.text_simplifier import TextSimplifier
    print('   [OK] TextSimplifier module imports successfully')
except Exception as e:
    print(f'   [NO] TextSimplifier: {str(e)[:40]}')
    modules_ok = False

print()

# 5. Functional Tests
print('5 FUNCTIONAL TESTS')
print('-' * 80)

functional_ok = True

try:
    tts = TextToSpeech(rate=150)
    print('   [OK] TextToSpeech object created successfully')
except Exception as e:
    print(f'   [NO] TextToSpeech: {str(e)[:40]}')
    functional_ok = False

try:
    simplifier = TextSimplifier()
    test_text = 'The quick brown fox jumps over the lazy dog.'
    level = simplifier.calculate_flesch_kincaid_level(test_text)
    print(f'   [OK] TextSimplifier works (reading level: {level})')
except Exception as e:
    print(f'   [NO] TextSimplifier: {str(e)[:40]}')
    functional_ok = False

try:
    ocr = OCRExtractor()
    print('   [OK] OCRExtractor object created successfully')
except Exception as e:
    print(f'   [NO] OCRExtractor: {str(e)[:40]}')
    functional_ok = False

print()

# 6. Summary
print('='*80)
print('FINAL STATUS')
print('='*80)

all_ok = (installed_core == len(packages) and modules_ok and functional_ok)

if all_ok:
    print()
    print('   SUCCESS - Project is FULLY FUNCTIONAL and READY TO USE!')
    print()
    print('   Quick start:')
    print('   python app_lite.py')
    print()
else:
    print()
    print('   STATUS SUMMARY:')
    print(f'   Core packages: {installed_core}/{len(packages)}')
    print(f'   Module imports: {"PASS" if modules_ok else "FAIL"}')
    print(f'   Functional tests: {"PASS" if functional_ok else "FAIL"}')
    print()

print('='*80)
