import random
import streamlit as st
import json
import typing as t


@st.cache_resource
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data
def load_cards(cards_path: str) -> t.Mapping[str, str]:
    with open(cards_path, encoding='utf-8') as f:
        return json.load(f)


def get_random_question(cards_: t.Mapping[str, str]) -> str:
    random_question = random.choice(tuple(cards_.items()))
    return random_question


def cards():
    def callback():
        st.session_state.button_clicked = True

    def callback2():
        st.session_state.button2_clicked = True

    local_css('style.css')
    cards_ = load_cards('cards.json')

    q_id, question_text = get_random_question(cards_)

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    if "button2_clicked" not in st.session_state:
        st.session_state.button2_clicked = False

    tab1, = st.tabs(['Карточки'])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            question = st.button(
                'Получить вопрос',
                on_click=callback,
                key='Draw',
                use_container_width=True,
            )
        with col2:
            answer = st.button(
                'Показать ответ',
                on_click=callback2,
                key='Answer',
                use_container_width=True,
            )

        if question or st.session_state.button_clicked:
            st.markdown(
                f"""
                <div class="question-block">
                    <h1 class="question-header">Вопрос #{q_id}</h1>
                    <h4>&mdash; {question_text}</h4>
                </div>
                """,
                unsafe_allow_html=True,
            )
            u_answer = st.text_input('Ваш ответ: ', value='')

            if answer and st.session_state.button2_clicked:
                        # <p class='answer-text'>Правильный ответ: {u_answer}</p>
                st.markdown(
                    f"""
                    <div class='answer-block'>
                        <p class='answer-text'>Ваш ответ схож с правильным на {0.99:.3%}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.session_state.button2_clicked = False
