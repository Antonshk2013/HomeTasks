"""Создать функцию get_total_statistics, которая
 - принимает текст
 - и возвращает словарь в формате <буква: её количество в тексте>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint


def get_total_statistics(text: str) -> dict[str, int]:
    new_dict = {}
    for char in text.lower():
        if char.isalpha():
            new_dict[char] = new_dict.get(char, 0) + 1
    return new_dict

some_text = 'Bernard Shaw: "Life isn\'t about finding yourself. Life is about creating yourself."'
pprint(get_total_statistics(some_text))