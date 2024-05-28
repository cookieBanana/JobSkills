# тут описаны все заводы
# классы чаще всего используются main, но могут быть использованы и в других местах
import classes_date
import tools
import  multiprocessing

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
    prof_obj = classes_date.Profession(1, prof[1], )
    tools.add_prof_inDB(prof_obj)

    # for x in range(len(prof)):

        #print(prof[x], syns[x])


    #tools.add_syn_prof_inDB(trans_prof, trans_syns)


# 7.создать функцию которая принимает ссылку на файл. Получает список всех профессий и их синонимов(5) Сохраняет их в бд (6)
def prof_csv_to_bd(file_path):
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


#перевести данные
def f(i,data_for_worker_item,return_dict):
    rus_data_for_worker_item = []
    local_i = i*20
    for x in data_for_worker_item:
        trans_prof = tools.translate_word(x[0][0])
        trans_syns = tools.translate_text(x[1])[0].split("\n")
        db_context = classes_date.Controller_db()
        print(trans_syns)
        db_context.create_row("Professions", ["Professions_id", "Professions_name", "Profession_syn"],[local_i, trans_prof, trans_syns])

        return_dict[local_i] = [trans_prof]
        local_i+=1



# создаст df, потом разрежит его на 1000 частей
# каждую часть даст процессу, процесс положит в бд
def esco_to_array(file):
    names, alt_names = tools.get_prof_and_syn_from_standart(file)
    data_for_worker = []
    # разделить на кусочки размером 20 names
    print(len(names))
    data_for_worker_item = []
    local_i = 0
    for i in range(len(names)):
        local_i +=1
        data_for_worker_item.append([[names[i]], [alt_names[i]]])
        if (local_i % 20 == 0 and local_i > 0) or (i == len(names) -1):
            data_for_worker.append(data_for_worker_item)
            data_for_worker_item = []
            local_i = 0

    # q = multiprocessing.Queue()
    # pool = multiprocessing.Pool() #use all available cores, otherwise specify the number you want as an argument
    # for x in range(1):
    #    pool.apply_async(f, args=(data_for_worker[x], 1))
    # pool.close()
    # pool.join()

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(len(data_for_worker)):
        p = multiprocessing.Process(target=f, args=(i,data_for_worker[i],return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    result = return_dict.values()
    for item in result:
        print("ITEM", item)
    print("ITs rus_data_for_worker_item")


