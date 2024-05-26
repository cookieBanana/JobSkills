# тут описаны все классы
# классы чаще всего используются tools, но могут быть использованы и в других местах
import psycopg2


class Controller_api_hh:
    def __init__(self):
        pass

    # перенести
    def get_vacancies(self, profeccion):
        pass

    # перенести
    def get_vacancy_info(self, vacancy):
        pass

    def get_skills(self, vacancy_info):
        pass


class Controller_db:
    conn = psycopg2.connect(dbname="hh_backup", user="postgres", password="12345", host="127.0.0.1", port="5432")

    def __init__(self):
        pass

    def create_table_if_not_exists(self, table_name, cols, types):
        cursor = self.conn.cursor()
        sql1 = 'CREATE TABLE if not exists "' + table_name + '"('
        sql1 += '"' + table_name + '_id' + '" bigserial primary key,'
        for index, col_name in enumerate(cols):
            if index < len(cols) - 1:
                sql1 += '"' + col_name + '" ' + types[index] + ","
            elif index == len(cols) - 1:
                sql1 += '"'+ col_name + '" ' + types[index]
        sql1 += ");"
        print("sql1", sql1)
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
        cursor = self.conn.cursor()
        cursor.execute("SELECT * from '"+table_name+"'")
        result = cursor.fetchall()
        print(result)
        data = result
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение
        return data

    def get_row_by_id(self, table_name, id):
        postgreSQL_select_Query = "select * from '"+ table_name +"' where '"+table_name+"_id"+"' = "+id
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        result = cursor.fetchall()
        print(result)
        data = result
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение
        return data

class Vacancy:
    def __init__(self):
        pass


class Profession:
    Profession_id = 0
    Profession_Name =""
    def __init__(self,Profession_id,Profession_Name):
        self.Profession_id = Profession_id
        self.Profession_Name = Profession_Name


class Skill:
    def __init__(self):
        pass


class Resume:
    def __init__(self):
        pass

