import streamlit as st
from voice_recignizing_button import voice_recignizing_button
from jsrecordbutton import jsbutton
from streamlit_option_menu import option_menu
import vosk
from game.streamlit_app import game
from voice_recignizing_button import voice_recignizing_button
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container 

def main():
    model = vosk.Model("vosk-model-small-ru-0.22")
    st.title("Голосовой ассистент")
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
    with st.sidebar:
        selected = option_menu("Main Menu", ["игра", 'теория'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected
    if selected == "игра":
        game()
    
    with st.container():
        with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                position: fixed;
                right:0;
                bottom:0;
            }
            """,
        ):
            jsbutton()
    
if __name__ == "__main__":
    main()