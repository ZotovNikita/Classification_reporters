import streamlit as st

import game.game_scenes as game_scenes


def game():

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    if "place" not in st.session_state:
        st.session_state["place"] = "scene1"
    if "sheep_anger" not in st.session_state:
        st.session_state["sheep_anger"] = 0
    if "sword" not in st.session_state:
        st.session_state["sword"] = 0
    if "dragon_alive" not in st.session_state:
        st.session_state["dragon_alive"] = 1
    if "dragon_hp" not in st.session_state:
        st.session_state["dragon_hp"] = 20
    if "temp" not in st.session_state:
        st.session_state["temp"] = ""
    if "counter" not in st.session_state:
        st.session_state["counter"] = 0
    if "scenes_counter" not in st.session_state:
        st.session_state["scenes_counter"] = {
            "intro_counter": 0,
            "cave_counter": 0,
            "trip_counter": 0,
            "elf_counter": 0,
        }


    ###############################################


    local_css("game/style.css")

   
    if st.session_state.place == "scene1":
        game_scenes.scene1()
    elif st.session_state.place == "scene2":
        game_scenes.scene2()    
    elif st.session_state.place == "scene3":
        game_scenes.scene3()
    elif st.session_state.place == "scene4":
        game_scenes.scene4()
    elif st.session_state.place == "scene5":
        game_scenes.scene5()
    elif st.session_state.place == "scene6":
        game_scenes.scene6()
    elif st.session_state.place == "scene7":
        game_scenes.scene7()
    elif st.session_state.place == "scene8":
        game_scenes.scene8()
    elif st.session_state.place == "scene9":
        game_scenes.scene9()
    elif st.session_state.place == "scene10":
        game_scenes.scene10()
