'''
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity)
и Sales с полями (sid, id, pid).
Программа должна запросить у пользователя название таблицы и вывести все ее строки или сообщение, что такой таблицы нет.
'''
from pprint import pprint

import mysql.connector
from local_settings import *

import mysql.connector
dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

def get_all_data(table_name: str):
    try:
        connection = mysql.connector.connect(**dbconfig)
        cursor = connection.cursor()
        cursor.execute(f'select * from {table_name}')
        result = cursor.fetchall()
        cursor.close()
        return result
    except:
        return f"The table {table_name} does not exist!"

'''
В базе данных ich_edit три таблицы. 
Users с полями (id, name, age), 
Products с полями (pid, prod, quantity) 
Sales с полями (sid, id, pid).

Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и вывести все покупки этого 
пользователя.
'''

def show_all_sales_by_user(user_id: int):
    table_name = "Sales"
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f'select * from {table_name} where id={user_id}')
    result = cursor.fetchall()
    cursor.close()
    pprint(result)

def show_all_users():
    table_name = "Users"
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f'select * from {table_name}')
    result = cursor.fetchall()
    cursor.close()
    pprint(result)

def main():
    print("Start")
    show_all_users()
    usrer_id = int(input("Enter User_id: "))
    show_all_sales_by_user(usrer_id)
    print("End")

if __name__ == '__main__':
    # print(get_all_data('Users'))
    main()