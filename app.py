import streamlit as st
from jsrecordbutton import jsbutton
from streamlit_option_menu import option_menu
import vosk
from game.streamlit_app import game
from cards import cards
from streamlit_extras.stylable_container import stylable_container


def main():
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
        selected = option_menu(
            "Меню",
            ["Игра", 'Теория', 'Карточки'],
            icons=['house', 'gear', 'shield'],
            menu_icon="cast",
            default_index=1,
        )
        selected

    if selected == 'Игра':
        game()

    if selected == 'Карточки':
        cards()

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
    model = vosk.Model("vosk-model-small-ru-0.22")
    main()
