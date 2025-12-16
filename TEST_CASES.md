# Manual Test Cases for Reading Aid Application

This document outlines manual test scenarios to ensure the "Reading Aid for Dyslexic People" application is functioning correctly.

## Prerequisites
- Application is running (`streamlit run app.py`)
- Internet connection (for downloading models if not cached)
- Sample files:
    - A clear image containing text (JPG/PNG)
    - A PDF file with text
    - A complex text paragraph for pasting

## Test Scenarios

### 1. Upload & Extract (OCR)

| ID | Test Case | Steps | Expected Result |
|----|-----------|-------|-----------------|
| 1.1 | **Upload Image** | 1. Go to "Upload & Extract" tab.<br>2. Select "Upload Image".<br>3. Upload a sample image with text. | - Image is displayed.<br> - Success message "Text extracted successfully!".<br> - Extracted text appears in the text area. |
| 1.2 | **Upload PDF** | 1. Go to "Upload & Extract" tab.<br>2. Select "Upload PDF".<br>3. Upload a sample PDF. | - Success message "Text extracted successfully!".<br> - Extracted text appears in the text area. |
| 1.3 | **Paste Text** | 1. Go to "Upload & Extract" tab.<br>2. Select "Paste Text".<br>3. Paste text into the area.<br>4. Click "Use This Text". | - Success message "Text loaded successfully!".<br> - Extracted text appears in the text area. |
| 1.4 | **Clear Text** | 1. After extracting text, click "Clear Text". | - Text area is cleared.<br> - Session state is reset. |

### 2. Simplify Text

| ID | Test Case | Steps | Expected Result |
|----|-----------|-------|-----------------|
| 2.1 | **Simplify with T5** | 1. Ensure text is extracted (from step 1).<br>2. Go to "Simplify" tab.<br>3. Select "T5-small" in sidebar.<br>4. Click "Simplify Text". | - Spinner appears.<br> - Success message "Text simplified successfully!".<br> - Simplified text appears in the right column.<br> - "Used: T5-small AI model" info is shown. |
| 2.2 | **Simplify with BART** | 1. Ensure text is extracted.<br>2. Go to "Simplify" tab.<br>3. Select "BART" in sidebar.<br>4. Click "Simplify Text". | - Spinner appears.<br> - Success message "Text simplified successfully!".<br> - Simplified text appears.<br> - "Used: BART AI model" info is shown. |
| 2.3 | **Adjust Parameters** | 1. Change "Max Sentence Length" in sidebar.<br>2. Change "Target Reading Level".<br>3. Click "Simplify Text". | - Output text length/complexity changes accordingly. |
| 2.4 | **Download Text** | 1. After simplification, click "Download Simplified Text". | - A text file `simplified_text.txt` is downloaded containing the simplified text. |

### 3. Text-to-Speech (Listen)

| ID | Test Case | Steps | Expected Result |
|----|-----------|-------|-----------------|
| 3.1 | **Play Audio** | 1. Ensure text is simplified (or extracted).<br>2. Go to "Listen" tab.<br>3. Click "Play Audio". | - Audio starts playing.<br> - Success message "Audio played successfully!". |
| 3.2 | **Save Audio** | 1. Click "Save Audio". | - Spinner appears.<br> - Success message "Audio saved to output/simplified_audio.mp3".<br> - Download button appears. |
| 3.3 | **Change Voice** | 1. Change "Voice Gender" in sidebar (Male/Female).<br>2. Click "Play Audio". | - Voice sounds different (if multiple voices available on OS). |
| 3.4 | **Change Rate/Volume** | 1. Adjust "Speech Rate" and "Volume" in sidebar.<br>2. Click "Play Audio". | - Speed and volume of speech change accordingly. |

### 4. Analysis

| ID | Test Case | Steps | Expected Result |
|----|-----------|-------|-----------------|
| 4.1 | **Check Stats** | 1. Go to "Analysis" tab after simplification. | - "Original Text Statistics" are shown (Words, Sentences, FK Level).<br> - "Simplified Text Statistics" are shown.<br> - "Improvement Analysis" shows reduction in reading level. |

## Edge Cases

- **Empty Input**: Try to simplify without uploading text. -> Should show warning "Please upload or paste text first!".
- **Invalid File**: Upload a non-image/PDF file. -> Streamlit uploader should reject it or show error.
- **Large File**: Upload a very large PDF. -> Should handle gracefully or show timeout/memory error (check logs).

## Sample Text for Testing

Here are two complex sentences you can use to test the simplification:

**Option 1 (Scientific):**
> "The photosynthesis process involves the transformation of light energy into chemical energy, which is subsequently stored in the bonds of glucose molecules."

**Option 2 (Formal/Legal):**
> "Notwithstanding the aforementioned stipulations, the party of the first part reserves the right to terminate this agreement effective immediately upon written notice."
