import numpy as np
import streamlit as st
from cards import load_cards
from model import model_sbert, tokenizer_sbert
from utils import cos_similarity, lower_case, get_embedding


def match_answer(excepted: str, actual: str) -> float:
    return cos_similarity(
        get_embedding(lower_case(excepted), tokenizer_sbert, model_sbert),
        get_embedding(lower_case(actual), tokenizer_sbert, model_sbert),
    ).item()


def show_question(card_idx: int):
    current_card = st.session_state.exam_cards[card_idx]
    user_answer = st.text_input(f'Вопрос {st.session_state.cur_question}/{st.session_state.n_questions}: {current_card["txt"]}')

    if not st.session_state.false_answered:
        if st.button('Проверить ответ'):
            if (weight := match_answer(user_answer, current_card["ans"])) > 0.5:
                st.success('Верно!')
                st.session_state.true_answers += 1
            else:
                st.error('Неверный ответ :(')
                st.session_state.false_answered = True
                st.error(f'Совпадение на {max(0, weight):.1%}')
                st.error('Возможно стоит потренироваться на карточках или отвечать более подробно.')


def exam(n_cards: int = 5):
    card_idx = 0

    st.title('Тестирование')

    if 'exam_start' not in st.session_state:
        st.session_state.exam_start = None
        st.session_state.exam_cards = None

    if (
        st.session_state.exam_start
        and st.session_state.exam_cards is not None
        and len(st.session_state.exam_cards) == 0
    ):
        with st.container():
            st.title('Тестирование завершено')
            st.write(f'Правильно отвечено на {st.session_state.true_answers / st.session_state.n_questions:.1%} вопросов')

            del st.session_state.exam_cards
            st.session_state.exam_start = False

            if st.button('Попробовать снова'):
                pass

    if not st.session_state.exam_start:
        cards = load_cards()
        tp_choice = np.random.choice(len(cards), size=n_cards, replace=False)
        exam_cards = [
            {
                'id': card['id'],
                'txt': card['txt'],
                'ans': card['ans'],
            }
            for i, card in enumerate(cards)
            if i in tp_choice
        ]
        st.session_state.exam_cards = exam_cards
        st.session_state.exam_start = True
        st.session_state.true_answers = 0
        st.session_state.cur_question = 1
        st.session_state.false_answered = False
        st.session_state.n_questions = n_cards
    else:
        show_question(card_idx)

        if st.button('Следующий вопрос'):
            st.session_state.false_answered = False
            st.session_state.cur_question += 1
            st.session_state.exam_cards.pop(card_idx)
            print([x['id'] for x in st.session_state.exam_cards], 'exam_cards' in st.session_state)
            st.rerun()
