# тут описаны все классы
# классы чаще всего используются tools, но могут быть использованы и в других местах
import psycopg2


class Controller_api_hh:
    def __init__(self):
        pass

    def get_vacancies_info(self, prof):
        pass

    def get_vacancies_info_from_sync(self, prof, sync):
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
        self.conn = psycopg2.connect(dbname="hh_backup", user="postgres", password="12345", host="127.0.0.1", port="5432")
        cursor = self.conn.cursor()
        sql1 = 'INSERT INTO "' + table_name + '"('
        for index, col_name in enumerate(col_names):
            if index < len(col_names) - 1:
                sql1 += '"'+col_name + '" ,'
            elif index == len(col_names) - 1:
                sql1 += '"'+col_name + '" '
        sql1 += ") VALUES( "
        for index, col_value in enumerate(col_values):
            if index < len(col_values) - 1:
                if(type(col_value) == type(" ")):
                    sql1 += " '"+str(col_value) + "' ,"
                elif (type(col_value) == type(1)):
                    sql1 += str(col_value) + ' ,'

                elif (type(col_value) == type([" ", " "])):
                    sql1 += " array [ "
                    index = 0
                    for i in col_value:
                        sql1 += " '"+str(i)+"' "
                        if index < len(col_value)-1:
                            sql1 += ","
                        index += 1
                    sql1 += "] ,"

            elif index == len(col_values) - 1:
                if (type(col_value) == type(" ")):
                    sql1 += " '"+str(col_value) + "' "

                elif (type(col_value) == type(1)):
                    sql1 += str(col_value) + ' '

                elif (type(col_value) == type([" ", " "])):
                    sql1 += " array [ "
                    index =0
                    for i in col_value:

                        sql1 += " '"+str(i)+"' "
                        if index < len(col_value)-1:
                            sql1 += ","
                        index += 1

                    sql1 += "]"

        sql1 += ");"
        print(sql1)
        cursor.execute(sql1)
        self.conn.commit()  # реальное выполнение команд sql1
        self.conn.close()  # закрываем подключение

    def add_row_to_table(self, table_name, cols, value):
        self.create_table_if_not_exists(table_name, cols)
        self.create_row(table_name, cols, value)

    def get_all_table(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * from "'+table_name+'"')
        result = cursor.fetchall()
        print(result)
        data = result
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение
        return data

    def get_row_by_id(self, table_name, id):
        postgreSQL_select_Query = 'select * from "'+ table_name +'" where "'+table_name+"_id"+"' = "+id
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        result = cursor.fetchall()
        print(result)
        data = result
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключение
        return data


        # DELETE FROM table_name WHERE table_name_id = value;
    def del_str_SQL(self, table_name, value):
        postgreSQL_select_Query = 'DELETE FROM "'+ table_name +'" where "'+table_name+'_id"'+' = '+value
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключени


        # UPDATE table_name SET column = value WHERE table_name_id = id;
    def change_value_SQL(self, table_name, column, table_name_id, id, value):
        postgreSQL_select_Query = 'UPDATE "'+ table_name +'" SET "'+column+'" = '+value+' WHERE "'+table_name_id+'" =' + id
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключени


        # SELECT * FROM table_name WHERE column1 = value1 AND column2 = value2 AND ...;
    def get_rows_by_values(self, table_name, column_array, value_array):
        postgreSQL_select_Query = 'SELECT * FROM "'+ table_name+'" WHERE '
        for index, col_name in enumerate(column_array):
            if index < len(column_array) - 1:
                postgreSQL_select_Query += ' "'+col_name + '" = ' + value_array[index] + ' AND '
            elif index == len(column_array) - 1:
                postgreSQL_select_Query += '"'+col_name + '" = ' + value_array[index] + ';'
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        result = cursor.fetchall()
        print(result)
        data = result
        self.conn.commit()  # реальное выполнение команд sql1
        cursor.close()  # закрываем курсор
        self.conn.close()  # закрываем подключени
        return data

class Vacancy:
    def __init__(self, vacancy_info):
        # get vacancy_detail from vacancy_info
        pass

    def get_skils(self):
        pass

    def save_in_db(self):
        # сохранит (Если нет такого в бд), с FK на профессию
        pass

    def add_skills(self):
        # добавить навык, который найден, не в метках
        pass

class Resume:
    def __init__(self, resume_info):
        # get resume_detail from vresume_info
        pass

    def get_skils(self):
        pass

    def save_in_db(self):
        # сохранит (Если нет такого в бд), с FK на профессию
        pass

    def add_skills(self):
        # добавить навык, который найден, не в метках
        pass




class Profession:
    Profession_id = 0
    Profession_Name =""
    Profession_synonyms = []
    def __init__(self,Profession_id, Profession_Name, Profession_synonyms):
        self.Profession_id = Profession_id
        self.Profession_Name = Profession_Name
        self.Profession_synonyms = Profession_synonyms


class Profession_storage:

    def __init__(self):
        pass



class Skill:
    def __init__(self):
        pass



