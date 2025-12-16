"""
Interactive test - Run this and tell me what error you see
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

print("\n" + "="*80)
print("INTERACTIVE STREAMLIT SIMULATION TEST")
print("="*80)

# Simulate the exact Streamlit workflow
print("\nSimulating Streamlit app workflow...")

# Step 1: User selects model
model_type_display = "T5-small"  # What user sees in UI
model_map = {"T5-small": "t5", "BART": "bart"}
selected_model = model_map[model_type_display]

print(f"\n1. User selected: {model_type_display}")
print(f"   Mapped to: {selected_model}")

# Step 2: User has some text
extracted_text = """
Artificial intelligence represents a transformative technological paradigm 
that encompasses machine learning algorithms, neural networks, and 
sophisticated computational methodologies designed to emulate human 
cognitive processes and decision-making capabilities.
"""

print(f"\n2. User's text loaded ({len(extracted_text.split())} words)")

# Step 3: User clicks "Simplify Text" button
print(f"\n3. User clicks 'Simplify Text' button...")
print(f"   Initializing {model_type_display} model...")

try:
    # This is EXACTLY what the app does
    simplifier = TextSimplifier(model_type=selected_model)
    print(f"   ✅ Model initialized")
    
    # Split and simplify
    print(f"   Processing text...")
    simplified_text = simplifier.split_and_simplify(
        extracted_text,
        chunk_size=100
    )
    
    print(f"   ✅ Text simplified successfully!")
    print(f"\n   ORIGINAL:")
    print(f"   {extracted_text.strip()[:100]}...")
    print(f"\n   SIMPLIFIED:")
    print(f"   {simplified_text}")
    
    # Calculate reading level
    print(f"\n   Calculating reading level...")
    reading_level = simplifier.calculate_flesch_kincaid_level(simplified_text)
    
    print(f"   ✅ Reading level calculated")
    print(f"   Level: {reading_level['fk_level']}")
    print(f"   Complexity: {reading_level['complexity']}")
    
    print("\n" + "="*80)
    print("✅ SUCCESS - Everything works exactly as in Streamlit!")
    print("="*80)
    
except Exception as e:
    print(f"\n❌ ERROR OCCURRED:")
    print(f"   {type(e).__name__}: {str(e)}")
    print("\nFull traceback:")
    import traceback
    traceback.print_exc()
    
    print("\n" + "="*80)
    print("❌ FAILURE - This is the error you're seeing!")
    print("="*80)

print("\n📝 Please copy the output above and share what error you see.\n")
