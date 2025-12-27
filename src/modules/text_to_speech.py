"""
Text-to-Speech Module
Converts simplified text to speech for accessibility
"""

import pyttsx3
import logging
from pathlib import Path
import os
import torch
import torchaudio
import soundfile as sf
import numpy as np
from scipy import signal
import librosa

import time

# Global cache for Silero model to avoid reloading
_SILERO_CACHE = {
    "model": None,
    "device": None,
    "example_text": None
}


logger = logging.getLogger(__name__)

class TextToSpeech:
    """Convert text to speech using pyttsx3 or Silero TTS"""
    
    def __init__(self, rate: int = 150, volume: float = 1.0, voice_id: int = 0, engine_type: str = "standard"):
        """
        Initialize Text-to-Speech engine
        
        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
            voice_id: Voice ID 
                     - Standard: index of system voice
                     - Natural: index of speaker (en_0, en_1, etc.)
            engine_type: "standard" (pyttsx3) or "natural" (Silero)
        """
        self.engine_type = engine_type
        self.rate = rate
        self.volume = volume
        self.voice_id = voice_id
        
        if self.engine_type == "natural":
            self._init_silero()
        else:
            self._init_pyttsx3()

    def _init_pyttsx3(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', self.rate)
            self.engine.setProperty('volume', self.volume)
            
            voices = self.engine.getProperty('voices')
            if self.voice_id < len(voices):
                self.engine.setProperty('voice', voices[self.voice_id].id)
            
            logger.info(f"Standard TTS engine initialized with rate={self.rate}, volume={self.volume}")
        except Exception as e:
            logger.error(f"Failed to initialize pyttsx3: {e}")
            self.engine = None

    def _init_silero(self):
        try:
            logger.info("Initializing Silero TTS...")
            device = torch.device('cpu')
            
            # Load model from cache or download
            if _SILERO_CACHE["model"] is None:
                logger.info("Loading Silero model from hub...")
                # This will download the model on first run and cache it
                model, example_text = torch.hub.load(
                    repo_or_dir='snakers4/silero-models',
                    model='silero_tts',
                    language='en',
                    speaker='v3_en'
                )
                model.to(device)
                
                # Update cache
                _SILERO_CACHE["model"] = model
                _SILERO_CACHE["example_text"] = example_text
                _SILERO_CACHE["device"] = device
            else:
                logger.info("Using cached Silero model")
            
            self.model = _SILERO_CACHE["model"]
            self.example_text = _SILERO_CACHE["example_text"]
            self.device = _SILERO_CACHE["device"]

            
            # Map simple voice IDs to Silero speakers
            # v3_en speakers: 'en_0', 'en_1', ... 'en_117'
            # CORRECTED: en_0 is actually female, en_1 is actually male (reversed from initial assumption)
            # voice_id 0 = Male -> en_1, voice_id 1 = Female -> en_0
            speakers = ['en_1', 'en_0', 'en_10', 'en_11', 'en_12']  # Swapped en_0 and en_1
            self.speaker = speakers[self.voice_id % len(speakers)]
            
            logger.info(f"Natural TTS engine initialized completely. Speaker: {self.speaker}")
        except Exception as e:
            logger.error(f"Failed to initialize Silero TTS: {e}")
            self.model = None
            # Fallback to standard if natural fails
            self.engine_type = "standard"
            self._init_pyttsx3()

    def _apply_speed_change(self, audio_data: np.ndarray, sample_rate: int, speed_factor: float) -> np.ndarray:
        """
        Apply pitch-preserving speed change to audio using librosa's time stretching
        
        Args:
            audio_data: Audio samples as numpy array
            sample_rate: Original sample rate
            speed_factor: Speed multiplier (1.0 = normal, >1.0 = faster, <1.0 = slower)
        
        Returns:
            Speed-adjusted audio with preserved pitch
        """
        if speed_factor == 1.0:
            return audio_data
        
        # Use librosa's time_stretch for pitch-preserving speed change
        # Note: librosa.effects.time_stretch uses rate parameter where:
        # rate > 1.0 = faster (stretch less), rate < 1.0 = slower (stretch more)
        stretched_audio = librosa.effects.time_stretch(audio_data, rate=speed_factor)
        
        logger.info(f"Applied pitch-preserving time stretch: {speed_factor:.2f}x")
        
        return stretched_audio

    def save_to_file(self, text: str, output_path: str):
        """
        Save speech to an audio file
        """
        try:
            # Ensure output directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            if self.engine_type == "natural" and self.model:
                # Silero Generation
                sample_rate = 48000
                
                # Generate audio
                audio = self.model.apply_tts(text=text,
                                           speaker=self.speaker,
                                           sample_rate=sample_rate)
                
                # Convert to numpy for processing
                audio_np = audio.detach().cpu().numpy()
                
                # Apply speech rate control
                # Convert rate (words per minute) to speed factor
                # Normal speech is ~150 WPM, so we use that as baseline
                baseline_rate = 150
                speed_factor = self.rate / baseline_rate
                
                # Apply speed change if needed
                if speed_factor != 1.0:
                    audio_np = self._apply_speed_change(audio_np, sample_rate, speed_factor)
                    logger.info(f"Applied speed factor: {speed_factor:.2f}x (rate: {self.rate} WPM)")
                
                # Apply volume
                audio_np = audio_np * self.volume
                
                # Save
                # Use soundfile directly for robustness as torchaudio.save can be flaky on Windows
                sf.write(output_path, audio_np, sample_rate)
                logger.info(f"Natural speech saved to {output_path}")
                
            else:
                # Standard Generation
                if self.engine:
                    self.engine.save_to_file(text, output_path)
                    self.engine.runAndWait()
                    logger.info(f"Standard speech saved to {output_path}")
                else:
                    raise Exception("No TTS engine available")
                    
        except Exception as e:
            logger.error(f"Error saving speech to file: {str(e)}")
            raise

    def list_voices(self):
        """List available voices based on active engine"""
        if self.engine_type == "natural":
            # Updated to match corrected speaker mapping: voice_id 0=Male(en_1), 1=Female(en_0)
            return [
                {'id': 0, 'name': 'Natural Male (en_1)', 'gender': 'Male'},
                {'id': 1, 'name': 'Natural Female (en_0)', 'gender': 'Female'},
                {'id': 2, 'name': 'Natural Voice 3 (en_10)', 'gender': 'Unknown'},
                {'id': 3, 'name': 'Natural Voice 4 (en_11)', 'gender': 'Unknown'},
                {'id': 4, 'name': 'Natural Voice 5 (en_12)', 'gender': 'Unknown'}
            ]
        else:
            if not self.engine:
                return []
            voices = self.engine.getProperty('voices')
            voice_list = []
            for i, voice in enumerate(voices):
                voice_list.append({
                    'id': i,
                    'name': voice.name,
                    'gender': voice.gender if hasattr(voice, 'gender') else 'N/A'
                })
            return voice_list

