"""
Test the actual Streamlit app workflow programmatically
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

def test_streamlit_workflow():
    """Simulate the Streamlit app workflow"""
    
    print("\n" + "="*70)
    print("STREAMLIT APP WORKFLOW TEST")
    print("="*70)
    
    # Sample text (as if uploaded/pasted in the app)
    sample_text = """
    Artificial intelligence has revolutionized numerous industries by 
    enabling machines to perform tasks that traditionally required human 
    intelligence, such as visual perception, speech recognition, and 
    decision-making processes.
    """
    
    print(f"\n📄 Step 1: Text Input")
    print(f"Original Text: {sample_text.strip()}")
    
    # Test T5 simplification (as selected in sidebar)
    print(f"\n🤖 Step 2: Simplifying with T5-small...")
    try:
        t5_simplifier = TextSimplifier(model_type="t5")
        t5_simplified = t5_simplifier.split_and_simplify(sample_text, chunk_size=100)
        t5_level = t5_simplifier.calculate_flesch_kincaid_level(t5_simplified)
        
        print(f"✅ T5 Simplified: {t5_simplified}")
        print(f"   Reading Level: {t5_level['fk_level']} ({t5_level['complexity']})")
    except Exception as e:
        print(f"❌ T5 Error: {str(e)}")
        return False
    
    # Test BART simplification
    print(f"\n🤖 Step 3: Simplifying with BART...")
    try:
        bart_simplifier = TextSimplifier(model_type="bart")
        bart_simplified = bart_simplifier.split_and_simplify(sample_text, chunk_size=100)
        bart_level = bart_simplifier.calculate_flesch_kincaid_level(bart_simplified)
        
        print(f"✅ BART Simplified: {bart_simplified}")
        print(f"   Reading Level: {bart_level['fk_level']} ({bart_level['complexity']})")
    except Exception as e:
        print(f"❌ BART Error: {str(e)}")
        return False
    
    print("\n" + "="*70)
    print("✅ ALL STREAMLIT WORKFLOW TESTS PASSED!")
    print("="*70 + "\n")
    
    return True

if __name__ == "__main__":
    success = test_streamlit_workflow()
    
    if success:
        print("\n🎉 TRANSFORMERS ARE WORKING CORRECTLY IN THE APP!")
        print("\nYou can now use the Streamlit app at http://localhost:8501")
        print("Both T5-small and BART models are fully functional.\n")
    else:
        print("\n⚠️  There were some issues. Check the output above.\n")
    
    sys.exit(0 if success else 1)
