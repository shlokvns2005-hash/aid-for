
import pyttsx3

try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voice {i}: {voice.name} - ID: {voice.id}")
except Exception as e:
    print(f"Error: {e}")
