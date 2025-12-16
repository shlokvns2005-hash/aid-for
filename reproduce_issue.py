"""
Reproduction script to check if the model returns original + simplified text.
"""
import sys
from pathlib import Path
import logging

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

def test_output_format():
    print("="*80)
    print("TESTING MODEL OUTPUT FORMAT")
    print("="*80)

    text = "The aforementioned party shall be held accountable and liable for any and all damages."
    
    # Test BART
    print("\nTesting BART (sshleifer/distilbart-cnn-12-6)...")
    try:
        simplifier = TextSimplifier(model_type="bart")
        simplified = simplifier.simplify_text(text, max_length=100)
        
        print(f"\nInput: '{text}'")
        print(f"Output: '{simplified}'")
        
        if text in simplified and len(simplified) > len(text):
            print("WARNING: Output seems to contain input + something else.")
        else:
            print("SUCCESS: Output looks normal (not just input + output).")
            
    except Exception as e:
        print(f"ERROR: {e}")

    # Test T5
    print("\nTesting T5...")
    try:
        simplifier = TextSimplifier(model_type="t5")
        simplified = simplifier.simplify_text(text, max_length=100)
        
        print(f"\nInput: '{text}'")
        print(f"Output: '{simplified}'")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_output_format()
