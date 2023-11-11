import streamlit as st
from streamlit_option_menu import option_menu
from game.streamlit_app import game
from exam import exam
from cards import cards
from theory import theory


def main():

    with st.sidebar:
        selected = option_menu(
            'Меню',
            ['К Стёпе', 'Ментор', 'Карточки', 'Тестирование'],
            icons=['controller', 'credit-card-2-front', 'bi-book', 'patch-question'],
            menu_icon='cast',
            default_index=1,
        )

    match selected:
        case 'К Стёпе':
            game()
        case 'Ментор':
            theory()
        case 'Карточки':
            cards()
        case 'Тестирование':
            exam()


if __name__ == '__main__':
    st.set_page_config(layout='wide')
    remove_padding_css = """
        .block-container {
        padding: 2rem 2rem;
        }
        """
    st.markdown(
        "<style>"
        + remove_padding_css
        + "</styles>",
        unsafe_allow_html=True,
    )
    st.expander("foo")
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    main()
