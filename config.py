"""
Advanced Configuration and Settings
Customize behavior, model parameters, and performance settings
"""

import os
from pathlib import Path

# ============================================================================
# DIRECTORY CONFIGURATION
# ============================================================================
BASE_DIR = Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "output"
MODELS_CACHE_DIR = os.path.expanduser("~/.cache/huggingface/")

# Create directories if they don't exist
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================================================
# OCR CONFIGURATION
# ============================================================================
OCR_CONFIG = {
    # Tesseract path (set to None for automatic detection)
    "tesseract_path": None,  # Windows: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    # PDF conversion DPI (higher = better quality but slower)
    "pdf_dpi": 200,
    
    # Language for OCR (ISO 639-1 codes)
    "languages": ["eng"],  # "eng", "fra", "deu", etc.
}

# ============================================================================
# TEXT SIMPLIFICATION CONFIGURATION
# ============================================================================
SIMPLIFICATION_CONFIG = {
    # Default model: "t5" or "bart"
    "default_model": "t5",
    
    # T5 configuration
    "t5": {
        "model_name": "t5-small",
        "max_length": 100,
        "num_beams": 4,
        "early_stopping": True,
        "temperature": 0.7,
        "top_p": 0.95,
    },
    
    # BART configuration
    "bart": {
        "model_name": "facebook/bart-base",
        "max_length": 100,
        "num_beams": 4,
        "early_stopping": True,
        "temperature": 0.7,
        "top_p": 0.95,
    },
    
    # Chunk size for processing large texts
    "chunk_size": 512,
    
    # Target reading levels
    "reading_levels": {
        "easy": {"min": 0, "max": 6},
        "moderate": {"min": 6, "max": 9},
        "difficult": {"min": 9, "max": 18},
    }
}

# ============================================================================
# TEXT-TO-SPEECH CONFIGURATION
# ============================================================================
TTS_CONFIG = {
    # Default speech rate (words per minute)
    "default_rate": 150,
    "min_rate": 50,
    "max_rate": 300,
    
    # Default volume (0.0 to 1.0)
    "default_volume": 1.0,
    "min_volume": 0.0,
    "max_volume": 1.0,
    
    # Available voices
    "voices": {
        "male": 0,
        "female": 1,
    },
    
    # Audio output format
    "audio_format": "mp3",
    "audio_bit_rate": "192k",
}

# ============================================================================
# STREAMLIT CONFIGURATION
# ============================================================================
STREAMLIT_CONFIG = {
    "page_title": "Reading Aid for Dyslexic People",
    "page_icon": "📖",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "max_upload_size": 500,  # MB
}

# ============================================================================
# PERFORMANCE CONFIGURATION
# ============================================================================
PERFORMANCE_CONFIG = {
    # Model caching
    "use_cache": True,
    "cache_dir": MODELS_CACHE_DIR,
    
    # Processing optimization
    "batch_size": 1,
    "num_workers": 0,
    
    # Memory management
    "offload_to_cpu": False,
    "use_fp16": False,  # Half precision (faster but less accurate)
    
    # Logging
    "log_level": "INFO",
    "log_file": BASE_DIR / "logs" / "app.log",
}

# ============================================================================
# FEATURE FLAGS
# ============================================================================
FEATURES = {
    "enable_ocr": True,
    "enable_simplification": True,
    "enable_tts": True,
    "enable_analysis": True,
    "enable_download": True,
    "enable_audio_save": True,
}

# ============================================================================
# ACCESSIBILITY CONFIGURATION
# ============================================================================
ACCESSIBILITY = {
    # Font sizes
    "font_size_base": 16,
    "font_size_h1": 36,
    "font_size_h2": 28,
    "font_size_h3": 24,
    
    # Colors (accessible color scheme)
    "primary_color": "#1f77b4",
    "background_color": "#ffffff",
    "secondary_background": "#f0f2f6",
    "text_color": "#262730",
    
    # High contrast mode
    "high_contrast": False,
    "dyslexia_friendly_font": True,
}

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================
ADVANCED = {
    # Sentence splitting strategy
    "sentence_split_method": "punkt",  # "punkt", "regex", "spacy"
    
    # Lemmatization
    "use_lemmatization": False,
    
    # Stop words removal
    "remove_stop_words": False,
    
    # Entity preservation (keep proper nouns)
    "preserve_entities": True,
    
    # Technical term preservation
    "preserve_technical_terms": True,
    
    # Maximum text length for processing
    "max_text_length": 100000,  # characters
}

# ============================================================================
# API & SERVICES (for future cloud integration)
# ============================================================================
SERVICES = {
    "use_local_models": True,  # Set to False to use cloud APIs
    "huggingface_api_key": os.getenv("HUGGINGFACE_API_KEY", ""),
    "timeout": 30,  # seconds
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_config(section: str) -> dict:
    """Get configuration section"""
    config_map = {
        "ocr": OCR_CONFIG,
        "simplification": SIMPLIFICATION_CONFIG,
        "tts": TTS_CONFIG,
        "streamlit": STREAMLIT_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "features": FEATURES,
        "accessibility": ACCESSIBILITY,
        "advanced": ADVANCED,
        "services": SERVICES,
    }
    return config_map.get(section, {})


def update_config(section: str, **kwargs):
    """Update configuration section"""
    config_map = {
        "ocr": OCR_CONFIG,
        "simplification": SIMPLIFICATION_CONFIG,
        "tts": TTS_CONFIG,
        "streamlit": STREAMLIT_CONFIG,
        "performance": PERFORMANCE_CONFIG,
        "features": FEATURES,
        "accessibility": ACCESSIBILITY,
        "advanced": ADVANCED,
        "services": SERVICES,
    }
    if section in config_map:
        config_map[section].update(kwargs)


def print_config():
    """Print all configurations"""
    configs = {
        "OCR": OCR_CONFIG,
        "SIMPLIFICATION": SIMPLIFICATION_CONFIG,
        "TTS": TTS_CONFIG,
        "STREAMLIT": STREAMLIT_CONFIG,
        "PERFORMANCE": PERFORMANCE_CONFIG,
        "FEATURES": FEATURES,
        "ACCESSIBILITY": ACCESSIBILITY,
        "ADVANCED": ADVANCED,
        "SERVICES": SERVICES,
    }
    
    for name, config in configs.items():
        print(f"\n{name}:")
        print("-" * 50)
        for key, value in config.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    print_config()
