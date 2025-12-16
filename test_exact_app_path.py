"""
Direct test of the exact code path used in Streamlit app
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

print("="*80)
print("TESTING EXACT STREAMLIT APP CODE PATH")
print("="*80)

# Test 1: Import the module
print("\n1. Testing module import...")
try:
    from modules.text_simplifier import TextSimplifier
    print("   ✅ Module imported successfully")
except Exception as e:
    print(f"   ❌ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 2: Initialize T5 (as app does)
print("\n2. Initializing T5 model (as Streamlit app does)...")
try:
    model_type = "t5"  # This is what the app uses
    simplifier = TextSimplifier(model_type=model_type)
    print(f"   ✅ T5 simplifier initialized")
    print(f"   Model type: {simplifier.model_type}")
    print(f"   Has model: {simplifier.model is not None}")
    print(f"   Has tokenizer: {simplifier.tokenizer is not None}")
except Exception as e:
    print(f"   ❌ T5 initialization failed: {e}")
    import traceback
    traceback.print_exc()

# Test 3: Try the exact method the app calls
print("\n3. Testing split_and_simplify (exact app method)...")
try:
    test_text = "The quick brown fox jumps over the lazy dog."
    result = simplifier.split_and_simplify(test_text, chunk_size=100)
    print(f"   ✅ Simplification successful")
    print(f"   Input: {test_text}")
    print(f"   Output: {result}")
except Exception as e:
    print(f"   ❌ Simplification failed: {e}")
    import traceback
    traceback.print_exc()

# Test 4: Initialize BART
print("\n4. Initializing BART model...")
try:
    bart_simplifier = TextSimplifier(model_type="bart")
    print(f"   ✅ BART simplifier initialized")
    print(f"   Model type: {bart_simplifier.model_type}")
    print(f"   Has model: {bart_simplifier.model is not None}")
    print(f"   Has tokenizer: {bart_simplifier.tokenizer is not None}")
except Exception as e:
    print(f"   ❌ BART initialization failed: {e}")
    import traceback
    traceback.print_exc()

# Test 5: BART simplification
print("\n5. Testing BART simplification...")
try:
    result = bart_simplifier.split_and_simplify(test_text, chunk_size=100)
    print(f"   ✅ BART simplification successful")
    print(f"   Output: {result}")
except Exception as e:
    print(f"   ❌ BART simplification failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*80)
print("TEST COMPLETE")
print("="*80)
