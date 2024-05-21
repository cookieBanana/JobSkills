# задачи
# заполнить db_context (получает имя таблицы и строку) -> кладёт строку в таблицу
# заполнить hh_context (получает профессию или её синоним) -> вакансии


# пространство
from googletrans import Translator, constants
from pprint import pprint
import pandas as pd
import pymorphy3
import nltk
import psycopg2


#nltk.download('punkt')
#nltk.download('wordnet')
#morph = pymorphy2.MorphAnalyzer()


# станки заполненные

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def lemmatize(text):
    morph = pymorphy3.MorphAnalyzer()
    res = list()
    for word in text:
        p = morph.parse(word)[0]
        res.append(p.normal_form)
    return res


def find_lemmas_in_text(tok_lem_text, skills):
    result = []
    for lemma in tok_lem_text:
        if lemma in skills:
            result.append(lemma)
    return result


# 1.функция принимает слово и выдаёт его перевод
def translate_word(word):
    translator = Translator()
    return translator.translate(word, dest="ru").text


# 2.функция принимает массив слов и возвращает массив перевёднных слов (использует функцию 1)
def translate_text(words):
    #return [translate_word(word) for word in words]
    arr = []
    for word in words:
        arr.append(translate_word(word))
    return arr


# 19 найти новые навыки
def search_new_skills(vac_skills, find_skills):
    new_skills = []
    if len(vac_skills) < len(find_skills):
        for skill in find_skills:
            if skill not in vac_skills:
                new_skills.append(skill)


# станки пустые


# 3.создай пустую функцию добавиить_професиию_в_бд. Принимает русское название
def add_prof_inDB(prof):
    pass


# 4.создай пустую функцию добавить_синоним_к_профессии_в_бд. русское название профессии и синоним на русском языке
def add_syn_prof_inDB(prof, syn):
    pass


# 5.создай пустую функцию получть_профессии_и_синонимы_из_стандарта принимает ссылку на файл
def get_prof_and_syn_from_standart(file_path):
    df = pd.read_csv(file_path)
    preferredLabel = df[["preferredLabel", "altLabels"]]
    preferredLabel.altLabels = preferredLabel.altLabels.str.split('\n').apply(translate_text)
    preferredLabel.preferredLabel = preferredLabel.preferredLabel.apply(translate_word)

    return [preferredLabel.preferredLabel, preferredLabel.altLabels]


# 8.создать пустую функцию которая принимает профессию и её синонимы на русском и выдаёт список вакансий
def vacancies_list(prof, syns):
    vac_list = []
    return vac_list


# 9.создать пустую функцию которая принимает вакансию и выдаёт первичные навыки
def get_skills_from_vac(vac):
    skills_list = []
    return skills_list


# 10. создай пустую функцию, которая принимает навык и кладёт его в общий банк навыков
def add_skill_DB(skill):
    pass


# 12. создать функцию, которая возвращает все навыки из банка навыков
def get_skills():
    pass


# 13. создать пустую функцию, говорая возвращает все профессии
def get_profs():
    pass


# 14. создать пустую функуию, которая принимает профессию и возврщает все её синонимы
def get_syns_of_prof(prof):
    pass


# 15. создать пустую функуию, которая принимает профессию и возвращает все её вакансии
def get_vacs_of_prof(prof):
    pass


# 16. создать пустую функцию, которая принимает вакансию и возвращает её навыки
def get_skills_of_vac(vac):
    pass


# 17. создать пустую функцию, которая добавляет навык к вакансии
def add_skill_in_vac(skill, vac):
    pass


# 20.написать функцию пустую, которая принимает название профессии, и массив строк(параметры запроса к api hh)
#    и выдаёт список вакансий (пометить: нужен контроллер api hh)
def get_vacs_for_prof(prof, requestAPI):
    pass


# 21. написать функцию пустую, которая принимает вакансию и название професии и добавляет вакансию к профессии в бд (пометить: нужен контроллер бд)
def put_vac_in_prof(vac, prof):
    pass


# 22. написать функцию, которая по синониму выдаст назввание професии (пометить нужен контроллер бд)
def get_prof_by_syn(syn):
    pass


# classes

class Controller_api_hh:
    def __init__(self):
        pass


