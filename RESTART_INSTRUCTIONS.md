# 🔄 RESTART REQUIRED

## Why Restart is Needed

The `sentencepiece` library was installed **after** Streamlit started running. Streamlit loads all Python modules when it starts, so it doesn't know about the new dependency yet.

## How to Fix

### Option 1: Restart Streamlit (Recommended)

1. **Stop the current Streamlit server:**
   - Go to the terminal where Streamlit is running
   - Press `Ctrl + C` to stop it

2. **Start Streamlit again:**
   ```bash
   streamlit run app.py
   ```

3. **Test the models:**
   - Open http://localhost:8501
   - Go to "Upload & Extract" tab
   - Paste some text
   - Go to "Simplify" tab
   - Select "T5-small" in the sidebar
   - Click "Simplify Text"

### Option 2: Clear Streamlit Cache

If restarting doesn't work:

1. In the Streamlit app, press `C` to open the menu
2. Click "Clear cache"
3. Try simplifying text again

### Option 3: Force Restart

```bash
# Kill all Streamlit processes
taskkill /F /IM streamlit.exe

# Start fresh
streamlit run app.py
```

## Verification

After restarting, you can verify the models work by running:

```bash
python simulate_streamlit_click.py
```

This simulates exactly what happens when you click the "Simplify Text" button.

## What Should Happen

When working correctly, you should see:

1. ✅ "Simplifying text using T5-small..." spinner
2. ✅ Simplified text appears in the right column
3. ✅ "Text simplified successfully!" success message
4. ✅ Reading level metrics in the Analysis tab

## If Still Not Working

Run this diagnostic:

```bash
python check_environment.py
```

And share the output so I can see what's happening.

---

**TL;DR: Stop Streamlit (Ctrl+C) and restart it with `streamlit run app.py`**
