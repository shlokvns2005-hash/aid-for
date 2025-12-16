"""
Test script for OCR and TTS functionality using mocks
"""

import unittest
from unittest.mock import MagicMock, patch, mock_open
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.ocr_extractor import OCRExtractor
from modules.text_to_speech import TextToSpeech

class TestOCRExtractor(unittest.TestCase):
    
    @patch('modules.ocr_extractor.pytesseract')
    @patch('modules.ocr_extractor.Image')
    def test_extract_from_image(self, mock_image, mock_pytesseract):
        """Test extraction from image"""
        # Setup mocks
        mock_pytesseract.image_to_string.return_value = "Mocked extracted text"
        mock_image.open.return_value = MagicMock()
        
        # Initialize
        ocr = OCRExtractor()
        
        # Test
        result = ocr.extract_from_image("dummy_image.jpg")
        
        # Verify
        self.assertEqual(result, "Mocked extracted text")
        mock_image.open.assert_called_with("dummy_image.jpg")
        mock_pytesseract.image_to_string.assert_called()

    @patch('modules.ocr_extractor.convert_from_path')
    @patch('modules.ocr_extractor.pytesseract')
    def test_extract_from_pdf(self, mock_pytesseract, mock_convert_from_path):
        """Test extraction from PDF"""
        # Setup mocks
        mock_page_image = MagicMock()
        mock_convert_from_path.return_value = [mock_page_image, mock_page_image] # 2 pages
        mock_pytesseract.image_to_string.side_effect = ["Page 1 text", "Page 2 text"]
        
        # Initialize
        ocr = OCRExtractor()
        
        # Test
        result = ocr.extract_from_pdf("dummy.pdf")
        
        # Verify
        self.assertIn("Page 1 text", result)
        self.assertIn("Page 2 text", result)
        self.assertIn("--- Page 1 ---", result)
        self.assertIn("--- Page 2 ---", result)
        mock_convert_from_path.assert_called_with("dummy.pdf", dpi=200)

class TestTextToSpeech(unittest.TestCase):
    
    @patch('modules.text_to_speech.pyttsx3')
    def test_init(self, mock_pyttsx3):
        """Test initialization"""
        mock_engine = MagicMock()
        mock_pyttsx3.init.return_value = mock_engine
        mock_engine.getProperty.return_value = [] # No voices for simplicity
        
        tts = TextToSpeech(rate=150, volume=0.8)
        
        mock_engine.setProperty.assert_any_call('rate', 150)
        mock_engine.setProperty.assert_any_call('volume', 0.8)
        
    @patch('modules.text_to_speech.pyttsx3')
    def test_speak(self, mock_pyttsx3):
        """Test speak method"""
        mock_engine = MagicMock()
        mock_pyttsx3.init.return_value = mock_engine
        mock_engine.getProperty.return_value = []
        
        tts = TextToSpeech()
        tts.speak("Hello world")
        
        mock_engine.say.assert_called_with("Hello world")
        mock_engine.runAndWait.assert_called()

    @patch('modules.text_to_speech.pyttsx3')
    def test_save_to_file(self, mock_pyttsx3):
        """Test save to file"""
        mock_engine = MagicMock()
        mock_pyttsx3.init.return_value = mock_engine
        mock_engine.getProperty.return_value = []
        
        tts = TextToSpeech()
        
        # Mock Path.mkdir to avoid actual filesystem creation
        with patch('pathlib.Path.mkdir'):
            tts.save_to_file("Hello world", "output/test.mp3")
        
        mock_engine.save_to_file.assert_called_with("Hello world", "output/test.mp3")
        mock_engine.runAndWait.assert_called()

if __name__ == '__main__':
    unittest.main()
