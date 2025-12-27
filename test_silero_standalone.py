import torch
import os
import time

def verify_silero():
    print("Verifying Silero TTS...")
    
    try:
        import torchaudio
        import omegaconf
        print("Dependencies imported successfully.")
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return

    try:
        # Debug backends
        print(f"Torchaudio version: {torchaudio.__version__}")
        # util availability check for older versions or backend info
        if hasattr(torchaudio, "list_audio_backends"):
             print(f"Available backends: {torchaudio.list_audio_backends()}")
        
        # Try forcing soundfile if possible/needed (deprecated but might help confirm)
        # torchaudio.set_audio_backend("soundfile") 
        
        device = torch.device('cpu')
        print(f"Using device: {device}")
        
        print("Loading Silero model (this may take time on first run)...")
        start_time = time.time()
        
        # Explicitly reload to verify it works
        model, example_text = torch.hub.load(
            repo_or_dir='snakers4/silero-models',
            model='silero_tts',
            language='en',
            speaker='v3_en',
            trust_repo=True
        )
        model.to(device)
        print(f"Model loaded in {time.time() - start_time:.2f} seconds.")
        
        print("Generating test audio...")
        sample_rate = 48000
        speaker = 'en_0'
        
        audio = model.apply_tts(text="Hello, this is a test of the offline natural text to speech.",
                               speaker=speaker,
                               sample_rate=sample_rate)
        
        output_path = "test_silero.wav"
        # torchaudio.save(output_path, audio.unsqueeze(0), sample_rate, backend="soundfile")
        
        # Use soundfile directly for robustness
        import soundfile as sf
        # audio is [1, T] or [T], need to check shape usually Silero returns [T]
        # Silero apply_tts returns 1D tensor usually.
        # soundfile expects [T] or [T, C]
        audio_np = audio.detach().cpu().numpy()
        sf.write(output_path, audio_np, sample_rate)
        
        print(f"Audio saved to {output_path}")
        
        # Cleanup
        if os.path.exists(output_path):
            os.remove(output_path)
            print("Cleanup successful.")
            
        print("VERIFICATION SUCCESSFUL")
        
    except Exception as e:
        print(f"VERIFICATION FAILED: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_silero()
