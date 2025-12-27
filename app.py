"""
Reading Aid for Dyslexic People - Main Streamlit Application
Pipeline: PDF/Image → OCR → Text Simplification → Text-to-Speech
"""

import streamlit as st
import sys
import os
from pathlib import Path
import logging
from io import BytesIO

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from modules.ocr_extractor import OCRExtractor
from modules.text_simplifier import TextSimplifier
from modules.text_simplifier import TextSimplifier
from modules.text_to_speech import TextToSpeech
from config import OCR_CONFIG

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Reading Aid for Dyslexic People",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better accessibility
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem;
    }
    h1, h2, h3 {
        font-family: Arial, sans-serif;
        color: #1f77b4;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = ""
if 'simplified_text' not in st.session_state:
    st.session_state.simplified_text = ""
if 'reading_level' not in st.session_state:
    st.session_state.reading_level = None
if 'tts_engine' not in st.session_state:
    st.session_state.tts_engine = None

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # Model selection
    st.subheader("AI Model Settings")
    model_type = st.radio(
        "Select Simplification Model:",
        options=["T5-small", "BART"],
        help="T5: Fast summarization. BART: High-quality simplification (DistilBART-CNN)"
    )
    
    # Text-to-Speech settings
    st.subheader("Text-to-Speech Settings")
    tts_engine_type = st.radio(
        "TTS Engine:",
        options=["Standard", "Natural (HQ)"],
        help="Standard: Robotic but fast. Natural: Human-like (First run downloads model)"
    )
    
    # Speech rate moved to Listen tab
    speech_volume = st.slider(
        "Volume:",
        min_value=0.0,
        max_value=1.0,
        value=1.0,
        step=0.1
    )
    voice_gender = st.radio(
        "Voice Gender:",
        options=["Male", "Female"],
        help="Select preferred voice"
    )
    
    # Simplification settings
    st.subheader("Simplification Settings")
    target_reading_level = st.selectbox(
        "Target Reading Level:",
        options=["Easy (6-)", "Moderate (6-9)", "Difficult (9+)"],
        help="Target complexity level for simplified text"
    )
    max_length = st.slider(
        "Max Sentence Length:",
        min_value=50,
        max_value=200,
        value=100,
        step=10
    )
    
    # Information
    st.markdown("---")
    st.markdown("""
    ### About This Tool
    
    This app helps dyslexic readers by:
    - 📄 Extracting text from PDFs and images
    - 🤖 Simplifying complex language
    - 🔊 Converting text to speech
    
    **Supported Formats:**
    - PDF files
    - Images (JPG, PNG, BMP, TIFF)
    - Plain text
    """)


# Main content
st.title("📖 Reading Aid for Dyslexic People")
st.markdown("""
<div class="info-box">
    <strong>Welcome!</strong> This tool helps you read and understand complex texts by:
    <br>1. Converting images/PDFs to text (OCR)
    <br>2. Simplifying the text using AI
    <br>3. Converting the simple text to speech
</div>
""", unsafe_allow_html=True)

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["📤 Upload & Extract", "✏️ Simplify", "🔊 Listen", "📊 Analysis"])

# TAB 1: Upload and Extract
with tab1:
    st.header("Step 1: Upload & Extract Text")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Choose Input Method")
        input_method = st.radio(
            "How would you like to provide text?",
            options=["Upload PDF", "Upload Image", "Paste Text"],
            horizontal=True,
            label_visibility="collapsed"
        )
    
    with col2:
        st.info("💡 Tip: Use high-quality images for better text extraction")
    
    # Initialize OCR extractor
    ocr = OCRExtractor(tesseract_path=OCR_CONFIG["tesseract_path"])
    
    if input_method == "Upload PDF":
        st.subheader("Upload PDF File")
        pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])
        
        if pdf_file is not None:
            with st.spinner("📄 Extracting text from PDF..."):
                try:
                    # Save uploaded file temporarily
                    temp_path = Path("uploads") / pdf_file.name
                    Path("uploads").mkdir(exist_ok=True)
                    with open(temp_path, "wb") as f:
                        f.write(pdf_file.getbuffer())
                    
                    # Extract text
                    st.session_state.extracted_text = ocr.extract_from_pdf(str(temp_path))
                    st.success("✅ Text extracted successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error extracting text: {str(e)}")
    
    elif input_method == "Upload Image":
        st.subheader("Upload Image File")
        image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tiff"])
        
        if image_file is not None:
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(image_file, use_container_width=True, caption="Uploaded Image")
            
            with col2:
                with st.spinner("🖼️ Extracting text from image..."):
                    try:
                        # Save uploaded file temporarily
                        temp_path = Path("uploads") / image_file.name
                        Path("uploads").mkdir(exist_ok=True)
                        with open(temp_path, "wb") as f:
                            f.write(image_file.getbuffer())
                        
                        # Extract text
                        st.session_state.extracted_text = ocr.extract_from_image(str(temp_path))
                        st.success("✅ Text extracted successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error extracting text: {str(e)}")
    
    else:  # Paste Text
        st.subheader("Paste or Type Text")
        text_input = st.text_area(
            "Enter or paste your text here:",
            height=200,
            placeholder="Paste your text here..."
        )
        
        if st.button("Use This Text", type="primary"):
            st.session_state.extracted_text = text_input
            st.success("✅ Text loaded successfully!")
    
    # Display extracted text
    if st.session_state.extracted_text:
        st.subheader("Extracted Text:")
        st.text_area(
            "Original Text:",
            value=st.session_state.extracted_text,
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )
        
        # Option to clear
        if st.button("Clear Text"):
            st.session_state.extracted_text = ""
            st.rerun()


