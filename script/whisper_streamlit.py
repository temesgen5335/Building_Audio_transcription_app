import streamlit as st
import whisper

st.title("Whisper APP")

#Upload audio files with streamlit
audio_file = st.file_uploader("Upload Audio", type = ["wav", "mp3", "m4a"])


model = whisper.load_model("base")
st.text("Whisper model Loaded")



if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")

if st.sidebar.button("Play Original Audio File"):
    st.sidebar.audio(audio_file)