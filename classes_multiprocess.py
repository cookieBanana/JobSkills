import multiprocessing as mp

#создать поток, который принимает на вход фунцию
# должен паралельно складывать профессии, синонимы, вакансии, навыки в бд


#Создать асбтрактного worker и унаследовать конкретные
class controller_mulrtiproc:
    def __init__(self):
        pass

    def create_worker(self, count, body):
        pass


class Abstract_worker:
    def __init__(self):
        pass



# принимает table_name, obj, command (create, insert, update, delete)
# работает с бд, использует context_bd
class sender_bd:
    def __init__(self):
        pass

# принимает name(prof or synonim)
# работает с hh, использует context_hh
class sender_hh:
    def __init__(self):
        pass

