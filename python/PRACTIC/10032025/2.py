"""Создать функцию get_statistics_by_words, которая
 - принимает текст
 - и возвращает словарь в формате <буква: [её количество в каждом слове, где есть хотя бы одна]>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint
import string


def get_statistics_by_words(text: str)-> dict[str, list[str]]:
    new_dict = {letter: 0 for letter in string.ascii_lowercase}
    for char in text.lower():
        if char in string.ascii_lowercase:
            new_dict.update({char: new_dict[char] + 1})
    return new_dict

def get_statistics_by_words1(text: str)-> dict[str, list[str]]:
    new_dict = {letter: [] for letter in string.ascii_lowercase}
    for char in text.lower():
        if char in string.ascii_lowercase:
            new_dict.update({char: new_dict[char].append(1)})
    return new_dict


if __name__ == '__main__':
    text = 'Mark Twain: "I have never let my schooling interfere with my education.""'
    pprint(get_statistics_by_words(text))
    pprint(get_statistics_by_words1(text))