"""
Check what's actually happening in the Streamlit process
"""

import subprocess
import sys

print("="*80)
print("STREAMLIT ENVIRONMENT CHECK")
print("="*80)

# Check if sentencepiece is available
print("\n1. Checking sentencepiece installation...")
try:
    import sentencepiece
    print(f"   ✅ sentencepiece is installed")
    print(f"   Version: {sentencepiece.__version__}")
    print(f"   Location: {sentencepiece.__file__}")
except ImportError as e:
    print(f"   ❌ sentencepiece NOT installed: {e}")

# Check transformers
print("\n2. Checking transformers installation...")
try:
    import transformers
    print(f"   ✅ transformers is installed")
    print(f"   Version: {transformers.__version__}")
except ImportError as e:
    print(f"   ❌ transformers NOT installed: {e}")

# Check if T5Tokenizer can load
print("\n3. Checking T5Tokenizer...")
try:
    from transformers import T5Tokenizer
    print(f"   ✅ T5Tokenizer can be imported")
    
    # Try to actually load it
    print("   Loading T5 tokenizer...")
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    print(f"   ✅ T5 tokenizer loaded successfully")
except Exception as e:
    print(f"   ❌ T5Tokenizer failed: {e}")

# Check Python environment
print("\n4. Python environment info...")
print(f"   Python: {sys.executable}")
print(f"   Version: {sys.version}")

# Check which pip
print("\n5. Pip location...")
result = subprocess.run(['where', 'pip'], capture_output=True, text=True, shell=True)
print(f"   {result.stdout}")

print("="*80)
