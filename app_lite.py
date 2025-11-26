#!/usr/bin/env python3
"""
Minimal Reading Aid for Dyslexic People
Working version without heavy ML dependencies
Uses basic text processing and pyttsx3 for TTS
"""

import os
import sys
from pathlib import Path
from typing import Optional

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from modules.text_to_speech import TextToSpeech
from modules.ocr_extractor import OCRExtractor
import config

def extract_text_from_file(file_path: str) -> Optional[str]:
    """Extract text from PDF or image file"""
    try:
        extractor = OCRExtractor()
        
        if file_path.lower().endswith('.pdf'):
            text = extractor.extract_from_pdf(file_path)
        elif file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            text = extractor.extract_from_image(file_path)
        else:
            print(f"Unsupported file type: {file_path}")
            return None
            
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def simplify_text(text: str) -> str:
    """
    Simple text simplification (without ML models)
    Just breaks text into shorter sentences and paragraphs
    """
    # Split by sentences (basic approach)
    sentences = text.replace('. ', '.\n').replace('! ', '!\n').replace('? ', '?\n').split('\n')
    
    # Simplify by breaking long sentences
    simplified = []
    for sentence in sentences:
        if len(sentence.split()) > 20:
            # Split long sentences at commas or conjunctions
            parts = sentence.replace(', ', ',\n').replace(' and ', '\n and ').split('\n')
            simplified.extend([p.strip() for p in parts if p.strip()])
        else:
            simplified.append(sentence.strip())
    
    return '\n'.join(simplified)

def calculate_reading_level(text: str) -> dict:
    """Calculate Flesch-Kincaid reading level"""
    words = text.split()
    sentences = text.split('.')
    syllables = sum(count_syllables(word) for word in words)
    
    if len(words) == 0 or len(sentences) == 0:
        return {"level": "Unknown", "score": 0}
    
    # Flesch-Kincaid Grade Level
    grade = (0.39 * len(words) / len(sentences) + 
             11.8 * syllables / len(words) - 15.59)
    grade = max(0, grade)
    
    if grade < 6:
        level = "Easy"
    elif grade < 9:
        level = "Normal"
    elif grade < 13:
        level = "Advanced"
    else:
        level = "Very Advanced"
    
    return {"level": level, "score": round(grade, 1)}

def count_syllables(word: str) -> int:
    """Rough syllable counter"""
    word = word.lower()
    syllables = 0
    vowels = "aeiou"
    previous_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllables += 1
        previous_was_vowel = is_vowel
    
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le'):
        syllables += 1
    
    return max(1, syllables)

def main():
    """Main CLI interface"""
    print("=" * 60)
    print("Reading Aid for Dyslexic People - Lite Version")
    print("=" * 60)
    print("\nOptions:")
    print("1. Extract text from PDF/Image")
    print("2. Simplify text")
    print("3. Generate speech from text")
    print("4. Full pipeline (extract -> simplify -> speech)")
    print("5. Exit")
    
    while True:
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            file_path = input("Enter PDF/Image file path: ").strip()
            if os.path.exists(file_path):
                text = extract_text_from_file(file_path)
                if text:
                    print("\n--- Extracted Text ---")
                    print(text[:500] + "..." if len(text) > 500 else text)
                    print(f"\n[Total words: {len(text.split())}]")
            else:
                print("File not found!")
        
        elif choice == '2':
            text = input("Enter text to simplify (or 'previous' for last extracted): ").strip()
            if text:
                simplified = simplify_text(text)
                reading_level = calculate_reading_level(simplified)
                print("\n--- Simplified Text ---")
                print(simplified)
                print(f"\n[Reading Level: {reading_level['level']} (Grade {reading_level['score']})]")
        
        elif choice == '3':
            text = input("Enter text for speech: ").strip()
            if text:
                try:
                    tts = TextToSpeech()
                    print("\n[Generating speech...]")
                    tts.speak(text, rate=150)
                    print("[Done!]")
                except ImportError:
                    print("Error: pyttsx3 or dependencies not installed.")
                    print("Install with: pip install pyttsx3 comtypes")
                except Exception as e:
                    print(f"Error: {e}")
        
        elif choice == '4':
            file_path = input("Enter PDF/Image file path: ").strip()
            if os.path.exists(file_path):
                print("\n[Extracting text...]")
                text = extract_text_from_file(file_path)
                if text:
                    print("[Simplifying text...]")
                    simplified = simplify_text(text)
                    reading_level = calculate_reading_level(simplified)
                    print(f"\n--- Result ---")
                    print(f"Reading Level: {reading_level['level']} (Grade {reading_level['score']})")
                    print(f"\n--- Text Preview ---")
                    print(simplified[:300] + "...")
                    
                    speak = input("\nGenerate speech? (y/n): ").lower() == 'y'
                    if speak:
                        try:
                            tts = TextToSpeech()
                            print("[Generating speech...]")
                            tts.speak(simplified, rate=150)
                            print("[Done!]")
                        except Exception as e:
                            print(f"Error: {e}")
            else:
                print("File not found!")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
