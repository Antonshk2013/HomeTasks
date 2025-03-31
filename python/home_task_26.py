"""1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py или запускает его.
При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует или
не может быть запущен, программа должна вывести соответствующее сообщение об ошибке."""
import os
from typing import Any

def execute_file(paht: str)-> Any:
    try:
        os.system(f'python {paht}')
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")


"""2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории или выводит 
список всех файлов или поддиректорий внутри этой директории. Для этой задачи используйте модуль os или его функцию 
walk. Программа должна выводить полный путь к каждому файлу или директории."""

def wolk_dirrectory(path: str) -> Any:
    dir_a = os.walk(path)
    _, list_dir, list_files = next(dir_a)
    for dir in list_dir:
        file_path = os.path.dirname(os.path.abspath(dir))
        print(f'[FILE] {file_path}/{dir}')
    for file in list_files:
        file_path = os.path.dirname(os.path.abspath(file))
        print(f'[FILE] {file_path}/{file}')


if __name__ == '__main__':
    # execute_file('additional_files/file_26_1.py')
    # execute_file('additional_files/file_26_1.py')
    # wolk_dirrectory('additional_files/file_26_1')
    path = ".."
    wolk_dirrectory(path)
