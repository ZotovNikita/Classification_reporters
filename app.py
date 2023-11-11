import streamlit as st
from streamlit_option_menu import option_menu
from game.streamlit_app import game
from exam import exam
from cards import cards
from theory import theory


def main():
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
            ["Игра", 'Теория', 'Карточки', 'Тест'],
            icons=['house', 'gear', 'bi-book', 'patch-question'],
            menu_icon="cast",
            default_index=1,
        )
        selected

    match selected:
        case 'Игра':
            game()
        case 'Теория':
            theory()
        case 'Карточки':
            cards()
        case 'Тест':
            exam()


if __name__ == "__main__":
    main()
