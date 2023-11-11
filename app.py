import streamlit as st
from streamlit_option_menu import option_menu
from game.streamlit_app import game
from exam import exam
from cards import cards
from theory import theory
from game.game_scenes_chapter_1 import test3, test1, test2

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
            ["К Стёпе", 'Ментор', 'Карточки', 'Тестирование'],
            icons=['controller', 'credit-card-2-front', 'bi-book', 'patch-question'],
            menu_icon="cast",
            default_index=1,
        )

    match selected:
        case 'Игра':
            game()
        case 'Теория':
            theory()
        case 'Карточки':
            cards()
        case 'Тестирование':
            exam()


if __name__ == "__main__":
    main()
