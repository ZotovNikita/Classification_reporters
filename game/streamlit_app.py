import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards
import time
import random
import game.game_scenes as game_scenes

# additional components from https://extras.streamlit.app/

# -------------- app config ---------------
def game():

    # define external css
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    ###############################################
    #
    #
    #           VARIABLES DEFINITION
    #
    #
    ################################################

    # variable responsible for checking if player provided his name and game can be started


    # set session states
    # this is streamlit specific. For more contex please check streamlit documenation

    # if "health" not in st.session_state:
    #     st.session_state["health"] = 100
    # if "mana" not in st.session_state:
    #     st.session_state["mana"] = 80
    # if "gold" not in st.session_state:
    #     st.session_state["gold"] = 5
    # if "place" not in st.session_state:
    #     st.session_state["place"] = "scene1"
    # if "sheep_anger" not in st.session_state:
    #     st.session_state["sheep_anger"] = 0
    # if "sword" not in st.session_state:
    #     st.session_state["sword"] = 0
    # if "dragon_alive" not in st.session_state:
    #     st.session_state["dragon_alive"] = 1
    # if "dragon_hp" not in st.session_state:
    #     st.session_state["dragon_hp"] = 20
    # if "temp" not in st.session_state:
    #     st.session_state["temp"] = ""
    # if "counter" not in st.session_state:
    #     st.session_state["counter"] = 0
    # if "scenes_counter" not in st.session_state:
    #     st.session_state["scenes_counter"] = {
    #         "intro_counter": 0,
    #         "cave_counter": 0,
    #         "trip_counter": 0,
    #         "elf_counter": 0,
    #     }


    ###############################################
    #
    #
    #               GAME ENGINE
    #
    #
    ################################################

    # ---------------- CSS ----------------

    local_css("game/style.css")

    # ----------------- game start --------
    start = True

    # welcome = st.empty()
    # welcome.title("Welcome to StreamlitLand, adventurer!")

    # # hero base statistics

    # player_name_container = st.empty()
    # player_name_container.text_input(
    #     "State your name and hit enter to start the game", key="player_name"
    # )
    # main_text_container = st.empty()


    # if st.session_state.player_name != "":
    #     player_name_container.empty()

    #     main_text_container.empty()
    #     start = True

    # START THE GAME

 
    if start == True:
        # delete welcome
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

        # player stats

        # col1, col2, col3 = st.columns(3)
        # col1.metric(label="Health", value=st.session_state.health, delta=0)
        # col2.metric(label="Mana", value=st.session_state.mana, delta=0)
        # col3.metric(label="Gold", value=st.session_state.gold, delta=0)
        # style_metric_cards(
        #     background_color="#black", border_color="#21212f", border_left_color="#21212f"
        # )

        # if st.session_state["sword"] == 1:
        #     st.write("🗡️ sword equipped")

    # this part of the code focuses input on text window
    # please note that counter is required - for streamlit specific it does not work without it

    components.html(
        f"""
            <div>some hidden container</div>
            <p>{st.session_state.counter}</p>
            <script>
                var input = window.parent.document.querySelectorAll("input[type=text]");
                for (var i = 0; i < input.length; ++i) {{
                    input[i].focus();
                }}
        </script>
        """,
        height=0,
    )

    hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    