# TAB 2: Simplify
with tab2:
    st.header("Step 2: Simplify Text")
    
    if not st.session_state.extracted_text:
        st.warning("⚠️ Please upload or paste text first!")
    else:
        model_map = {"T5-small": "t5", "BART": "bart"}
        selected_model = model_map[model_type]
        
        
        if st.button("🤖 Simplify Text", type="primary", key="simplify_btn"):
            with st.spinner(f"Simplifying text using {model_type}..."):
                try:
                    # Initialize simplifier
                    st.info(f"Initializing {model_type} model...")
                    simplifier = TextSimplifier(model_type=selected_model)
                    
                    # Check if model actually loaded
                    if simplifier.model_type == "basic" and selected_model != "basic":
                        st.warning(f"⚠️ {model_type} model failed to load. Using basic simplification instead.")
                        st.info("💡 Try restarting Streamlit: Press Ctrl+C and run 'streamlit run app.py' again")
                    else:
                        st.success(f"✅ {model_type} model loaded successfully!")
                    
                    # Split and simplify
                    st.info("Processing text...")
                    st.session_state.simplified_text = simplifier.split_and_simplify(
                        st.session_state.extracted_text,
                        chunk_size=max_length
                    )
                    
                    # Calculate reading level
                    st.session_state.reading_level = simplifier.calculate_flesch_kincaid_level(
                        st.session_state.simplified_text
                    )
                    
                    st.success("✅ Text simplified successfully!")
                    
                    # Show which model was actually used
                    if simplifier.model_type == "basic":
                        st.info(f"ℹ️ Used: Basic rule-based simplification")
                    else:
                        st.info(f"ℹ️ Used: {model_type} AI model")
                    
                except Exception as e:
                    st.error(f"❌ Error simplifying text: {str(e)}")
                    st.error(f"Error type: {type(e).__name__}")
                    with st.expander("Show full error details"):
                        import traceback
                        st.code(traceback.format_exc())
        
        # Display results
        if st.session_state.simplified_text:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Original Text")
                st.text_area(
                    "Original:",
                    value=st.session_state.extracted_text,
                    height=250,
                    disabled=True,
                    label_visibility="collapsed"
                )
            
            with col2:
                st.subheader("Simplified Text")
                st.text_area(
                    "Simplified:",
                    value=st.session_state.simplified_text,
                    height=250,
                    disabled=True,
                    label_visibility="collapsed"
                )
            
            # Download button
            st.download_button(
                label="📥 Download Simplified Text",
                data=st.session_state.simplified_text,
                file_name="simplified_text.txt",
                mime="text/plain"
            )


