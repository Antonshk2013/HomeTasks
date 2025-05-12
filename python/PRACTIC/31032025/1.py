"""Создайте zip-объект (zip_obj) из двух списков:
    - списка индексов значений и
    - списка самих значений.
Убедитесь, что функция zip действительно возвращает итератор.
Распечатайте результат - каждая пара в новой строке.

Объект zip-ob является итератором: True

Дополнительное условие: всё решение должно занимать не более 3-x строк:
 1. Создание объекта zip_obj
 2. Проверка является ли zip_obj итератором? (True или False)
 3. Вывод на печать zip-пар (каждая пара - в новой строке)
"""
import zipfile
from typing import Iterator

my_list = ['apple', 'banana', 'cherry', 'date']

zip_obj = zip([my_list.index(x) for x in my_list], my_list)
print(zip_obj)
print(f"Объект zip-ob является итератором: {isinstance(zip_obj, Iterator)}")
print(*zip_obj, sep='\n')

# Объект zip-ob является итератором: True
# (0, 'apple')
# (1, 'banana')
# (2, 'cherry')
# (3, 'date')