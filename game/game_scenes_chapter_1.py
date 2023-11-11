# import streamlit as st
# from streamlit_extras.stoggle import stoggle
# import game.game_config as game_config
# import game.game_def as game_def

# ###############################################
# #
# #               intro Scene
# #
# ################################################
# def set_state(i):
#     st.session_state.place = i

# def ch1_scene1():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["start_ch1_scene"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Знание нормативной документации РЖД необходимо для сотрудника этой компании. Поэтому для начала ознакомься с теорией данного модуля.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene2"))

    

# def ch1_scene2():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["start_ch1_scene"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Инструкция по организации движения поездов и маневровой работы на железнодорожном транспорте Российской Федерации (далее - Инструкция) устанавливает правила приема, отправления и пропуска поездов (приложения N 1 - N 9 к Инструкции), производства маневров (приложения N 10 - N 11 к Инструкции), закрепления железнодорожного подвижного состава (приложение N 12 к Инструкции), правила приема и отправления поездов в условиях выполнения ремонтно-строительных работ (приложения N 13 - N 14 к Инструкции), порядок назначения и передачи предупреждений на поезда (приложение N 15 к Инструкции), а также отдельные процессы, связанные с производством поездной и маневровой работы (приложения N 16 - N 20 к Инструкции).</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene1"), key='1')
#     st.button("Далее", type="primary", on_click = set_state("ch1_scene3"), key='2')
    


# def ch1_scene3():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["start_ch1_scene"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Не так уж и сложно, правда? Проверим насколько ты усвоил эту небольшую теоретическую выкладку.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     player_name_container = st.empty()
#     player_name_container.text_input(
#         "Введи свое имя", key="player_name"
#     )
#     main_text_container = st.empty()
#     if st.session_state.player_name != "":
#         player_name_container.empty()

#         main_text_container.empty()


#     st.button("Далее", type="primary", on_click = set_state("ch1_scene4"), key='3')
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene2"), key='4')



# def ch1_scene4():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["in_train"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Думаю, тебе понятно, по какому принципу мы будем работать. Теперь тебе будет предложен к изучению теоретический блок покрупнее, после чего мы проверим твои знания.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene5"))
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene3"))

# def ch1_scene5():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["history1"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Нормативно-технический документ, графически отображающий следование поездов на масштабной сетке (далее - график движения поездов) <1>, объединяет деятельность всех подразделений, выражает заданный объем эксплуатационной работы подразделений владельцев инфраструктур железнодорожного транспорта общего пользования (далее - инфраструктура) (владельцев железнодорожных путей необщего пользования).</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene6"))
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene4"))


# def ch1_scene6():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["history2"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Сводный график движения поездов утверждается в порядке, определяемом федеральным органом исполнительной власти в области железнодорожного транспорта, на основании предложенных владельцами инфраструктур графиков движения поездов в пределах инфраструктур.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene7"))
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene5"))



# def ch1_scene7():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["history3"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Организация движения поездов в пределах одной инфраструктуры осуществляется на основании графика движения поездов, утверждаемого и вводимого в действие владельцем этой инфраструктуры.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene8"))
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene6"))


# def ch1_scene8():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["history4"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Движение поездов по графику обеспечивается соблюдением требований Правил технической эксплуатации железных дорог Российской Федерации, утвержденным настоящим Приказом (далее - Правила), организацией и выполнением технологического процесса работы подразделений железнодорожного транспорта, связанных с движением поездов.<p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     st.button("Далее", type="primary", on_click = set_state("ch1_scene9"))
#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene7"))

# def ch1_scene9():

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         st.image(game_config.image_source["in_train"])
#         st.write("")
#     with col2:
#         if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Нарушение графика движения поездов не допускается. В случаях нарушения графика движения поездов работники всех подразделений железнодорожного транспорта обязаны принимать оперативные меры для ввода в график опаздывающих поездов и обеспечивать их безопасное проследование.</p></div>',
#                 unsafe_allow_html=True,
#             )

#             audio_file = open("game/audio/intro.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")

#     # st.button("Назад", type="primary", on_click = set_state("ch1_scene8"))

# def test1(): 

#     st.multiselect("Выбери все верные варианты: Инструкция по организации движения поездов и маневровой работы на железнодорожном транспорте Российской Федерации устанавливает:", 
#                    ["правила приема, отправления и пропуска поездов", 
#                     "правила конструирования поездов", 
#                     "правила производства маневров",
#                     "правила приема и отправления поездов в условиях выполнения   ремонтно-строительных работ ",
#                     "внутренний интерьер вагонов"])