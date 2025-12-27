
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path("d:/aid-for/src")))

from modules.text_to_speech import TextToSpeech
import os

def test_standard():
    print("Testing Standard TextToSpeech (pyttsx3)...")
    try:
        tts = TextToSpeech(engine_type="standard")
        if tts.engine is None:
            print("FAILURE: Engine is None. Initialization failed.")
            return

        text = "This is a test of the standard text to speech module."
        output_path = "test_standard.mp3"
        
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
    test_standard()
