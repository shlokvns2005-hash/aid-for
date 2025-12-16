"""
Minimal Streamlit app to test JUST the transformers
Run this to see if the issue is with the main app or the models
"""

import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

st.set_page_config(page_title="Transformer Test", page_icon="🧪")

st.title("🧪 Transformer Model Test")

st.markdown("""
This is a minimal test app to check if the transformers are working.
If this works, the issue is with the main app. If this fails, we need to fix the models.
""")

# Model selection
model_choice = st.radio("Select Model:", ["T5-small", "BART"])

# Text input
test_text = st.text_area(
    "Enter text to simplify:",
    value="The phenomenon of photosynthesis is an extraordinarily complex biochemical process.",
    height=100
)

if st.button("Test Simplification", type="primary"):
    model_map = {"T5-small": "t5", "BART": "bart"}
    selected_model = model_map[model_choice]
    
    with st.spinner(f"Testing {model_choice}..."):
        try:
            # Import
            st.info("Step 1: Importing TextSimplifier...")
            from modules.text_simplifier import TextSimplifier
            st.success("✅ Import successful")
            
            # Initialize
            st.info(f"Step 2: Initializing {model_choice} model...")
            simplifier = TextSimplifier(model_type=selected_model)
            st.success(f"✅ Model initialized (type: {simplifier.model_type})")
            
            # Check if model loaded
            if simplifier.model is None:
                st.error("❌ Model is None - transformers not available!")
                st.warning(f"Model fell back to: {simplifier.model_type}")
            else:
                st.success(f"✅ Model loaded: {type(simplifier.model).__name__}")
            
            # Simplify
            st.info("Step 3: Simplifying text...")
            result = simplifier.simplify_text(test_text, max_length=100)
            st.success("✅ Simplification successful!")
            
            # Show results
            st.subheader("Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Original:**")
                st.write(test_text)
            
            with col2:
                st.markdown("**Simplified:**")
                st.write(result)
            
            # Reading level
            level = simplifier.calculate_flesch_kincaid_level(result)
            st.metric("Reading Level", f"{level['fk_level']} ({level['complexity']})")
            
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error: {type(e).__name__}")
            st.code(str(e))
            
            with st.expander("Full Error Details"):
                import traceback
                st.code(traceback.format_exc())

st.markdown("---")
st.markdown("""
### Troubleshooting

If you see errors:

1. **"sentencepiece not found"** → Restart Streamlit
2. **"Model is None"** → Transformers not loading properly
3. **Any other error** → Check the error details above

**To restart:** Press Ctrl+C in terminal, then run `streamlit run test_minimal_app.py`
""")
