import torchaudio
print(f"Torchaudio version: {torchaudio.__version__}")
try:
    print(f"Backends: {torchaudio.list_audio_backends()}")
except:
    print("list_audio_backends not found")

try:
    import soundfile
    print(f"Soundfile version: {soundfile.__version__}")
except ImportError:
    print("Soundfile not installed")
