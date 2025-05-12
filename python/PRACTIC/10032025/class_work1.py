"""Словарь синонимов.
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Написать функцию, которая для заданного слова из словаря, определяет его синоним.

Пример словаря:
    dct = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

    get_synonym(“Goodbye”) -> Bye.
    get_synonym(“Plate) -> THe word <Plate> was not found in the dictionary!
"""
from pprint import pprint


def get_synonym(synonyms: dict, word: str) -> str:
    if synonyms.get(word):
        return synonyms.get(word)
    else:
        for key in synonyms:
            if synonyms.get(key) == word:
                return key
    return f'THe word <{word}> was not found in the dictionary!'


# words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
#
# print(get_synonym(words, "Goodbye"))  # Bye
# print(get_synonym(words, "List"))     # Array
# print(get_synonym(words, "Plate"))    # Word <Plate> was not found in the dictionary!


""" 02 ===========================================================================

Дан json-файл 'cities-countries.json', в котором
по ключу <Страна> находится строка с названиями городов, разделённых пробелом.

Напишите функцию, которая:
 - считывает данные из файла;
 - по аргументу ГОРОД возвращает
    - либо название страны
    - либо "not found"

which_country("Novgorod") = Russia
which_country("Mumbai") = Not found

"""
import json


def read_json_file(filename: str) -> dict[str, str]:
    with open(filename, "r", encoding="utf-8") as f:
        city = json.load(f)
        return city


def which_country(city: str) -> str:
    citys_dict = read_json_file('cities-countries.json')

    for country, citys in citys_dict.items():
        if city in citys_dict.get(country):
            return country

    return "Not found"


#
# print(which_country("Novgorod"))   # Russia
# print(which_country("Turin"))      # Italy
# print(which_country("Mumbai"))     # Not found



"""Дана база данных о продажах некоторого интернет-магазина.
Каждая строка файла 'sales.json' представляет собой запись вида
покупатель-товар-количество, где
    покупатель — имя покупателя (строка без пробелов),
    товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных
им единиц каждого вида товаров.
Список покупателей, а также список товаров для каждого покупателя
нужно выводить в лексикографическом порядке.

Данные:
[
    "Alice-apple-5",
    "Alice-orange-3",
    "Bob-apple-2",
    "Bob-banana-7",
    "Alice-banana-2",
    "Charlie-apple-1
]

Пример вывода:
    {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
     'Bob': {'apple': 2, 'banana': 7},
     'Charlie': {'apple': 1}}
"""
import json
from pprint import pprint


def read_list_from_json_file(filename: str) -> dict[str, str]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


def process_sales_data(filename: str) -> dict[str, dict[str, int]]:
    data = sorted(read_list_from_json_file(filename))
    pprint(data)
    pass

sales_dict = process_sales_data('sales.json')

pprint(sales_dict)

# {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
#  'Bob': {'apple': 2, 'banana': 7},
#  'Charlie': {'apple': 1}}
