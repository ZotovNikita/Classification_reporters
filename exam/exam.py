import numpy as np
import streamlit as st
from cards import load_cards


def match_answer(excepted, actual) -> float:
    return 1.0


def show_question(card_idx: int):
    current_card = st.session_state.exam_cards[card_idx]
    user_answer = st.text_input("Вопрос: " + current_card['txt'])
    if st.button("Проверить ответ"):
        if match_answer(user_answer, current_card["ans"]) > 0.8:
            st.success("Верно!")
        else:
            st.error("Неверный ответ :( Нужно потренироваться на карточках.")


def exam(n_cards: int = 5):
    st.title("Экзамен")

    if 'exam_cards' in st.session_state and not st.session_state.exam_cards:
        with st.container():
            st.write()
    elif 'exam_cards' not in st.session_state:
        cards = load_cards()
        tp_choice = np.random.choice(len(cards), size=n_cards, replace=False)
        exam_cards = [
            {
                "id": card['id'],
                "txt": card['txt'],
                "ans": card['ans'],
            }
            for i, card in enumerate(cards)
            if i in tp_choice
        ]
        st.session_state.exam_cards = exam_cards

    card_idx = 0
    show_question(card_idx)

    if st.button("Следующий вопрос"):
        st.session_state.exam_cards.pop(card_idx)
        print(len(st.session_state.exam_cards))
