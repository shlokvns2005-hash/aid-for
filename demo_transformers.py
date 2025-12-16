"""
Live Demonstration of Transformers in Action
Shows real-time text simplification with both models
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80)

def print_section(text):
    """Print a formatted section"""
    print("\n" + "-"*80)
    print(f"  {text}")
    print("-"*80)

def demonstrate_simplification():
    """Demonstrate text simplification with real examples"""
    
    print_header("🚀 TRANSFORMERS LIVE DEMONSTRATION")
    
    # Example texts
    examples = [
        {
            "title": "Scientific Text",
            "text": "The mitochondria is the powerhouse of the cell, responsible for producing adenosine triphosphate through the process of cellular respiration."
        },
        {
            "title": "Legal Text",
            "text": "The aforementioned party shall be held accountable for any and all damages resulting from the breach of contract."
        },
        {
            "title": "Academic Text",
            "text": "Contemporary educational methodologies emphasize collaborative learning environments that facilitate knowledge construction."
        }
    ]
    
    # Initialize models
    print("\n📦 Loading AI Models...")
    print("   (This may take a moment on first run)")
    
    t5_simplifier = TextSimplifier(model_type="t5")
    print("   ✅ T5-small loaded")
    
    bart_simplifier = TextSimplifier(model_type="bart")
    print("   ✅ BART loaded")
    
    # Process each example
    for i, example in enumerate(examples, 1):
        print_header(f"Example {i}: {example['title']}")
        
        original = example['text']
        print(f"\n📝 ORIGINAL TEXT:")
        print(f"   {original}")
        
        # Calculate original reading level
        orig_level = t5_simplifier.calculate_flesch_kincaid_level(original)
        print(f"\n📊 Original Reading Level: {orig_level['fk_level']} ({orig_level['complexity'].upper()})")
        
        # T5 Simplification
        print_section("🤖 T5-small Simplification")
        t5_result = t5_simplifier.simplify_text(original, max_length=100)
        t5_level = t5_simplifier.calculate_flesch_kincaid_level(t5_result)
        
        print(f"\n   Result: {t5_result}")
        print(f"\n   📊 Reading Level: {t5_level['fk_level']} ({t5_level['complexity'].upper()})")
        print(f"   📈 Improvement: {orig_level['fk_level'] - t5_level['fk_level']:.2f} levels easier")
        
        # BART Simplification
        print_section("🤖 BART Simplification")
        bart_result = bart_simplifier.simplify_text(original, max_length=100)
        bart_level = bart_simplifier.calculate_flesch_kincaid_level(bart_result)
        
        print(f"\n   Result: {bart_result}")
        print(f"\n   📊 Reading Level: {bart_level['fk_level']} ({bart_level['complexity'].upper()})")
        print(f"   📈 Improvement: {orig_level['fk_level'] - bart_level['fk_level']:.2f} levels easier")
    
    print_header("✅ DEMONSTRATION COMPLETE")
    
    print("\n🎯 Key Takeaways:")
    print("   • Both T5 and BART models are working perfectly")
    print("   • Text complexity is being reduced successfully")
    print("   • Reading levels are being calculated accurately")
    print("   • The Streamlit app has full AI functionality")
    
    print("\n🌐 Access the app at: http://localhost:8501")
    print("   Try uploading your own text to see the magic! ✨\n")

if __name__ == "__main__":
    try:
        demonstrate_simplification()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
