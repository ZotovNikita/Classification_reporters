import streamlit as st


def clear(ss_variable):
    st.session_state["temp"] = st.session_state[ss_variable]
    st.session_state[ss_variable] = ""
    st.session_state["counter"] += 1


def temp_clear():
    st.session_state["temp"] = ""
