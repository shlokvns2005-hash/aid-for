"""
Text Simplification Module
Simplifies complex text using rule-based and optional AI models
Implements FleschKincaid ease level based simplification
"""

import logging
from typing import List
import re

logger = logging.getLogger(__name__)

# Try to import transformers, but make it optional
try:
    from transformers import T5Tokenizer, T5ForConditionalGeneration
    from transformers import BartForConditionalGeneration, BartTokenizer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False


class TextSimplifier:
    """Simplify text using rule-based and optional AI models"""
    
    def __init__(self, model_type: str = "basic"):
        """
        Initialize Text Simplifier
        
        Args:
            model_type: Type of model to use ("basic", "t5", or "bart")
                       Falls back to "basic" if transformers not available
        """
        self.model_type = model_type
        self.model = None
        self.tokenizer = None
        
        if model_type != "basic":
            self._load_model()
    
    def _load_model(self):
        """Load the selected AI model and tokenizer"""
        if not HAS_TRANSFORMERS:
            logger.warning(f"Transformers not available, using basic simplification instead")
            self.model_type = "basic"
            return
            
        try:
            if self.model_type == "t5":
                self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
                self.model = T5ForConditionalGeneration.from_pretrained("t5-small")
                logger.info("T5-small model loaded successfully")
            elif self.model_type == "bart":
                # Use a distilled BART model fine-tuned for summarization
                # This is much better than raw bart-base for simplification
                model_name = "sshleifer/distilbart-cnn-12-6"
                self.tokenizer = BartTokenizer.from_pretrained(model_name)
                self.model = BartForConditionalGeneration.from_pretrained(model_name)
                logger.info(f"BART model ({model_name}) loaded successfully")
            else:
                logger.warning(f"Unsupported model type: {self.model_type}, using basic")
                self.model_type = "basic"
        except Exception as e:
            logger.warning(f"Error loading AI model ({e}), falling back to basic simplification")
            self.model_type = "basic"
    
    def simplify_text(self, text: str, max_length: int = 100, num_beams: int = 4) -> str:
        """
        Simplify complex text using the loaded model or basic rules
        
        Args:
            text: The text to simplify
            max_length: Maximum length of simplified text
            num_beams: Number of beams for beam search (ignored for basic mode)
            
        Returns:
            Simplified text
        """
        try:
            if self.model_type == "basic":
                return self._simplify_basic(text)
            
            if self.model_type == "t5":
                # T5 uses "summarize: " prefix for summarization/simplification
                input_text = f"summarize: {text}"
            else:  # BART
                # BART models don't need a prefix, but we need a model fine-tuned for summarization
                input_text = text
            
            inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            
            summary_ids = self.model.generate(
                inputs,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True
            )
            
            simplified_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
            
            # Debug: Write to file and print
            debug_file = "bart_debug.txt"
            with open(debug_file, "a", encoding="utf-8") as f:
                f.write(f"\n{'='*80}\n")
                f.write(f"BART Debug Output - {__import__('datetime').datetime.now()}\n")
                f.write(f"{'='*80}\n")
                f.write(f"Raw BART output length: {len(simplified_text)} chars\n")
                f.write(f"Raw BART output:\n{simplified_text}\n")
                f.write(f"\n")
            
            # Check for input duplication using fuzzy matching
            # BART sometimes repeats the input text before generating the summary
            from difflib import SequenceMatcher
            
            # Use stripped text for comparison
            clean_text = text.strip()
            
            matcher = SequenceMatcher(None, clean_text, simplified_text)
            match = matcher.find_longest_match(0, len(clean_text), 0, len(simplified_text))
            
            # If match starts at beginning of both strings and covers > 90% of input
            if match.a == 0 and match.b == 0 and match.size / len(clean_text) > 0.9:
                # Check if there is significant content after the duplication
                if len(simplified_text) > match.size + 10:
                    logger.info(f"Detected input duplication (coverage: {match.size / len(text):.2f}). Removing it.")
                    simplified_text = simplified_text[match.size:].strip()
                    
                    # Remove leading punctuation that might be left over (like " .")
                    import string
                    simplified_text = simplified_text.lstrip(string.punctuation + string.whitespace)
                    
                    with open(debug_file, "a", encoding="utf-8") as f:
                        f.write(f"✓ Removed duplication. New output:\n{simplified_text}\n")
            
            # Additional check: if the simplified text is very similar to input, it might be a failed simplification
            if len(simplified_text.strip()) == 0:
                logger.warning("Model returned empty output, using basic simplification")
                return self._simplify_basic(text)
            
            with open(debug_file, "a", encoding="utf-8") as f:
                f.write(f"\nFinal simplified text:\n{simplified_text}\n")
                f.write(f"{'='*80}\n\n")
            
            logger.info("Text simplified successfully")
            return simplified_text
        except Exception as e:
            logger.warning(f"Error simplifying text with AI model: {str(e)}, using basic simplification")
            return self._simplify_basic(text)
    
    def _simplify_basic(self, text: str) -> str:
        """Basic rule-based text simplification"""
        # Break into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        simplified = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            # Remove very long clauses
            if len(sentence.split()) > 20:
                # Try to split at conjunctions
                parts = re.split(r'\s+(and|but|or|because)\s+', sentence)
                simplified.extend([p.strip() for p in parts if p.strip() and p not in ['and', 'but', 'or', 'because']])
            else:
                simplified.append(sentence)
        
        return ' '.join(simplified)
    
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
                logger.warning(f"Could not simplify sentence. Using basic simplification.")
                simplified.append(self._simplify_basic(sentence))
        
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
