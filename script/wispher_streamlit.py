import streamlit as st
import whisper

st.title("Whisper APP")

#Upload audio files with streamlit
audio_file = st.file_uploader("Upload Audio", type = ["wav", "mp3", "m4a"])


@st.cache
def load_whisper_model():
    model = whisper.load_model("base")
    return model


if st.sidebar.button("load whisper Model"):
    model = load_whisper_model()
    st.sidebar.success("Whisper model Loaded")


if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.message("Transcribing Audio")
        transcription = model.transcribe(audio_file)
        st.sidebar.success("transcription Complete")
        st.text(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")
