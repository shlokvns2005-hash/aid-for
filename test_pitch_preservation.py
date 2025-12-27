"""
Test script to verify pitch-preserving time-stretching in Natural HQ TTS
Generates audio at different speech rates to confirm pitch remains constant
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_to_speech import TextToSpeech
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_pitch_preservation():
    """Test that pitch remains constant across different speech rates"""
    
    test_text = "Hello, this is a test of the pitch-preserving time-stretching algorithm. The pitch should remain constant regardless of the speech rate."
    
    # Test different speech rates
    test_rates = [
        (50, "slow"),
        (150, "normal"),
        (300, "fast")
    ]
    
    # Test both genders
    test_voices = [
        (0, "male"),
        (1, "female")
    ]
    
    output_dir = Path("output") / "pitch_test"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "="*60)
    print("Testing Pitch-Preserving Time-Stretching")
    print("="*60 + "\n")
    
    for voice_id, gender in test_voices:
        print(f"\n--- Testing {gender.upper()} voice (voice_id={voice_id}) ---\n")
        
        for rate, speed_label in test_rates:
            print(f"Generating audio at {rate} WPM ({speed_label})...")
            
            try:
                # Initialize TTS with Natural engine
                tts = TextToSpeech(
                    rate=rate,
                    volume=1.0,
                    voice_id=voice_id,
                    engine_type="natural"
                )
                
                # Generate audio
                output_path = output_dir / f"{gender}_{speed_label}_{rate}wpm.mp3"
                tts.save_to_file(test_text, str(output_path))
                
                print(f"✅ Saved to: {output_path}")
                
            except Exception as e:
                print(f"❌ Error: {e}")
                import traceback
                traceback.print_exc()
    
    print("\n" + "="*60)
    print("Test Complete!")
    print("="*60)
    print(f"\nAudio files saved to: {output_dir}")
    print("\nPlease listen to the files and verify:")
    print("1. Speed changes across files (slow/normal/fast)")
    print("2. Pitch remains CONSTANT for each gender")
    print("3. No 'chipmunk' effect at high speeds")
    print("4. No 'deep voice' effect at low speeds")
    print("\n")

if __name__ == "__main__":
    test_pitch_preservation()
