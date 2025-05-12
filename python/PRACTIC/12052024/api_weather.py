from pprint import pprint
import requests
from local_settings import WEATHER_API_KEY

def get_weather(location):
    url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': WEATHER_API_KEY,
        'q': location,
        'aqi': 'no'}

    resp = requests.get(url, params=params)
    print(resp.status_code)
    return resp.json()


"""
В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales с
полями (sid, id, pid). Написать мини-интерфейс к базе данных, который умеет выполнять разные команды.
Выбрать таблицу для запроса. 

1.) Предусмотреть возможность выбрать несколько таблиц. Вывести результат их соединения, если это возможно, или
 сообщение об ошибке.

2.) Выбрать одно поле из выбранной таблицы и искомое значение этого поля. Вывести все подходящие строки"""


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
    def __init__(self, table_name, colums):
        self.table_name = table_name
        self.colums = colums

    def __str__(self):
        return f"{self.table_name} {' '.join(self.colums)}"

    def select(self, colums="*"):
        try:
            connection = mysql.connector.connect(**dbconfig)
            cursor = connection.cursor()
            # colums = cursor.description
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()
        except:
            return f"The table {self.table_name} does not exist!"
        if colums == "*":

            return

if __name__ == '__main__':
    pprint(get_weather('Rostock'))