"""
Test script to debug BART output issue
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

# Test sentence
test_text = "The mitochondria, often referred to as the powerhouse of the cell, is responsible for producing adenosine triphosphate through the process of cellular respiration."

print("=" * 80)
print("Testing BART Output")
print("=" * 80)
print(f"\nInput text:\n{test_text}")
print(f"\nInput length: {len(test_text)} chars, {len(test_text.split())} words")

# Initialize BART
print("\n" + "=" * 80)
print("Initializing BART model...")
simplifier = TextSimplifier(model_type="bart")

if simplifier.model_type != "bart":
    print(f"ERROR: Model type is {simplifier.model_type}, not bart!")
    sys.exit(1)

print("BART model loaded successfully!")

# Test simplify_text directly
print("\n" + "=" * 80)
print("Testing simplify_text() method directly...")
print("=" * 80)
simplified = simplifier.simplify_text(test_text, max_length=100)
print(f"\nOutput:\n{simplified}")
print(f"\nOutput length: {len(simplified)} chars, {len(simplified.split())} words")

# Check if output contains input
normalized_input = " ".join(test_text.split())
normalized_output = " ".join(simplified.split())

print("\n" + "=" * 80)
print("Analysis:")
print("=" * 80)
print(f"Output starts with input? {normalized_output.startswith(normalized_input)}")
print(f"Output contains input? {normalized_input in normalized_output}")

if normalized_output.startswith(normalized_input):
    print("\n⚠️ WARNING: Output starts with input text!")
    print(f"Input words: {len(normalized_input.split())}")
    print(f"Output words: {len(normalized_output.split())}")
    print(f"Extra words: {len(normalized_output.split()) - len(normalized_input.split())}")
else:
    print("\n✅ Output does NOT start with input - looks good!")

# Test split_and_simplify
print("\n" + "=" * 80)
print("Testing split_and_simplify() method...")
print("=" * 80)
simplified2 = simplifier.split_and_simplify(test_text, chunk_size=100)
print(f"\nOutput:\n{simplified2}")
print(f"\nOutput length: {len(simplified2)} chars, {len(simplified2.split())} words")

print("\n" + "=" * 80)
print("Done!")
print("=" * 80)
