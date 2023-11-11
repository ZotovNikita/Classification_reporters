import streamlit as st
from voice_recognize import vosk_voice_recognize


def voice_recognizing_button(model):
    st.markdown(
        """
        <style>
        .stButton{
            position: fixed;
            right: 0px;
            bottom: 20px; 
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    if st.button("", key='voice_button'):
        text = vosk_voice_recognize(model)
        st.write(f"Вы сказали: {text}")
