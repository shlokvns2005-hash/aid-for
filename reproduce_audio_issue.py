
import streamlit as st
import time

st.title("Audio Reproduction Test")

if 'audio_path' not in st.session_state:
    st.session_state.audio_path = None

if st.button("Generate Audio"):
    # Simulate generation
    st.write("Generating...")
    time.sleep(1)
    # Use a dummy generic mp3 or text-to-speech if available easily, or just mock it.
    # I'll create a dummy file.
    with open("test_audio.mp3", "wb") as f:
        f.write(b"ID3" + b"\x00"*100) # Mock mp3 header
    
    st.audio("test_audio.mp3")
    st.write("Audio generated and player shown (inside button).")

st.write("Click this other button to trigger rerun:")
if st.button("Rerun"):
    st.write("Rerunning...")

