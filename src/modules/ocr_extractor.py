"""
OCR and Text Extraction Module
Handles extraction of text from PDF and image files
"""

import pytesseract
from PIL import Image
try:
    import pypdfium2 as pdfium
except ImportError:
    pdfium = None
    
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
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
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
            
            # Clean text: replace newlines with spaces and strip
            text = text.replace('\n', ' ').strip()
            text = " ".join(text.split())
            
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
        if pdfium is None:
            raise ImportError("pypdfium2 is not installed. Please install it with 'pip install pypdfium2'")
            
        try:
            pdf = pdfium.PdfDocument(pdf_path)
            text_parts = []
            
            for i in range(len(pdf)):
                page = pdf[i]
                # Render page to image (scale=2.0 for better quality ~144dpi, scale=3.0 ~216dpi)
                bitmap = page.render(scale=3.0)
                pil_image = bitmap.to_pil()
                
                page_text = pytesseract.image_to_string(pil_image)
                
                # Clean text: replace newlines with spaces and strip
                cleaned_text = page_text.replace('\n', ' ').strip()
                if cleaned_text:
                    text_parts.append(cleaned_text)
                
                logger.info(f"Extracted text from page {i + 1}")
            
            # Join all parts with a single space and remove extra whitespace
            full_text = " ".join(text_parts)
            full_text = " ".join(full_text.split())
            
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