# TAB 3: Listen
with tab3:
    st.header("Step 3: Text-to-Speech")
    
    if not st.session_state.simplified_text and not st.session_state.extracted_text:
        st.warning("⚠️ Please extract and simplify text first!")
    else:
        text_to_speak = st.session_state.simplified_text if st.session_state.simplified_text else st.session_state.extracted_text
        
        # Initialize session state for audio path if not exists
        if 'audio_path' not in st.session_state:
            st.session_state.audio_path = None
        if 'last_tts_config' not in st.session_state:
            st.session_state.last_tts_config = {}
        
        # Speech Rate Control (Visual only, value used in generation)
        col_rate, col_vol = st.columns(2)
        with col_rate:
            speech_rate = st.slider(
                "Speech Rate (Words per Minute)", 
                min_value=50, 
                max_value=300, 
                value=150, 
                step=10,
                help="Adjust how fast the text is spoken. Natural voices use audio time-stretching for speed control."
            )
        
        # Determine voice ID
        voice_id = 1 if voice_gender == "Female" else 0
        
        # Audio Generation Logic
        current_config = {
            "text": text_to_speak,
            "rate": speech_rate,
            "volume": speech_volume,
            "voice_id": voice_id,
            "engine": tts_engine_type
        }
        
        # Check if we need to regenerate (if config changed or no audio yet)
        should_generate = (
            st.session_state.audio_path is None or 
            not os.path.exists(st.session_state.audio_path) or
            st.session_state.last_tts_config != current_config
        )
        
        if should_generate:
            try:
                # Initialize TTS with selected rate
                # Note: We rely on the caching/persistence of the file system
                import time
                timestamp = int(time.time())
                output_filename = f"simplified_audio_{timestamp}.mp3"
                output_path = str(Path("output") / output_filename)
                
                # Ensure output directory exists
                Path("output").mkdir(exist_ok=True)
                
                # Cleanup old files if needed to save space? 
                # For now, let's just keep the new one and reference it.
                # Ideally we delete the previous one tracked in session state
                if st.session_state.audio_path and os.path.exists(st.session_state.audio_path):
                    try:
                        os.remove(st.session_state.audio_path)
                    except:
                        pass # Ignore cleanup errors
                
                engine_code = "natural" if tts_engine_type == "Natural (HQ)" else "standard"
                tts = TextToSpeech(rate=speech_rate, volume=speech_volume, voice_id=voice_id, engine_type=engine_code)
                tts.save_to_file(text_to_speak, output_path)
                
                st.session_state.audio_path = output_path
                st.session_state.last_tts_config = current_config.copy()
                
            except Exception as e:
                st.error(f"❌ Error generating audio: {str(e)}")
        
        # Display Audio Player if path exists
        if st.session_state.audio_path and os.path.exists(st.session_state.audio_path):
            st.audio(st.session_state.audio_path, format="audio/mp3")
            
            # Download button
            with open(st.session_state.audio_path, "rb") as audio_file:
                st.download_button(
                    label="📥 Download Audio",
                    data=audio_file,
                    file_name="simplified_audio.mp3",
                    mime="audio/mpeg"
                )
        
        # Text preview
        st.subheader("Text to be Spoken:")
        st.text_area(
            "Preview:",
            value=text_to_speak,
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )


# TAB 4: Analysis
with tab4:
    st.header("📊 Text Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Text Statistics")
        if st.session_state.extracted_text:
            words = st.session_state.extracted_text.split()
            sentences = [s for s in st.session_state.extracted_text.split(".") if s.strip()]
            
            st.metric("Total Words", len(words))
            st.metric("Total Sentences", len(sentences))
            st.metric("Avg Words per Sentence", round(len(words) / max(len(sentences), 1), 2))
            
            # Calculate original reading level
            simplifier = TextSimplifier()
            orig_level = simplifier.calculate_flesch_kincaid_level(st.session_state.extracted_text)
            
            st.metric("Flesch-Kincaid Level", orig_level["fk_level"])
            st.metric("Complexity", orig_level["complexity"].capitalize())
        else:
            st.info("No original text to analyze")
    
    with col2:
        st.subheader("Simplified Text Statistics")
        if st.session_state.simplified_text:
            words = st.session_state.simplified_text.split()
            sentences = [s for s in st.session_state.simplified_text.split(".") if s.strip()]
            
            st.metric("Total Words", len(words))
            st.metric("Total Sentences", len(sentences))
            st.metric("Avg Words per Sentence", round(len(words) / max(len(sentences), 1), 2))
            
            if st.session_state.reading_level:
                st.metric("Flesch-Kincaid Level", st.session_state.reading_level["fk_level"])
                st.metric("Complexity", st.session_state.reading_level["complexity"].capitalize())
        else:
            st.info("No simplified text to analyze")
    
    # Comparison
    if st.session_state.extracted_text and st.session_state.simplified_text:
        st.subheader("Improvement Analysis")
        
        simplifier = TextSimplifier()
        orig_level = simplifier.calculate_flesch_kincaid_level(st.session_state.extracted_text)
        simp_level = st.session_state.reading_level if st.session_state.reading_level else simplifier.calculate_flesch_kincaid_level(st.session_state.simplified_text)
        
        level_reduction = orig_level["fk_level"] - simp_level["fk_level"]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Reading Level Improvement", f"{level_reduction:.2f} levels", delta=f"{-level_reduction:.2f}")
        with col2:
            st.metric("Original Complexity", orig_level["complexity"].capitalize())
        with col3:
            st.metric("Simplified Complexity", simp_level["complexity"].capitalize())


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8rem;'>
    <p>Reading Aid for Dyslexic People © 2024</p>
    <p>Powered by Tesseract OCR, T5/BART, and pyttsx3</p>
    <p>This tool is designed to help individuals with dyslexia read and understand complex texts more easily.</p>
</div>
""", unsafe_allow_html=True)
