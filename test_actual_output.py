"""
Test what the models are actually outputting
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

# Test with the exact text you're using
test_texts = [
    "Artificial intelligence encompasses machine learning algorithms and neural networks designed to emulate human cognitive functions.",
    "The mitochondria is the powerhouse of the cell.",
    "The phenomenon of photosynthesis is an extraordinarily complex biochemical process whereby plants convert light energy into chemical energy stored in glucose molecules."
]

print("="*80)
print("TESTING ACTUAL MODEL OUTPUT")
print("="*80)

for i, text in enumerate(test_texts, 1):
    print(f"\n{'='*80}")
    print(f"TEST {i}")
    print(f"{'='*80}")
    print(f"\nORIGINAL TEXT:")
    print(f"{text}")
    
    # Test T5
    print(f"\n{'-'*80}")
    print("T5-SMALL OUTPUT:")
    print(f"{'-'*80}")
    t5 = TextSimplifier(model_type="t5")
    t5_result = t5.simplify_text(text, max_length=100)
    print(f"{t5_result}")
    print(f"\nSame as original? {t5_result.strip() == text.strip()}")
    print(f"Length: Original={len(text)}, Simplified={len(t5_result)}")
    
    # Test BART
    print(f"\n{'-'*80}")
    print("BART OUTPUT:")
    print(f"{'-'*80}")
    bart = TextSimplifier(model_type="bart")
    bart_result = bart.simplify_text(text, max_length=100)
    print(f"{bart_result}")
    print(f"\nSame as original? {bart_result.strip() == text.strip()}")
    print(f"Length: Original={len(text)}, Simplified={len(bart_result)}")

print(f"\n{'='*80}")
print("ANALYSIS COMPLETE")
print(f"{'='*80}\n")
