# тут описаны все станки
# классы чаще всего используются fabrics, но могут быть использованы и в других местах

# пространство
from googletrans import Translator, constants
from pprint import pprint
import pandas as pd
import pymorphy3
import nltk
import  classes_date

pd.options.mode.chained_assignment = None

controller_db = classes_date.Controller_db()

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
    print("test3./1", word)
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
    cols = ["Professions_name",]
    types = ["text"]
    controller_db.create_table_if_not_exists("Professions", cols, types)


# 4.создай пустую функцию добавить_синоним_к_профессии_в_бд. русское название профессии и синоним на русском языке
def add_syn_prof_inDB(prof, syn):
    pass


# 5.создай пустую функцию получть_профессии_и_синонимы_из_стандарта принимает ссылку на файл
def get_prof_and_syn_from_standart(file_path):
    df = pd.read_csv(file_path)
    prof = df[["preferredLabel", "altLabels"]]
    # prof["preferredLabel"]= prof["preferredLabel"].apply(translate_word)
    # prof["altLabels"] = prof["altLabels"].str.split('\n').apply(translate_text)
    return prof["preferredLabel"].tolist(), prof["altLabels"].tolist()


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

