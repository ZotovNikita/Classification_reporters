import streamlit as st
from streamlit_extras.stoggle import stoggle
import game.game_config as game_config
import game.game_def as game_def
import streamlit_extras.stylable_container as stylable_container


def set_state(i):
    st.session_state.place = i

def scene1():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["start_scene"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Чу-чух! Компания РЖД приветствует тебя, путник,  на нашем поезде! Меня зовут Степа, я буду твоим персональным компаньоном и помогу тебе освоиться в этом непростом, но очень интересном мире железных дорог!</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene2"))

    

def scene2():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["start_scene"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Нам  предстоит изучить правила и нормативы РЖД. Процесс обучения построен в формате квест-игры. Чтобы успешно проходить уровни, изучай теорию, периодически выполняя задания для закрепления пройденного материала, и получай за это очки.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    # st.button("Назад", type="primary", on_click = set_state("scene1"), key='1')
    st.button("Далее", type="primary", on_click = set_state("scene3"), key='2')
    


def scene3():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["start_scene"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Если трудности тебя не пугают, то введи свое имя, и мы начнем наше приключение!</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    player_name_container = st.empty()
    player_name_container.text_input(
        "Введи свое имя", key="player_name"
    )
    main_text_container = st.empty()
    if st.session_state.player_name != "":
        player_name_container.empty()

        main_text_container.empty()


    st.button("Далее", type="primary", on_click = set_state("scene4"), key='3')
    # st.button("Назад", type="primary", on_click = set_state("scene2"), key='4')



def scene4():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["in_train"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Рад с тобой познакомиться, {st.session_state.player_name}. Ты действительно смелый. Позволь, для начала я введу в тебя в курс дела. </p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene5"))
    # st.button("Назад", type="primary", on_click = set_state("scene3"))

def scene5():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["history1"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Железные дороги и поезда играли огромную роль в развитии цивилизаций по всему миру. Их история начинается еще в Древней Греции, где были вырублены колеи в павшем камне, чтобы облегчить перевозку лодок через Истмос Коринфа 1. Однако после завоевания греков римлянами в 146 г. до н.э. железные дороги ушли в небытие на более чем 1400 лет. Современная железнодорожная система появилась только в 16 веке, но еще триста лет понадобилось, чтобы изобретение паровой машины преобразовало железнодорожный транспорт в масштабное явление на мировом уровне.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene6"))
    # st.button("Назад", type="primary", on_click = set_state("scene4"))


def scene6():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["history2"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Первые предшественники современных поездов появились в начале 1550-х годов в Германии с появлением вагонных дорог. Эти первобытные железные дороги состояли из деревянных рельс, по которым легче передвигались повозки, запряженные лошадьми, чем по грязным дорогам. К 1770-м годам деревянные рельсы были заменены железными. Эти вагонные дороги превратились в трамвайные линии, распространенные по всей Европе. В 1789 году англичанин Уильям Джессап спроектировал первые вагоны с фланцевыми колесами, которые были желобчатыми, что позволяло колесам лучше сцепляться с рельсами. Эта важная конструктивная особенность была передана на более поздние локомотивы.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene7"))
    # st.button("Назад", type="primary", on_click = set_state("scene5"))



def scene7():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["history3"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p> В 1803 году человек по имени Сэмюэл Хомфрей решил финансировать разработку парового транспортного средства для замены повозок, запряженных лошадьми, на трамвайных линиях. В 1820 году Джон Биркиншо изобрел более прочный материал, называемый кованым железом, который стал стандартом до появления процесса Бессемера, позволившего дешево производить сталь в конце 1860-х годов, что привело к быстрому расширению железных дорог не только в Америке, но и во всем мире.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene8"))
    # st.button("Назад", type="primary", on_click = set_state("scene6"))


def scene8():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["history4"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>В 19 веке железнодорожный транспорт стал одним из самых важных средств передвижения и транспортировки грузов. В 1804 году появился первый поезд, который смог перевезти 25 тонн железного материала и 70 человек на расстояние 10 миль 2. С тех пор поезда были оснащены паровыми, электрическими и дизельными двигателями 2. Сегодня железнодорожный транспорт продолжает играть важную роль в мировой экономике и транспортировке людей и грузов.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("scene9"))
    # st.button("Назад", type="primary", on_click = set_state("scene7"))

def scene9():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["in_train"])
        st.write("")
    with col2:
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Надеюсь, этот небольшой экскурс в историю тебе не наскучил. Теперь, когда ты погрузился в историю возникновения железных дорог, ты готов начать обучение. Пусть твой локомотив всегда ведет железная дорога приключений! Желаю успехов!</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
    game_def.restart()

    # st.button("Назад", type="primary", on_click = set_state("scene8"))

def test1(): 

    st.multiselect("Выбери все верные варианты: Инструкция по организации движения поездов и маневровой работы на железнодорожном транспорте Российской Федерации устанавливает:", 
                   ["правила приема, отправления и пропуска поездов", 
                    "правила конструирования поездов", 
                    "правила производства маневров",
                    "правила приема и отправления поездов в условиях выполнения   ремонтно-строительных работ ",
                    "внутренний интерьер вагонов"])
    