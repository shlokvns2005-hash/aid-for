"""
Test speech rate control for Natural TTS
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_to_speech import TextToSpeech

def test_speech_rates():
    """Test different speech rates with Natural TTS"""
    
    test_text = "This is a test of the speech rate control feature. The quick brown fox jumps over the lazy dog."
    
    rates = [75, 150, 225]  # Slow, Normal, Fast
    
    for rate in rates:
        print(f"\n{'='*60}")
        print(f"Testing Natural TTS at {rate} WPM...")
        print(f"{'='*60}")
        
        try:
            # Initialize with Natural TTS
            tts = TextToSpeech(
                rate=rate,
                volume=1.0,
                voice_id=0,  # Male voice
                engine_type="natural"
            )
            
            # Generate audio
            output_file = f"output/test_rate_{rate}wpm.mp3"
            Path("output").mkdir(exist_ok=True)
            
            print(f"Generating audio at {rate} WPM...")
            tts.save_to_file(test_text, output_file)
            
            print(f"✅ Successfully generated: {output_file}")
            print(f"   Speed factor: {rate/150:.2f}x")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print("Test complete! Check the output folder for generated files.")
    print("Compare the three files to hear the speed differences.")
    print(f"{'='*60}")

if __name__ == "__main__":
    test_speech_rates()
