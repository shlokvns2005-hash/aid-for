"""
Quick verification of transformers functionality
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

# Test text
test_text = "The phenomenon of photosynthesis is an extraordinarily complex biochemical process whereby plants convert light energy into chemical energy."

print("\n" + "="*70)
print("TRANSFORMERS VERIFICATION TEST")
print("="*70)

print(f"\nOriginal Text:\n{test_text}")

# Test T5
print("\n" + "-"*70)
print("Testing T5-small Model...")
print("-"*70)
try:
    t5_simplifier = TextSimplifier(model_type="t5")
    t5_result = t5_simplifier.simplify_text(test_text, max_length=100)
    print(f"T5 Result: {t5_result}")
    print("✅ T5 Model: WORKING")
except Exception as e:
    print(f"❌ T5 Model: FAILED - {str(e)}")

# Test BART
print("\n" + "-"*70)
print("Testing BART Model...")
print("-"*70)
try:
    bart_simplifier = TextSimplifier(model_type="bart")
    bart_result = bart_simplifier.simplify_text(test_text, max_length=100)
    print(f"BART Result: {bart_result}")
    print("✅ BART Model: WORKING")
except Exception as e:
    print(f"❌ BART Model: FAILED - {str(e)}")

# Test Basic
print("\n" + "-"*70)
print("Testing Basic Simplification...")
print("-"*70)
try:
    basic_simplifier = TextSimplifier(model_type="basic")
    basic_result = basic_simplifier.simplify_text(test_text)
    print(f"Basic Result: {basic_result}")
    print("✅ Basic Simplification: WORKING")
except Exception as e:
    print(f"❌ Basic Simplification: FAILED - {str(e)}")

print("\n" + "="*70)
print("VERIFICATION COMPLETE")
print("="*70 + "\n")
