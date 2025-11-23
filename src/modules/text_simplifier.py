"""
Text Simplification Module
Simplifies complex text using T5-small and BART models
Implements FleschKincaid ease level based simplification
"""

from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
from transformers import BartForConditionalGeneration, BartTokenizer
import logging
from typing import List

logger = logging.getLogger(__name__)


class TextSimplifier:
    """Simplify text using various AI models"""
    
    def __init__(self, model_type: str = "t5"):
        """
        Initialize Text Simplifier
        
        Args:
            model_type: Type of model to use ("t5" or "bart")
        """
        self.model_type = model_type
        self._load_model()
    
    def _load_model(self):
        """Load the selected model and tokenizer"""
        try:
            if self.model_type == "t5":
                self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
                self.model = T5ForConditionalGeneration.from_pretrained("t5-small")
                logger.info("T5-small model loaded successfully")
            elif self.model_type == "bart":
                self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")
                self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")
                logger.info("BART model loaded successfully")
            else:
                raise ValueError(f"Unsupported model type: {self.model_type}")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def simplify_text(self, text: str, max_length: int = 100, num_beams: int = 4) -> str:
        """
        Simplify complex text using the loaded model
        
        Args:
            text: The text to simplify
            max_length: Maximum length of simplified text
            num_beams: Number of beams for beam search
            
        Returns:
            Simplified text
        """
        try:
            if self.model_type == "t5":
                input_text = f"simplify: {text}"
            else:  # BART
                input_text = text
            
            inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            
            summary_ids = self.model.generate(
                inputs,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True
            )
            
            simplified_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            logger.info("Text simplified successfully")
            return simplified_text
        except Exception as e:
            logger.error(f"Error simplifying text: {str(e)}")
            raise
    
    def simplify_sentences(self, sentences: List[str], max_length: int = 100) -> List[str]:
        """
        Simplify a list of sentences
        
        Args:
            sentences: List of sentences to simplify
            max_length: Maximum length of each simplified sentence
            
        Returns:
            List of simplified sentences
        """
        simplified = []
        for sentence in sentences:
            try:
                simple_sent = self.simplify_text(sentence, max_length)
                simplified.append(simple_sent)
            except Exception as e:
                logger.warning(f"Could not simplify sentence: {sentence}. Error: {str(e)}")
                simplified.append(sentence)  # Keep original if simplification fails
        
        return simplified
    
    def split_and_simplify(self, text: str, chunk_size: int = 100) -> str:
        """
        Split text into sentences and simplify each one
        
        Args:
            text: The text to process
            chunk_size: Approximate size of each chunk
            
        Returns:
            Simplified text with all sentences processed
        """
        # Split text into sentences (simple approach)
        sentences = [s.strip() + "." for s in text.replace("\n", " ").split(".") if s.strip()]
        
        simplified_sentences = self.simplify_sentences(sentences)
        simplified_text = " ".join(simplified_sentences)
        
        logger.info("Text split and simplified successfully")
        return simplified_text
    
    def calculate_flesch_kincaid_level(self, text: str) -> dict:
        """
        Calculate Flesch-Kincaid reading level
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary with reading level and complexity
        """
        words = text.split()
        sentences = [s for s in text.split(".") if s.strip()]
        
        if len(words) == 0 or len(sentences) == 0:
            return {"fk_level": 0, "complexity": "easy"}
        
        # Simplified Flesch-Kincaid formula
        fk_level = (0.39 * (len(words) / len(sentences))) + (11.8 * (sum(len(w) for w in words) / len(words) / 6)) - 15.59
        fk_level = max(0, fk_level)  # Ensure non-negative
        
        if fk_level <= 6:
            complexity = "easy"
        elif fk_level <= 9:
            complexity = "moderate"
        else:
            complexity = "difficult"
        
        return {
            "fk_level": round(fk_level, 2),
            "complexity": complexity
        }
