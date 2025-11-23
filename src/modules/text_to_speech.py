"""
Text-to-Speech Module
Converts simplified text to speech for accessibility
"""

import pyttsx3
import logging
from pathlib import Path
import os

logger = logging.getLogger(__name__)


class TextToSpeech:
    """Convert text to speech using pyttsx3"""
    
    def __init__(self, rate: int = 150, volume: float = 1.0, voice_id: int = 0):
        """
        Initialize Text-to-Speech engine
        
        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
            voice_id: Voice ID (0 for male, 1 for female, etc.)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        voices = self.engine.getProperty('voices')
        if voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)
        
        logger.info(f"Text-to-Speech engine initialized with rate={rate}, volume={volume}")
    
    def speak(self, text: str):
        """
        Speak the given text
        
        Args:
            text: The text to speak
        """
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            logger.info("Text spoken successfully")
        except Exception as e:
            logger.error(f"Error during speech: {str(e)}")
            raise
    
    def save_to_file(self, text: str, output_path: str):
        """
        Save speech to an audio file
        
        Args:
            text: The text to convert to speech
            output_path: Path where the audio file will be saved
        """
        try:
            # Ensure output directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            self.engine.save_to_file(text, output_path)
            self.engine.runAndWait()
            logger.info(f"Speech saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving speech to file: {str(e)}")
            raise
    
    def set_rate(self, rate: int):
        """
        Set speech rate
        
        Args:
            rate: Speech rate in words per minute (default is around 200)
        """
        self.engine.setProperty('rate', rate)
        logger.info(f"Speech rate set to {rate}")
    
    def set_volume(self, volume: float):
        """
        Set volume level
        
        Args:
            volume: Volume level (0.0 to 1.0)
        """
        self.engine.setProperty('volume', min(1.0, max(0.0, volume)))
        logger.info(f"Volume set to {volume}")
    
    def list_voices(self):
        """
        List available voices
        
        Returns:
            List of available voices
        """
        voices = self.engine.getProperty('voices')
        voice_list = []
        for i, voice in enumerate(voices):
            voice_list.append({
                'id': i,
                'name': voice.name,
                'gender': voice.gender if hasattr(voice, 'gender') else 'N/A'
            })
        return voice_list
    
    def set_voice(self, voice_id: int):
        """
        Set the voice to use
        
        Args:
            voice_id: ID of the voice to use
        """
        voices = self.engine.getProperty('voices')
        if voice_id < len(voices):
            self.engine.setProperty('voice', voices[voice_id].id)
            logger.info(f"Voice set to {voices[voice_id].name}")
        else:
            logger.warning(f"Voice ID {voice_id} not found")
