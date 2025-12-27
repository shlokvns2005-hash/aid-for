
import sys
from pathlib import Path
import time
import shutil

# Add src to path
sys.path.insert(0, str(Path("d:/aid-for/src")))

from modules.text_to_speech import TextToSpeech

def test_caching():
    print("Testing TTS Model Caching...")
    
    # First initialization
    print("\n--- First Initialization ---")
    start_time = time.time()
    tts1 = TextToSpeech(engine_type="natural")
    duration1 = time.time() - start_time
    print(f"First initialization took: {duration1:.4f} seconds")
    
    # Second initialization
    print("\n--- Second Initialization ---")
    start_time = time.time()
    tts2 = TextToSpeech(engine_type="natural")
    duration2 = time.time() - start_time
    print(f"Second initialization took: {duration2:.4f} seconds")
    
    # Check if they share the same model object
    if tts1.model is tts2.model:
        print("\nSUCCESS: Model is shared (Cached)!")
    else:
        print("\nFAILURE: Models are different objects!")

    # Verify generation works for both
    output_path = "test_cache_output.mp3"
    try:
        tts2.save_to_file("Testing cached model generation.", output_path)
        print("Generation successful with cached model.")
    except Exception as e:
        print(f"Generation failed: {e}")

if __name__ == "__main__":
    test_caching()
