# How to Install Tesseract OCR

The "tesseract is not installed or it's not in your PATH" error means that the Tesseract OCR engine is missing from your computer. This software is required to read text from images.

## Step 1: Download the Installer
1.  Go to the Tesseract at UB Mannheim GitHub page: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2.  Download the latest installer, usually named something like `tesseract-ocr-w64-setup-v5.3.3.20231005.exe`.

## Step 2: Run the Installer
1.  Run the downloaded `.exe` file.
2.  **IMPORTANT:** During installation, you might see a screen asking about "Additional tasks" or components.
3.  **CRITICAL STEP:** Look for an option that says **"Add to PATH"** or similar, but even if you don't see it, just proceed with the default installation location: `C:\Program Files\Tesseract-OCR`.

## Step 3: Configure the App (If not added to PATH)
If you installed Tesseract but the app still can't find it, we need to tell the app exactly where it is.

1.  Open the file `config.py` in your project folder.
2.  Find the section `OCR_CONFIG`.
3.  Change the line:
    ```python
    "tesseract_path": None,
    ```
    to:
    ```python
    "tesseract_path": r'C:\Program Files\Tesseract-OCR\tesseract.exe',
    ```
    *(Make sure the path matches where you actually installed it)*

## Step 4: Restart
1.  Close the terminal/command prompt where Streamlit is running (Ctrl+C).
2.  Open a new terminal.
3.  Run the app again: `streamlit run app.py`
