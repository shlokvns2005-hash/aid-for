"""
Testing and Utility Functions
"""

from src.modules.text_simplifier import TextSimplifier


def test_simplification():
    """Test text simplification with sample text"""
    
    sample_texts = [
        "The ubiquitous integration of artificial intelligence into contemporary technological paradigms necessitates comprehensive reevaluation of epistemological frameworks.",
        "Notwithstanding the aforementioned complications, the implementation of sophisticated methodologies facilitates unprecedented opportunities for organizational advancement.",
        "The dichotomy between phenomenological abstraction and empirical reification continues to perplex contemporary academic discourse."
    ]
    
    print("=" * 80)
    print("TEXT SIMPLIFICATION TEST")
    print("=" * 80)
    
    for model in ["t5", "bart"]:
        print(f"\n\nTesting with {model.upper()} model:")
        print("-" * 80)
        
        try:
            simplifier = TextSimplifier(model_type=model)
            
            for i, text in enumerate(sample_texts, 1):
                print(f"\n--- Example {i} ---")
                
                # Original
                orig_level = simplifier.calculate_flesch_kincaid_level(text)
                print(f"Original FK Level: {orig_level['fk_level']} ({orig_level['complexity']})")
                print(f"Original: {text}")
                
                # Simplified
                simplified = simplifier.simplify_text(text, max_length=100)
                simp_level = simplifier.calculate_flesch_kincaid_level(simplified)
                print(f"\nSimplified FK Level: {simp_level['fk_level']} ({simp_level['complexity']})")
                print(f"Simplified: {simplified}")
                
                improvement = orig_level['fk_level'] - simp_level['fk_level']
                print(f"Improvement: {improvement:.2f} levels")
                
        except Exception as e:
            print(f"Error testing {model}: {str(e)}")


def test_reading_levels():
    """Test Flesch-Kincaid calculation"""
    
    test_cases = {
        "easy": "The cat sat on the mat. It was warm.",
        "moderate": "The implementation of advanced strategies requires careful consideration of various factors.",
        "difficult": "The epistemological frameworks necessitate comprehensive reevaluation of contemporary paradigmatic structures."
    }
    
    print("\n" + "=" * 80)
    print("READING LEVEL ANALYSIS TEST")
    print("=" * 80)
    
    simplifier = TextSimplifier()
    
    for level, text in test_cases.items():
        result = simplifier.calculate_flesch_kincaid_level(text)
        print(f"\n{level.upper()}:")
        print(f"  Text: {text}")
        print(f"  FK Level: {result['fk_level']}")
        print(f"  Complexity: {result['complexity']}")


if __name__ == "__main__":
    print("Running Reading Aid Tests...\n")
    
    try:
        test_reading_levels()
    except Exception as e:
        print(f"Error in reading levels test: {str(e)}")
    
    try:
        test_simplification()
    except Exception as e:
        print(f"Error in simplification test: {str(e)}")
    
    print("\n" + "=" * 80)
    print("Tests completed!")
    print("=" * 80)
