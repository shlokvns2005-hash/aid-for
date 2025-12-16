"""
Test script with highly complex sentences to verify simplification quality.
"""
import sys
from pathlib import Path
import logging

# Configure logging to see what's happening
logging.basicConfig(level=logging.INFO)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_simplifier import TextSimplifier

def test_complex_simplification():
    complex_sentences = [
        # Legal
        "The aforementioned party shall be held accountable and liable for any and all damages, losses, or injuries resulting from the breach of contract, negligence, or willful misconduct, including but not limited to consequential damages, punitive damages, and attorney fees, as stipulated in the contractual agreement executed on the date hereinabove mentioned.",
        
        # Medical
        "Hypertension, characterized by persistently elevated arterial blood pressure exceeding 140/90 mmHg, represents a significant cardiovascular risk factor that can lead to myocardial infarction, cerebrovascular accidents, and chronic kidney disease if left untreated, necessitating pharmacological interventions typically including angiotensin-converting enzyme inhibitors.",
        
        # Academic/Scientific
        "The phenomenon of photosynthesis is an extraordinarily complex biochemical process whereby plants convert light energy into chemical energy stored in glucose molecules, involving the absorption of photons by chlorophyll pigments and the subsequent generation of ATP and NADPH in the light-dependent reactions.",
        
        # Archaic/Literary
        "Whosoever shall be found guilty of such malfeasance shall forthwith be subject to the most severe penalties prescribed by the statutes of the realm, notwithstanding any prior claims of immunity or privilege that may have been accorded to them by virtue of their station."
    ]

    print("="*80)
    print("TESTING COMPLEX SENTENCE SIMPLIFICATION")
    print("="*80)

    models = ["t5", "bart"]
    
    for model_type in models:
        print(f"\n\nTesting Model: {model_type.upper()}")
        print("-" * 40)
        
        try:
            simplifier = TextSimplifier(model_type=model_type)
            
            for i, text in enumerate(complex_sentences, 1):
                print(f"\nInput {i} (Length: {len(text)}):")
                print(f"'{text}'")
                
                try:
                    simplified = simplifier.simplify_text(text, max_length=100)
                    print(f"\nOutput {i} (Length: {len(simplified)}):")
                    print(f"'{simplified}'")
                    
                    if simplified.strip() == text.strip():
                        print("⚠️  WARNING: Output is identical to input (No simplification)")
                    else:
                        print("✅ Output changed")
                        
                except Exception as e:
                    print(f"❌ Error simplifying text: {e}")
                    
        except Exception as e:
            print(f"❌ Error loading model {model_type}: {e}")

if __name__ == "__main__":
    test_complex_simplification()
