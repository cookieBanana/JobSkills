# задачи
# заполнить db_context (получает имя таблицы и строку) -> кладёт строку в таблицу
# заполнить hh_context (получает профессию или её синоним) -> вакансии
import fabrics
import tools


def main():
    # text = ["hellow", "my", "name", "is", "adelya"]
    # trans_text = tools.translate_text(text)
    # print(trans_text)
    # # пример один
    # text = "красная"
    # skills = ["красная"]
    # print(fabrics.find_skills_in_text(text, skills))
    # # пример второй
    # text = "пОпыт разработки под Bitrix24 Опыт разработки новых модулей Знание PHP, MYSQL, HTML, XML, CSS, JS (Ajax, JQuery) Понимание подсистем и модулей Bitrix и их взаимодействия Опыт работы с веб-сервисами (REST, SOAP), интеграции с внешними системами Опыт интеграции Bitrix со соронними системами и сервисами Навыки работы с системами контроля версий (Git)"
    # skills = ["PHP", "MYSQL", "Bitrix", "XML", "CSS", "Git"]
    # print(fabrics.find_skills_in_text(text, skills))


    # получить список всех профессий
    # перевести, поместить в бд
    # получить синонимы
    path = "P:\\diploma_a\\esco_dataset\\ESCO dataset - v1.1.2 - classification - en - csv\\occupations_en.csv"
    print("test")
    fabrics.save_in_DB(path)


main()


