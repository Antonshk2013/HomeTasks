"""Считать текст из файла anna-karenina.txt,
обработать его, и в итоге вернуть итератор,
состоящий из слов длиной более десяти символов.
"""
from typing import Iterator


def read_file(file_path: str) -> str:
    """
    Читает содержимое файла и возвращает его в виде строки.

    :param file_path: Путь к файлу.
    :return: Текст из файла.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def clean_word(word: str) -> str:
    """
    Очищает слово от небуквенных символов.

    :param word: Исходное слово.
    :return: Очищенное слово, содержащее только буквы.
    """
    world = ''.join(ch for ch in word if ch.isalpha())
    return world


def clean_and_split(text: str) -> Iterator[str]:
    """
    Приводит текст к нижнему регистру, разбивает на слова и очищает их.

    :param text: Исходный текст.
    :return: Итератор очищенных слов.
    """

    text = text.replace('-', ' ').split(' ')

    return text



def filter_long_words(words: Iterator[str]) -> Iterator[str]:
    """
    Фильтрует слова, оставляя только те, длина которых больше 10 символов.

    :param words: Итератор слов.
    :return: Итератор слов, длина которых превышает 10 символов.
    """
    if len(words) > 10:
        return True
    return False





def process_text(file_path: str) -> Iterator[str]:
    """
    Обрабатывает текст из файла:
    - Читает файл.
    - Разбивает текст на слова и очищает их.
    - Фильтрует слова длиной более 10 символов.

    :param file_path: Путь к файлу.
    :return: Итератор отфильтрованных слов.
    """
    file_text = read_file(file_path)
    file_list = clean_and_split(file_text)
    clean_file_text = [clean_word(file) for file in file_list]
    clean_long_words = (world for world in clean_file_text if len(world)>10)
    return clean_long_words




# несчастливая
# несчастлива
# француженкою
# гувернанткой
# продолжалось
# ...

if __name__ == '__main__':
    file_path = 'anna-karenina.txt'
    long_words = process_text(file_path)
    print(*long_words, sep='\n')
