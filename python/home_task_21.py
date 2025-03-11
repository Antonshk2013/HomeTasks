from collections import *
"""1. Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте и выводит на экран 
наиболее часто встречающиеся слова. Для решения задачи используйте класс Counter из модуля collections. 
Создайте функцию count_words, которая принимает текст в качестве аргумента и возвращает словарь с количеством 
вхождений каждого слова. Выведите наиболее часто встречающиеся слова и их количество.

Пример вывода:
Введенный текст: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est.
sed: 2
Lorem: 1
"""
def count_words(text: str) -> str:
    return Counter(text.lower().replace(".", '').replace(',','').split()).most_common(2)
"""
2. Напишите программу, которая создает именованный кортеж Person для хранения информации о человеке, включающий поля 
name, age и city. Создайте список объектов Person и выведите информацию о каждом человеке на экран.

Пример вывода:
Name: Alice, Age: 25, City: New York
Name: Bob, Age: 30, City: London
Name: Carol, Age: 35, City: Paris
"""

def print_person_data(*person_data: list) -> None:
    for person in person_data:
        print(f"Name: {person.name}, Age: {person.age}, City: {person.city}")

"""
3. Напишите программу, которая принимает словарь от пользователя и ключ, и возвращает значение для указанного 
ключа с использованием метода get или setdefault. Создайте функцию get_value_from_dict, которая принимает словарь 
и ключ в качестве аргументов, и возвращает значение для указанного ключа, используя метод get или setdefault в 
зависимости от выбранного варианта. Выведите полученное значение на экран.

Пример словаря:
my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
Пример вывода:

Введите ключ для поиска: banana
Использовать метод get (y/n)? y
Значение для ключа 'banana': 6
"""

def get_value_from_dict(my_dict: dict, key: str, is_get: bool) -> str:
    if is_get:
        return my_dict.get(key)
    return my_dict.setdefault(key, 0)

if __name__ == '__main__':
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed lacinia est."
    print(count_words(text))

    Person = namedtuple('Person', ['name', 'age', 'city'])
    person1 = Person(name='Alice', age=30, city='New York')
    person2 = Person(name='Bob', age=30, city='London')
    person3 = Person(name='Carol', age=35, city='Paris')
    print_person_data(person1, person2, person3)

    my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
    print(get_value_from_dict(my_dict, 'apple', False))
