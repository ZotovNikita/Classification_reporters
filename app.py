import streamlit as st
from streamlit_option_menu import option_menu
from game.streamlit_app import game
from exam import exam
from cards import cards
from theory import theory
from streamlit_extras.stylable_container import stylable_container
from game_menu import game_menu
from game.game_def import restart


def main():
    if 'game' not in st.session_state:
        st.session_state['game'] = -1

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
            modules = ["Введение", "ИНСТРУКЦИЯ ПО ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ И МАНЕВРОВОЙ РАБОТЫ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ.", "Общие требования к организации движения поездов на железнодорожном транспорте",
                    "ИНСТРУКЦИЯ ПО СИГНАЛИЗАЦИИ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ","Звуковые сигналы на железнодорожном транспорте","Общие положения","Правила применения семафоров","Ручные сигналы на железнодорожном транспорте",]
            i = 0
            div = st.empty()
            if st.session_state["game"] == -1:
                with div.container():
                    for module in modules:
                        with st.expander(module):
                            if i == 0:
                                if st.button("играть", key = "startass"):
                                    st.session_state["game"] = i 
                            elif i == 1:
                                st.button("играть", key = "start2")
                            else:
                                st.write("Comming soon 👀")
                            i+=1           
            if st.session_state["game"] == 0:
                div.empty()
                with stylable_container(
                    key="container_with_border",
                    css_styles="""
                    {
                    padding:3rem,5rem;
                    }
                    """,
                ):
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
    st.expander('foo')
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
