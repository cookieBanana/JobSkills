# тут описаны все заводы
# классы чаще всего используются main, но могут быть использованы и в других местах
import classes
import tools

# фабрика

# 11. создай функцию, которая принимает текст и выдаёт список навыков найденных в текст (ты уже делала это, там где поиск слов в тексте)
# функция, которая решает задачу. Берёт указнные данные, возвращает указанный результат
def find_skills_in_text(text, skills):
    lem_skills = tools.lemmatize(skills)
    tok_text = tools.tokenize_text(text)
    lem_text = tools.lemmatize(tok_text)
    count_skills = tools.find_lemmas_in_text(lem_text, lem_skills)
    return count_skills


# 6.создай функцию которая принимает профессию и её синонимы на английском. Она переводит (2), добавляет проф в бд (3), добавляет синонимы к проф (4)
def add_standart_to_DB(prof, syns):
    # trans_prof = tools.translate_word(prof)
    # trans_syns = tools.translate_text(syns)
    prof_obj = classes.Profession(1, prof[1], )
    tools.add_prof_inDB(prof_obj)

    # for x in range(len(prof)):

        #print(prof[x], syns[x])


    #tools.add_syn_prof_inDB(trans_prof, trans_syns)


# 7.создать функцию которая принимает ссылку на файл. Получает список всех профессий и их синонимов(5) Сохраняет их в бд (6)
def save_in_DB(file_path):
    prof, syns = tools.get_prof_and_syn_from_standart(file_path)
    print("save_in_DB", prof )
    add_standart_to_DB(prof, syns)


# 18. создать функцию которая получает все навыки из банка навыков (12) и получает все профессии (13),
#     1.запускается цикл, для каждой професии запрашивается список вакансий(15), и список уже найденных навыков (16),
#     2.запускается поиск навыков из общего банка навыков в тексте вакансии(11),
def update_skills_DB():
    # получение всех навыков и всех профессий
    all_skills = tools.get_skills()
    all_profs = tools.get_profs()

    prof_vacs = []
    vac_skills = []

    # итераиция по профессиям
    for prof in all_profs:
        prof_vacs = tools.get_vacs_of_prof(prof)

        # итераиция по вакансиям
        for vac in prof_vacs:
            # загрузка старых скилов и поиск новых (с помощью поиск слов в тексте,
            # где слова это навыки из общего банканавыков)
            vac_skills = tools.get_skills_of_vac(vac)

            text = vac.text()
            find_skills = find_skills_in_text(text, all_skills)

            # нахождение разницы(между старым набором навыков и набор найденным с помощью поиск слов в тексте,
            # где слова это навыки из общего банканавыков)
            # и сохранение новых скилов
            new_skills = tools.search_new_skills(vac_skills, find_skills)
            for skill in new_skills:
                tools.add_skill_in_vac(skill, vac)