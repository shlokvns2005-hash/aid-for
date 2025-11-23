"""
Example usage and integration patterns for Reading Aid application
"""

# ============================================================================
# EXAMPLE 1: Basic OCR Usage
# ============================================================================

def example_ocr():
    """Basic OCR extraction example"""
    from src.modules.ocr_extractor import OCRExtractor
    
    # Initialize OCR
    ocr = OCRExtractor()
    
    # Extract from PDF
    pdf_text = ocr.extract_from_pdf("sample.pdf")
    print("Extracted text from PDF:")
    print(pdf_text[:200] + "...")
    
    # Extract from image
    image_text = ocr.extract_from_image("sample.jpg")
    print("Extracted text from image:")
    print(image_text[:200] + "...")


# ============================================================================
# EXAMPLE 2: Text Simplification
# ============================================================================

def example_simplification():
    """Text simplification with both models"""
    from src.modules.text_simplifier import TextSimplifier
    
    complex_text = """
    The ubiquitous integration of artificial intelligence into contemporary 
    technological paradigms necessitates comprehensive reevaluation of 
    epistemological frameworks and methodological approaches.
    """
    
    # Using T5
    print("=== T5-Small Model ===")
    t5_simplifier = TextSimplifier(model_type="t5")
    t5_simple = t5_simplifier.simplify_text(complex_text)
    print(f"Original: {complex_text}")
    print(f"Simplified: {t5_simple}")
    
    # Using BART
    print("\n=== BART Model ===")
    bart_simplifier = TextSimplifier(model_type="bart")
    bart_simple = bart_simplifier.simplify_text(complex_text)
    print(f"Simplified: {bart_simple}")
    
    # Reading level analysis
    print("\n=== Reading Level Analysis ===")
    orig_level = t5_simplifier.calculate_flesch_kincaid_level(complex_text)
    simp_level = t5_simplifier.calculate_flesch_kincaid_level(t5_simple)
    
    print(f"Original FK Level: {orig_level['fk_level']} ({orig_level['complexity']})")
    print(f"Simplified FK Level: {simp_level['fk_level']} ({simp_level['complexity']})")


# ============================================================================
# EXAMPLE 3: Text-to-Speech
# ============================================================================

def example_tts():
    """Text-to-speech examples"""
    from src.modules.text_to_speech import TextToSpeech
    from pathlib import Path
    
    text = "Reading aid helps students with dyslexia understand complex texts."
    
    # Create output directory
    Path("output").mkdir(exist_ok=True)
    
    # Basic speech
    print("=== Playing Audio ===")
    tts = TextToSpeech(rate=150, volume=1.0)
    tts.speak(text)
    
    # Save to file
    print("=== Saving to File ===")
    tts.save_to_file(text, "output/sample_audio.mp3")
    print("Audio saved to output/sample_audio.mp3")
    
    # Adjust settings
    print("=== Custom Voice Settings ===")
    tts.set_rate(120)  # Slower
    tts.set_volume(0.8)
    tts.set_voice(1)  # Female voice
    tts.speak("This is slower speech with female voice.")
    
    # List available voices
    print("=== Available Voices ===")
    voices = tts.list_voices()
    for voice in voices:
        print(f"  {voice['id']}: {voice['name']} ({voice['gender']})")


# ============================================================================
# EXAMPLE 4: Complete Pipeline
# ============================================================================

def example_complete_pipeline():
    """Complete end-to-end pipeline"""
    from src.modules.ocr_extractor import OCRExtractor
    from src.modules.text_simplifier import TextSimplifier
    from src.modules.text_to_speech import TextToSpeech
    from pathlib import Path
    
    # Create output directory
    Path("output").mkdir(exist_ok=True)
    
    # Step 1: Extract text from PDF
    print("Step 1: Extracting text from PDF...")
    ocr = OCRExtractor()
    extracted_text = ocr.extract_from_pdf("document.pdf")
    print(f"Extracted {len(extracted_text)} characters")
    
    # Step 2: Simplify the text
    print("\nStep 2: Simplifying text...")
    simplifier = TextSimplifier(model_type="t5")
    simplified_text = simplifier.simplify_text(extracted_text, max_length=150)
    
    # Step 3: Analyze reading levels
    print("\nStep 3: Analyzing reading levels...")
    orig_level = simplifier.calculate_flesch_kincaid_level(extracted_text)
    simp_level = simplifier.calculate_flesch_kincaid_level(simplified_text)
    
    print(f"Original FK Level: {orig_level['fk_level']} ({orig_level['complexity']})")
    print(f"Simplified FK Level: {simp_level['fk_level']} ({simp_level['complexity']})")
    improvement = orig_level['fk_level'] - simp_level['fk_level']
    print(f"Improvement: {improvement:.2f} levels")
    
    # Step 4: Convert to speech
    print("\nStep 4: Converting to speech...")
    tts = TextToSpeech(rate=150, volume=1.0, voice_id=1)  # Female voice
    tts.save_to_file(simplified_text, "output/simplified_audio.mp3")
    print("Audio saved to output/simplified_audio.mp3")
    
    # Step 5: Save simplified text
    print("\nStep 5: Saving outputs...")
    with open("output/simplified_text.txt", "w") as f:
        f.write(simplified_text)
    print("Simplified text saved to output/simplified_text.txt")
    
    print("\n✅ Pipeline completed successfully!")


