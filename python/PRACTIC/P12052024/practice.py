"""В базе данных ich_edit три таблицы:
    Users с полями (id, name, age),
    Products с полями (pid, prod, quantity) и
    Sales с полями (sid, id, pid).

Дан список с именами таблиц.
Программа должна в цикле сделать запрос к каждой из указанных таблиц.
Если таблица есть в базе - вывести на печать её содержимое.
Если нет - вывести сообщение:"The table {table_name} does not exist!"
"""


import mysql.connector
from local_settings import HOST, USER, PASSWORD, DATABASE

dbconfig = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

connection = mysql.connector.connect(**dbconfig)

class Table:
    def __init__(self, table_name):
        self.table_name = table_name


    def get_all_data(self):
        try:
            connection = mysql.connector.connect(**dbconfig)
            cursor = connection.cursor()
            # colums = cursor.description
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()
        except:
            return f"The table {self.table_name} does not exist!"


if __name__ == '__main__':
    users = Table('Users')
    products = Table('Products')
    sales = Table('Sales')
    print(users.get_all_data())
    print(products.get_all_data())
    print(sales.get_all_data())






#  ===== Table 'Users': =====
# (1, 'John Doe', 30)
#  ===== Table 'Products': =====
# (1, 'Laptop', 20)
#  ===== Table 'Sales': =====
# (1, 1, 1)
# Тhe table <No_name> does not exist!