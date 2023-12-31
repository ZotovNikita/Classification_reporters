from joblib import load


text_corpus = load('nlp/text_corpus.pkl')
id2text = load('nlp/id2text.pkl')
id2vec = load('nlp/id2vec.pkl')
id2topic = {
    "1": "ИНСТРУКЦИЯ ПО ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ И МАНЕВРОВОЙ РАБОТЫ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ",
    "1.1": "Общие требования к организации движения поездов на железнодорожном транспорте",
    "2": "ИНСТРУКЦИЯ ПО СИГНАЛИЗАЦИИ НА ЖЕЛЕЗНОДОРОЖНОМ ТРАНСПОРТЕ РОССИЙСКОЙ ФЕДЕРАЦИИ",
        "2.1": "Звуковые сигналы на железнодорожном транспорте",
        "2.2": "Общие положения",
        "2.3": "Правила применения семафоров",
        "2.4": "Ручные сигналы на железнодорожном транспорте",
        "2.5": "Светофоры на железнодорожном транспорте",
        "2.6": "Сигналы на железнодорожном транспорте",
        "2.7": "Сигналы ограждения на железнодорожном транспорте",
        "2.8": "Сигналы тревоги и специальные указатели",
        "2.9": "Сигналы, применяемые для обозначения поездов, локомотивов и другого железнодорожного подвижного состава",
        "2.10": "Сигналы, применяемые при маневренной работе",
        "2.11": "Сигнальные указатели и знаки на железнодорожном транспорте",
    "3": "ПОРЯДОК ДВИЖЕНИЯ СПЕЦИАЛЬНОГО ПОДВИЖНОГО СОСТАВА НА КОМБИНИРОВАННОМ ХОДУ",
        "3.1": "Действия при возникновении аварийной или нестандартной ситуации при движении СПК по железнодорожным путям",
        "3.2": "Общие положения",
        "3.3": "Организация движения СПК на железнодорожной станции",
        "3.4": "Организация движения СПК на перегоне",
    "4": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ НА УЧАСТКАХ, ОБОРУДОВАННЫХ АВТОМАТИЧЕСКОЙ БЛОКИРОВКОЙ",
        "4.1": "Действия при неисправностях автоматической блокировки",
        "4.2": "Общие положения",
        "4.3": "Прекращение и восстановление действия автоматической блокировки",
        "4.4": "Прием и отправление поездов",
    "5": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ НА УЧАСТКАХ, ОБОРУДОВАННЫХ АВТОМАТИЧЕСКОЙ ЛОКОМОТИВНОЙ СИГНАЛИЗАЦИЕЙ, ПРИМЕНЯЕМОЙ КАК САМОСТОЯТЕЛЬНАЯ СИСТЕМА ИНТЕРВАЛЬНОГО РЕГУЛИРОВАНИЯ ДВИЖЕНИЯ ПОЕЗДОВ",
        "5.1": "Общие положения",
        "5.2": "Прием и отправление поездов",
    "6": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ НА УЧАСТКАХ, ОБОРУДОВАННЫХ ПОЛУАВТОМАТИЧЕСКОЙ БЛОКИРОВКОЙ",
        "6.1": "Движение поездов при неисправности полуавтоматической блокировки",
        "6.2": "Прием и отправление поездов",
    "7": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ НА УЧАСТКАХ, ОБОРУДОВАННЫХ ЭЛЕКТРОЖЕЗЛОВОЙ СИСТЕМОЙ",
        "7.1": "Движение поездов при наличии примыканий на перегоне",
        "7.2": "Движение поездов при неисправности электрожезловой системы и порядок регулировки количества жезлов в жезловых аппаратах",
        "7.3": "Общие положения",
        "7.4": "Прием и отправление поездов",
    "8": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ ПРИ ВОЗНИКНОВЕНИИ АВАРИЙНЫХ И НЕСТАНДАРТНЫХ СИТУАЦИЙ НА ПЕРЕГОНЕ",
        "8.1": "Возвращение поезда с перегона на железнодорожную станцию",
        "8.2": "Оказание помощи остановившемуся на перегоне поезду локомотивом сзади идущего поезда",
        "8.3": "Отправление восстановительных, пожарных поездов, специального самоходного подвижного состава и вспомогател",
    "9": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ ПРИ ИСПОЛЬЗОВАНИИ ТЕЛЕФОННЫХ СРЕДСТВ СВЯЗИ",
        "9.1": "Ведение журнала поездных телефонограмм",
        "9.2": "Общие положения",
        "9.3": "Телефонограммы при движении поездов на двухпутных участках",
        "9.4": "Телефонограммы при движении поездов на однопутных участках",
    "10": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ ПРИ ПЕРЕРЫВЕ ДЕЙСТВИЯ ВСЕХ СИСТЕМ ИНТЕРВАЛЬНОГО РЕГУЛИРОВАНИЯ ДВИЖЕНИЯ ПОЕЗДОВ И СВЯЗИ",
        "10.1": "Движение поездов на двухпутных перегонах",
        "10.2": "Движение поездов на однопутных перегонах",
        "10.3": "Общие положения",
    "11": "ПОРЯДОК ОРГАНИЗАЦИИ МАНЕВРОВОЙ РАБОТЫ",
        "11.1": "Маневровая работа в районах железнодорожных станций не обслуживаемых дежурными стрелочных постов",
        "11.2": "Маневры на главных и приемоотправочных железнодорожных путях",
        "11.3": "Маневры на сортировочных горках и вытяжных железнодорожных путях",
        "11.4": "Общие положения",
        "11.5": "Обязанности работников, участвующих в производстве маневров",
        "11.6": "Руководство маневровой работой",
        "11.7": "Скорости при маневрах",
    "12": "ПОРЯДОК ОРГАНИЗАЦИИ ПРИЕМА И ОТПРАВЛЕНИЯ ПОЕЗДОВ, В ТОМ ЧИСЛЕ НА УЧАСТКАХ, ОБОРУДОВАННЫХ СИСТЕМОЙ ТЕЛЕУПРАВЛЕНИЯ",
        "12.1": "Общие положения",
        "12.2": "Отправление поездов",
        "12.3": "Прием поездов на железнодорожную станцию при запрещающем показании входного светофора",
        "12.4": "Прием поездов",
    "13": "ПОРЯДОК ПРОИЗВОДСТВА МАНЕВРОВОЙ РАБОТЫ, ФОРМИРОВАНИЯ И ПРОПУСКА ПОЕЗДОВ С ВАГОНАМИ, ЗАГРУЖЕННЫМИ ОПАСНЫМИ ГРУЗАМИ КЛАССА 1 (ВЗРЫВЧАТЫМИ МАТЕРИАЛАМИ)",
        "13.1": "Действия в аварийных ситуациях",
        "13.2": "Общие положения",
        "13.3": "Следование поездов с взрывчатым",
        "13.4": "Формирование поездов",
    "14": "ПРАВИЛА ТЕХНИЧЕСКОЙ ЭКСПЛУАТАЦИИ ЖЕЛЕЗНЫХ ДОРОГ РОССИЙСКОЙ ФЕДЕРАЦИИ",
        "14.1": "Обслуживание сооружений и устройств железнодорожного транспорта",
        "14.2": "Общие положения",
        "14.3": "Обязанности работников железнодорожного транспорта",
        "14.4": "Организация эксплуатации технологических систем, сооружений, устройств и объектов технического назначения желез",
        "14.5": "Системы и устройства железнодорожной автоматики и телемеханики",
        "14.6": "Сооружения и устройства железнодорожного электроснабжения",
        "14.7": "Сооружения и устройства путевого хозяйства",
        "14.8": "Техническая эксплуатация железнодорожного подвижного состава",
        "14.9": "Устройства технологической железнодорожной электросвязи",
    "15": "ТИПОВЫЕ ТРЕБОВАНИЯ К ВЕДЕНИЮ РЕГЛАМЕНТА СЛУЖЕБНЫХ ПЕРЕГОВОРОВ",
        "15.1": "Ведение регламента служебных переговоров между машинистом и помощником машиниста",
        "15.2": "Ведение регламента служебных переговоров при закреплении железнодорожного подвижного состава",
        "15.3": "Ведение служебных переговоров при организации движения поездов",
        "15.4": "Ведение служебных переговоров при организации маневровой работы",
        "15.5": "Общие положения",
    "16": "ОСНОВНЫЕ ПОЛОЖЕНИЯ О ПОРЯДКЕ ДВИЖЕНИЯ ДРЕЗИН СЪЕМНОГО ТИПА",
    "17": "ПОРЯДОК ЗАКРЕПЛЕНИЯ ЖЕЛЕЗНОДОРОЖНОГО ПОДВИЖНОГО СОСТАВА",
    "18": "ПОРЯДОК НАЗНАЧЕНИЯ И ПЕРЕДАЧИ ПРЕДУПРЕЖДЕНИЙ",
    "19": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ПОЕЗДОВ С РАЗГРАНИЧЕНИЕМ ВРЕМЕНЕМ",
    "20": "ПОРЯДОК ОРГАНИЗАЦИИ ДВИЖЕНИЯ ХОЗЯЙСТВЕННЫХ ПОЕЗДОВ ПРИ ПРОИЗВОДСТВЕ РЕМОНТНЫХ И СТРОИТЕЛЬНЫХ РАБОТ НА ЖЕЛЕЗНОДОРОЖНОЙ ИНФРАСТРУКТУРЕ",
    "21": "ПОРЯДОК ОРГАНИЗАЦИИ ПРИЕМА, ОТПРАВЛЕНИЯ ПОЕЗДОВ И ПРОИЗВОДСТВА МАНЕВРОВ В УСЛОВИЯХ НАРУШЕНИЯ РАБОТОСПОСОБНОГО СОСТОЯНИЯ УСТРОЙСТВ ЖЕЛЕЗНОДОРОЖНОЙ АВТОМАТИКИ И ТЕЛЕМЕХАНИКИ НА ЖЕЛЕЗНОДОРОЖНЫХ СТАНЦИЯХ",
    "22": "ПОРЯДОК ОРГАНИЗАЦИИ РАБОТЫ ДИСПЕТЧЕРА ПОЕЗДНОГО",
    "23": "ПОРЯДОК ПОСТАНОВКИ В ПОЕЗДА ВАГОНОВ С ГРУЗАМИ, ТРЕБУЮЩИМИ ОСОБЫХ УСЛОВИЙ ПЕРЕВОЗКИ И СПЕЦИАЛЬНОГО ЖЕЛЕЗНОДОРОЖНОГО ПОДВИЖНОГО СОСТАВА",
}

if __name__ == "__main__":
    from pathlib import Path
    import os
    import sys

    sys.path.append(str(Path(os.getcwd())))


    from model.sbert import model_sbert, tokenizer_sbert
    from utils.find_sentences import find_sentences
    from utils.find_top_k_sentences import find_top_k_sentences
    from model.rut5_base_sum_gazeta import model_sum, tokenizer_sum
    from utils.summarization import summarization

    id = 22
    print(id2text[id])
    print("1------------------------------------")
    query = 'Работники железнодорожного транспорта, не прошедшие аттестацию, не допускаются к выполнению определенных работ.'
    print(find_sentences(query, id2text, id2vec, tokenizer_sbert, model_sbert))
    print("2------------------------------------")
    article_text = ' '.join(find_top_k_sentences(query, id2text, id2vec, tokenizer_sbert, model_sbert, 5))
    print(article_text)
    print("3------------------------------------")
    print(summarization(query + article_text , tokenizer_sum, model_sum))