# ============================================================================
# EXAMPLE 5: Batch Processing
# ============================================================================

def example_batch_processing():
    """Process multiple files in batch"""
    from src.modules.ocr_extractor import OCRExtractor
    from src.modules.text_simplifier import TextSimplifier
    from pathlib import Path
    
    # Get all PDF files
    pdf_files = list(Path("uploads").glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files to process")
    
    ocr = OCRExtractor()
    simplifier = TextSimplifier(model_type="t5")
    
    results = []
    
    for pdf_file in pdf_files:
        print(f"\nProcessing {pdf_file.name}...")
        
        # Extract text
        text = ocr.extract_from_pdf(str(pdf_file))
        
        # Simplify
        simple_text = simplifier.simplify_text(text, max_length=100)
        
        # Calculate metrics
        orig_level = simplifier.calculate_flesch_kincaid_level(text)
        simp_level = simplifier.calculate_flesch_kincaid_level(simple_text)
        
        results.append({
            'filename': pdf_file.name,
            'original_level': orig_level['fk_level'],
            'simplified_level': simp_level['fk_level'],
            'improvement': orig_level['fk_level'] - simp_level['fk_level'],
            'original_words': len(text.split()),
            'simplified_words': len(simple_text.split()),
        })
        
        print(f"  ✓ FK Level: {orig_level['fk_level']} → {simp_level['fk_level']}")
    
    # Print summary
    print("\n" + "="*50)
    print("BATCH PROCESSING SUMMARY")
    print("="*50)
    for result in results:
        print(f"\n{result['filename']}:")
        print(f"  Reading Level: {result['original_level']:.2f} → {result['simplified_level']:.2f}")
        print(f"  Improvement: {result['improvement']:.2f} levels")
        print(f"  Words: {result['original_words']} → {result['simplified_words']}")


# ============================================================================
# EXAMPLE 6: Custom Configuration
# ============================================================================

def example_custom_config():
    """Using custom configuration"""
    from config import update_config, get_config
    from src.modules.text_simplifier import TextSimplifier
    from src.modules.text_to_speech import TextToSpeech
    
    # Update configuration
    update_config(
        "simplification",
        default_model="bart",
        chunk_size=256
    )
    
    update_config(
        "tts",
        default_rate=120,
        default_volume=0.9
    )
    
    # Get updated config
    simp_config = get_config("simplification")
    tts_config = get_config("tts")
    
    print("Updated Configuration:")
    print(f"Simplification Model: {simp_config['default_model']}")
    print(f"TTS Rate: {tts_config['default_rate']} WPM")
    print(f"TTS Volume: {tts_config['default_volume']}")
    
    # Use updated config
    simplifier = TextSimplifier(model_type=simp_config['default_model'])
    tts = TextToSpeech(rate=tts_config['default_rate'], volume=tts_config['default_volume'])


# ============================================================================
# EXAMPLE 7: Error Handling
# ============================================================================

def example_error_handling():
    """Proper error handling patterns"""
    from src.modules.ocr_extractor import OCRExtractor
    from src.modules.text_simplifier import TextSimplifier
    import logging
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    ocr = OCRExtractor()
    simplifier = TextSimplifier()
    
    # Handling OCR errors
    try:
        text = ocr.extract_from_pdf("nonexistent.pdf")
    except FileNotFoundError as e:
        logger.error(f"PDF file not found: {e}")
    except Exception as e:
        logger.error(f"OCR extraction failed: {e}")
    
    # Handling simplification errors
    try:
        if not text or len(text) < 10:
            logger.warning("Text too short to simplify")
        else:
            simple_text = simplifier.simplify_text(text)
    except RuntimeError as e:
        logger.error(f"Model loading failed: {e}")
    except Exception as e:
        logger.error(f"Simplification failed: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    import sys
    
    examples = {
        "1": ("OCR Extraction", example_ocr),
        "2": ("Text Simplification", example_simplification),
        "3": ("Text-to-Speech", example_tts),
        "4": ("Complete Pipeline", example_complete_pipeline),
        "5": ("Batch Processing", example_batch_processing),
        "6": ("Custom Configuration", example_custom_config),
        "7": ("Error Handling", example_error_handling),
    }
    
    print("Reading Aid Examples")
    print("=" * 50)
    for key, (name, _) in examples.items():
        print(f"{key}. {name}")
    
    choice = input("\nSelect example (1-7) or 'all': ").strip()
    
    if choice == "all":
        for key, (name, func) in examples.items():
            print(f"\n{'='*50}")
            print(f"Running Example {key}: {name}")
            print('='*50)
            try:
                func()
            except Exception as e:
                print(f"Error in example {key}: {e}")
    elif choice in examples:
        name, func = examples[choice]
        print(f"\nRunning: {name}")
        try:
            func()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid selection")
