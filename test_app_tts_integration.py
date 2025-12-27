import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.text_to_speech import TextToSpeech
import time

def test_integration():
    print("Testing TextToSpeech integration...")
    try:
        # Initialize
        tts = TextToSpeech(engine_type="natural")
        
        # Generte
        text = "This is a test of the integrated text to speech module."
        output_path = "test_integration.mp3"
        
        tts.save_to_file(text, output_path)
        
        if os.path.exists(output_path):
            print(f"SUCCESS: Audio generated at {output_path}")
            # os.remove(output_path)
        else:
            print("FAILURE: Output file not found")
            
    except Exception as e:
        print(f"FAILURE: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_integration()
