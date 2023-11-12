import streamlit as st
from game.streamlit_app import game

def game_menu():
    show_list = True
    i=0
    modules = ["Введение", "ИНСТРУКЦИЯ ПО ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ И МАНЕВРОВОЙ РАБОТЫ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ.", "Общие требования к организации движения поездов на железнодорожном транспорте",
                "ИНСТРУКЦИЯ ПО СИГНАЛИЗАЦИИ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ","Звуковые сигналы на железнодорожном транспорте","Общие положения","Правила применения семафоров","Ручные сигналы на железнодорожном транспорте",]
    show_component = False
    if show_list:
        for module in modules:
            with st.expander(module):
                if i == 0:
                    if st.button("играть", key = "startass"):
                        show_component = True
                        show_list = False
                        
                elif i == 1:
                    st.button("играть", key = "start2")
                else:
                    st.write("Comming soon 👀")
                i+=1

    if show_component:
        game()        