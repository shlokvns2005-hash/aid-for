"""
OCR and Text Extraction Module
Handles extraction of text from PDF and image files
"""

import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class OCRExtractor:
    """Extract text from images and PDFs using Tesseract OCR"""
    
    def __init__(self, tesseract_path=None):
        """
        Initialize OCR Extractor
        
        Args:
            tesseract_path: Path to tesseract executable (optional)
        """
        if tesseract_path:
            pytesseract.pytesseract.pytesseract_cmd = tesseract_path
    
    def extract_from_image(self, image_path: str) -> str:
        """
        Extract text from an image file
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Extracted text from the image
        """
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            logger.info(f"Successfully extracted text from {image_path}")
            return text
        except Exception as e:
            logger.error(f"Error extracting text from image: {str(e)}")
            raise
    
    def extract_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text from all pages of the PDF
        """
        try:
            images = convert_from_path(pdf_path, dpi=200)
            full_text = ""
            
            for page_num, image in enumerate(images):
                page_text = pytesseract.image_to_string(image)
                full_text += f"\n--- Page {page_num + 1} ---\n{page_text}"
                logger.info(f"Extracted text from page {page_num + 1}")
            
            logger.info(f"Successfully extracted text from {pdf_path}")
            return full_text
        except Exception as e:
            logger.error(f"Error extracting text from PDF: {str(e)}")
            raise
    
    def extract_text(self, file_path: str) -> str:
        """
        Automatically detect file type and extract text
        
        Args:
            file_path: Path to the file (PDF or image)
            
        Returns:
            Extracted text
        """
        file_extension = Path(file_path).suffix.lower()
        
        if file_extension == ".pdf":
            return self.extract_from_pdf(file_path)
        elif file_extension in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
            return self.extract_from_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
