"""
Test script to verify transformers functionality
Tests both T5 and BART models for text simplification
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

def test_t5_model():
    """Test T5 model for text simplification"""
    print("\n" + "="*60)
    print("Testing T5-small Model")
    print("="*60)
    
    try:
        simplifier = TextSimplifier(model_type="t5")
        
        test_text = """
        The phenomenon of photosynthesis is an extraordinarily complex 
        biochemical process whereby plants convert light energy into 
        chemical energy stored in glucose molecules.
        """
        
        print(f"\nOriginal Text:\n{test_text.strip()}")
        
        simplified = simplifier.simplify_text(test_text, max_length=100)
        
        print(f"\nSimplified Text:\n{simplified}")
        
        # Calculate reading levels
        original_level = simplifier.calculate_flesch_kincaid_level(test_text)
        simplified_level = simplifier.calculate_flesch_kincaid_level(simplified)
        
        print(f"\nOriginal Reading Level: {original_level['fk_level']} ({original_level['complexity']})")
        print(f"Simplified Reading Level: {simplified_level['fk_level']} ({simplified_level['complexity']})")
        
        print("\n✅ T5 Model Test PASSED!")
        return True
        
    except Exception as e:
        print(f"\n❌ T5 Model Test FAILED: {str(e)}")
        return False


def test_bart_model():
    """Test BART model for text simplification"""
    print("\n" + "="*60)
    print("Testing BART Model")
    print("="*60)
    
    try:
        simplifier = TextSimplifier(model_type="bart")
        
        test_text = """
        Quantum mechanics is a fundamental theory in physics that 
        describes the physical properties of nature at the scale of 
        atoms and subatomic particles.
        """
        
        print(f"\nOriginal Text:\n{test_text.strip()}")
        
        simplified = simplifier.simplify_text(test_text, max_length=100)
        
        print(f"\nSimplified Text:\n{simplified}")
        
        # Calculate reading levels
        original_level = simplifier.calculate_flesch_kincaid_level(test_text)
        simplified_level = simplifier.calculate_flesch_kincaid_level(simplified)
        
        print(f"\nOriginal Reading Level: {original_level['fk_level']} ({original_level['complexity']})")
        print(f"Simplified Reading Level: {simplified_level['fk_level']} ({simplified_level['complexity']})")
        
        print("\n✅ BART Model Test PASSED!")
        return True
        
    except Exception as e:
        print(f"\n❌ BART Model Test FAILED: {str(e)}")
        return False


def test_basic_simplification():
    """Test basic rule-based simplification"""
    print("\n" + "="*60)
    print("Testing Basic Rule-Based Simplification")
    print("="*60)
    
    try:
        simplifier = TextSimplifier(model_type="basic")
        
        test_text = """
        The quick brown fox jumps over the lazy dog, and then it runs 
        through the forest because it was being chased by hunters.
        """
        
        print(f"\nOriginal Text:\n{test_text.strip()}")
        
        simplified = simplifier.simplify_text(test_text)
        
        print(f"\nSimplified Text:\n{simplified}")
        
        print("\n✅ Basic Simplification Test PASSED!")
        return True
        
    except Exception as e:
        print(f"\n❌ Basic Simplification Test FAILED: {str(e)}")
        return False


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("TRANSFORMERS FUNCTIONALITY TEST SUITE")
    print("="*60)
    
    results = {
        "Basic": test_basic_simplification(),
        "T5": test_t5_model(),
        "BART": test_bart_model()
    }
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for model, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{model:15} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Transformers are working correctly!")
    else:
        print("⚠️  SOME TESTS FAILED! Check the output above for details.")
    print("="*60 + "\n")
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