class Controller_db:
    conn = psycopg2.connect(dbname="hh_backup", user="postgres", password="12345", host="127.0.0.1", port="5432")

    def __init__(self):
        pass

    def create_table_if_not_exists(self, table_name, cols):
        cursor = self.conn.cursor()
        sql1 = "CREATE TABLE if not exists " + table_name + "("
        for index, col_name in enumerate(cols):
            if index < len(cols) - 1:
                sql1 += col_name + " " + cols[index] + ","
            elif index == len(cols) - 1:
                sql1 += col_name + " " + cols[index]
        sql1 += ");"
        cursor.execute(sql1)
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение

    def create_row(self, table_name, col_names, col_values):
        cursor = self.conn.cursor()
        sql1 = "INSERT INTO " + table_name + "("
        for index, col_name in enumerate(col_names):
            if index < len(col_names) - 1:
                sql1 += col_name + " ,"
            elif index == len(col_names) - 1:
                sql1 += col_name + " "
        sql1 += ") VALUES( "
        for index, col_value in enumerate(col_values):
            if index < len(col_values) - 1:
                sql1 += col_value + " ,"
            elif index == len(col_values) - 1:
                sql1 += col_value + " "
        sql1 += ");"
        cursor.execute(sql1)
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение

    def add_row_to_table(self, table_name, cols, value):
        self.create_table_if_not_exists(table_name, cols)
        self.create_row(table_name, cols, value)

    def get_all_table(self, table_name):
        pass

    def get_row_by_id(self, table_name, id):
        pass


class Vacancy:
    def __init__(self):
        pass


class Profession:
    def __init__(self):
        pass


class Skill:
    def __init__(self):
        pass


class Resume:
    def __init__(self):
        pass


# фабрика

# 11. создай функцию, которая принимает текст и выдаёт список навыков найденных в текст (ты уже делала это, там где поиск слов в тексте)
# функция, которая решает задачу. Берёт указнные данные, возвращает указанный результат
def find_skills_in_text(text, skills):
    lem_skills = lemmatize(skills)
    tok_text = tokenize_text(text)
    lem_text = lemmatize(tok_text)
    count_skills = find_lemmas_in_text(lem_text, lem_skills)
    return count_skills


# 6.создай функцию которая принимает профессию и её синонимы на английском. Она переводит (2), добавляет проф в бд (3), добавляет синонимы к проф (4)
def add_standart_to_DB(prof, syns):
    trans_prof = translate_word(prof)
    trans_syns = translate_text(syns)
    add_prof_inDB(trans_prof)
    add_syn_prof_inDB(trans_prof, trans_syns)


# 7.создать функцию которая принимает ссылку на файл. Получает список всех профессий и их синонимов(5) Сохраняет их в бд (6)
def save_in_DB(file_path):
    prof, syns = get_prof_and_syn_from_standart(file_path)
    add_standart_to_DB(prof, syns)


# 18. создать функцию которая получает все навыки из банка навыков (12) и получает все профессии (13),
#     1.запускается цикл, для каждой професии запрашивается список вакансий(15), и список уже найденных навыков (16),
#     2.запускается поиск навыков из общего банка навыков в тексте вакансии(11),
def update_skills_DB():
    # получение всех навыков и всех профессий
    all_skills = get_skills()
    all_profs = get_profs()

    prof_vacs = []
    vac_skills = []

    # итераиция по профессиям
    for prof in all_profs:
        prof_vacs = get_vacs_of_prof(prof)

        # итераиция по вакансиям
        for vac in prof_vacs:
            # загрузка старых скилов и поиск новых (с помощью поиск слов в тексте,
            # где слова это навыки из общего банканавыков)
            vac_skills = get_skills_of_vac(vac)

            text = vac.text()
            find_skills = find_skills_in_text(text, all_skills)

            # нахождение разницы(между старым набором навыков и набор найденным с помощью поиск слов в тексте,
            # где слова это навыки из общего банканавыков)
            # и сохранение новых скилов
            new_skills = search_new_skills(vac_skills, find_skills)
            for skill in new_skills:
                add_skill_in_vac(skill, vac)


def main():
    text = ["hellow", "my", "name", "is", "adelya"]
    trans_text = translate_text(text)
    print(trans_text)
    # пример один
    text = "красная"
    skills = ["красная"]
    print(find_skills_in_text(text, skills))
    # пример второй
    text = "пОпыт разработки под Bitrix24 Опыт разработки новых модулей Знание PHP, MYSQL, HTML, XML, CSS, JS (Ajax, JQuery) Понимание подсистем и модулей Bitrix и их взаимодействия Опыт работы с веб-сервисами (REST, SOAP), интеграции с внешними системами Опыт интеграции Bitrix со соронними системами и сервисами Навыки работы с системами контроля версий (Git)"
    skills = ["PHP", "MYSQL", "Bitrix", "XML", "CSS", "Git"]
    print(find_skills_in_text(text, skills))


main()
