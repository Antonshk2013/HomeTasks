"""Получить список всех имён селектора class,
используемых на заданной странице,
и выбрать из них 10 самых часто повторяющихся.
"""

import requests
from bs4 import BeautifulSoup
from collections import Counter


def find_most_common_classes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с атрибутом class
        # (Имя class зарезервировано в Python, поэтому BeautifulSoup
        # использует для своего параметра имя class_)
        elements_with_class = ...

        elements_with_class = soup.find_all(class_=True)
        all_classes = []
        for element in elements_with_class:
            all_classes.extend(element.get("class"))
        class_counter = Counter(all_classes)
        most_common_classes = class_counter.most_common(10)

        print("10 самых часто встречающихся классов:")
        for class_name, count in most_common_classes:
            print(f"Класс '{class_name}' встречается {count} раз")

    else:
        print(f"Ошибка при запросе: {response.status_code}")


URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
find_most_common_classes(URL)

# 10 самых часто встречающихся классов:
# Класс 'external' встречается 511 раз
# Класс 'text' встречается 510 раз
# Класс 'reference' встречается 266 раз
# Класс 'citation' встречается 253 раз
# Класс 'Z3988' встречается 253 раз
# Класс 'cs1' встречается 249 раз
# Класс 'mw-cite-backlink' встречается 247 раз
# Класс 'reference-text' встречается 247 раз
# Класс 'nowrap' встречается 236 раз
# Класс 'reference-accessdate' встречается 230 раз