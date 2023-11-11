import json
import typing as t
import random
import streamlit as st
from streamlit_extras.stylable_container import stylable_container


@st.cache_resource
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data
def load_cards(cards_path: str) -> t.Mapping[str, t.Tuple[str, str]]:
    with open(cards_path, encoding='utf-8') as f:
        return json.load(f)


def get_random_card(cards_: t.Mapping[str, t.Tuple[str, str]]) -> t.Tuple[str, t.Tuple[str, str]]:
    random_card = random.choice(tuple(cards_.items()))
    return random_card


def callback():
    st.session_state.button_clicked = True


def callback2():
    st.session_state.button2_clicked = True


def cards():
    local_css('style.css')
    cards_ = load_cards('cards.json')

    card_id, (card_q, card_ans) = get_random_card(cards_)

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    if "button2_clicked" not in st.session_state:
        st.session_state.button2_clicked = False

    tab1, = st.tabs(['Карточки'])

    with tab1:
        col1, = st.columns(1)
        with col1:
            question = st.button(
                'Получить вопрос',
                on_click=callback,
                key='Draw',
                use_container_width=True,
            )

        if question or st.session_state.button_clicked:
            st.markdown(
                f"""
                <div class="question-block">
                    <h1 class="question-header">Вопрос #{card_id}</h1>
                    <h4>&mdash; {card_q}</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )

            with stylable_container(
                key='container_with_border',
                css_styles="""
                {
                    margin: 1.25rem 0 0;
                }
                """):
                with st.expander("Ответ"):
                    st.markdown(
                        f"""
                        <div class='answer-block'>
                            <p class='answer-text'>{card_ans}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )