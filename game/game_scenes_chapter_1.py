import streamlit as st
from streamlit_extras.stoggle import stoggle
import game.game_config as game_config
import game.game_def as game_def
from st_draggable_list import DraggableList
from model.sbert import tokenizer_sbert, model_sbert
from utils.cos_similarity import cos_similarity
from utils.get_embedding import get_embedding
from utils.lower_case import lower_case


def set_state(i):
    st.session_state.place = i

def ch1_scene1():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Знание нормативной документации РЖД необходимо для сотрудника этой компании. Поэтому для начала ознакомься с теорией данного модуля.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene2"))

    

def ch1_scene2():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor2"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Инструкция по организации движения поездов и маневровой работы на железнодорожном транспорте Российской Федерации (далее - Инструкция) устанавливает правила приема, отправления и пропуска поездов (приложения N 1 - N 9 к Инструкции), производства маневров (приложения N 10 - N 11 к Инструкции), закрепления железнодорожного подвижного состава (приложение N 12 к Инструкции), правила приема и отправления поездов в условиях выполнения ремонтно-строительных работ (приложения N 13 - N 14 к Инструкции), порядок назначения и передачи предупреждений на поезда (приложение N 15 к Инструкции), а также отдельные процессы, связанные с производством поездной и маневровой работы (приложения N 16 - N 20 к Инструкции).</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    # st.button("Назад", type="primary", on_click = set_state("ch1_scene1"), key='1')
    st.button("Далее", type="primary", on_click = set_state("ch1_scene3"), key='2')
    


def ch1_scene3():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor3"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Не так уж и сложно, правда? Проверим насколько ты усвоил эту небольшую теоретическую выкладку.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene4"), key='3')
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene2"), key='4')



def ch1_scene4():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor4"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Думаю, тебе понятно, по какому принципу мы будем работать. Теперь тебе будет предложен к изучению теоретический блок покрупнее, после чего мы проверим твои знания.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene5"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene3"))

def ch1_scene5():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor5"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Нормативно-технический документ, графически отображающий следование поездов на масштабной сетке (далее - график движения поездов) <1>, объединяет деятельность всех подразделений, выражает заданный объем эксплуатационной работы подразделений владельцев инфраструктур железнодорожного транспорта общего пользования (далее - инфраструктура) (владельцев железнодорожных путей необщего пользования).</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene6"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene4"))


def ch1_scene6():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor2"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Сводный график движения поездов утверждается в порядке, определяемом федеральным органом исполнительной власти в области железнодорожного транспорта, на основании предложенных владельцами инфраструктур графиков движения поездов в пределах инфраструктур.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene7"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene5"))



def ch1_scene7():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor3"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Организация движения поездов в пределах одной инфраструктуры осуществляется на основании графика движения поездов, утверждаемого и вводимого в действие владельцем этой инфраструктуры.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene8"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene6"))


def ch1_scene8():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor4"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Движение поездов по графику обеспечивается соблюдением требований Правил технической эксплуатации железных дорог Российской Федерации, утвержденным настоящим Приказом (далее - Правила), организацией и выполнением технологического процесса работы подразделений железнодорожного транспорта, связанных с движением поездов.<p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene9"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene7"))

def ch1_scene9():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor5"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Нарушение графика движения поездов не допускается. В случаях нарушения графика движения поездов работники всех подразделений железнодорожного транспорта обязаны принимать оперативные меры для ввода в график опаздывающих поездов и обеспечивать их безопасное проследование.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
    st.button("Далее", type="primary", on_click = set_state("ch1_scene10"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene8"))


def ch1_scene10():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["tutor0"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>На железнодорожных путях необщего пользования владельцу железнодорожных путей необщего пользования допускается утверждать свой график движения поездов. В случае примыкания железнодорожных путей необщего пользования к инфраструктуре общего пользования или к железнодорожным путям необщего пользования графики движения поездов должны быть согласованы владельцем инфраструктуры и владельцем железнодорожных путей необщего пользования.</p></div>',
                unsafe_allow_html=True,
            )

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_scene11"))
    # st.button("Назад", type="primary", on_click = set_state("ch1_scene9"))

def ch1_scene11():

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["joke (1)"])
        st.write("")
    with col2:
        if st.session_state["ch1_scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Ты хорошо потрудился, должно быть ты устал, сделай перерыв, а пока вот тебе шутка \n\n— Проводник! Безобразие! Что у вас за поезд — только в него вошел, как у меня украли чемодан! \n\n— Ничего удивительного, наш поезд — скорый! \n\nМы хорошо провели время. Увидимся в следующем модуле!</p></div>', unsafe_allow_html=True)

            audio_file = open("game/audio/intro.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    st.button("Далее", type="primary", on_click = set_state("ch1_test1"))

def test1(): 
    st.title('Выбери все верные варианты:')
    a = st.multiselect("Инструкция по организации движения поездов и маневровой работы на железнодорожном транспорте Российской Федерации устанавливает:", 
                   [f:="правила приема, отправления и пропуска поездов", 
                    "правила конструирования поездов", 
                    s:="правила производства маневров",
                    t:="правила приема и отправления поездов в условиях выполнения   ремонтно-строительных работ ",
                    "внутренний интерьер вагонов"])
    
    if not set(a).difference([f, s, t]) and len(set(a)) == 3:
        st.button("Далее", type="primary", on_click = set_state("ch1_test2"))
    
def test2():
    st.title("Восстановите определение в правильном порядке")

    data = [
        {"id": "2", "order": 2, "name": "пользования к инфраструктуре общего пользования или к железнодорожным путям необщего пользования графики"},
        {"id": "1", "order": 1, "name": "допускается утверждать свой график движения поездов. В случае примыкания железнодорожных путей необщего"},
        {"id": "3", "order": 3, "name": "движения поездов должны быть согласованы владельцем инфраструктуры и владельцем железнодорожных путей необщего пользования"},
        {"id": "0", "order": 0, "name": "На железнодорожных путях необщего пользования владельцу железнодорожных путей необщего пользования"},
    ]

    slist = DraggableList(data, width="100%")
    if all([int(d["id"]) == d["order"] for d in slist]):
        st.button("Далее", type="primary", on_click = set_state("ch1_test3"))

def test3():
    st.title("Ответьте на вопрос")
    st.write("В каком порядке утверждается график движения поездов?")

    true_answer = "Сводный график движения поездов утверждается в порядке, определяемом федеральным органом исполнительной власти в области железнодорожного транспорта, на основании предложенных владельцами инфраструктур графиков движения поездов в пределах инфраструктур"

    answer = st.text_input('Ваш ответ: ')
    
    if st.button('Далее'):
        similarity = round(cos_similarity(
            get_embedding(lower_case(true_answer), tokenizer_sbert, model_sbert),
            get_embedding(lower_case(answer), tokenizer_sbert, model_sbert)
        ).item(), 2)

        if similarity > 0.5:
            st.write(f"Ваш ответ похож на истинный на {similarity * 100}%")
        else:
            st.write(f"Ваш ответ не похож на истинный на {100 - similarity * 100}%")

        with st.expander("Ответ"):
                st.write(true_answer)
