import streamlit as st
from jsrecordbutton import jsbutton
from streamlit_option_menu import option_menu
import vosk
from game.streamlit_app import game
from cards import cards
from voice_recognizing_button import voice_recognizing_button
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container
from streamlit_chat import message
from utils.find_sentences import find_sentences
from text_info.variables import id2text, id2vec
from model.sbert import model_sbert, tokenizer_sbert
from game_menu import game_menu
from game.game_def import restart


def main():
    if "game" not in st.session_state:
        st.session_state["game"] = -1

    
    with st.sidebar:
        selected = option_menu(
            "Меню",
            ["Игра", 'Теория', 'Карточки'],
            icons=['house', 'gear', 'bi-book'],
            menu_icon="cast",
            default_index=1,
        )
        selected
    if selected == 'Игра':
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
    if selected == 'Карточки':
        cards()

    if selected == "Теория":

        def on_input_change():
            user_input = st.session_state.user_input
            st.session_state['past'].append(user_input)
            ans = find_sentences(user_input, id2text, id2vec, tokenizer_sbert, model_sbert)
            st.session_state['generated'].append(ans)

        def on_input_change2(user_inputs):
            st.session_state['past'].append(user_inputs)
            ans = find_sentences(user_inputs, id2text, id2vec, tokenizer_sbert, model_sbert)
            st.session_state['generated'].append(ans)

        if 'generated' not in st.session_state:
            st.session_state['generated'] = []
        if 'past' not in st.session_state:
            st.session_state['past'] = []

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))

        result = ""
        label = st.empty()
        with label.container():
            st.text_input("Введите термин", "", key="user_input")
            st.button("отправить", on_click=on_input_change)
        with st.container():
            with stylable_container(
                key="container_with_border",
                css_styles="""
                {
                    position: fixed;
                    right:0;
                    bottom:0;
                    color:black;
                    background-size: cover;
                }
                """,
            ):
                for i in jsbutton():
                    button_value = i
                    with label.container():
                        ans = st.text_input("Введите термин", button_value, key="user_input2")
                        st.button("отправить", on_click=on_input_change2(button_value), key="dsd")


@st.cache_resource
def load_vosk():
    return vosk.Model("vosk-model-small-ru-0.22")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
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
    model = load_vosk()
    main()
