"""Напишите программу, которая принимает в качестве аргумента командной строки
 путь к директории и выводит список всех файлов с расширением .txt
 внутри этой директории и ее поддиректорий.
Для этой задачи используйте рекурсивную функцию, которая будет обходить
все поддиректории и искать файлы с расширением .txt.

start_directory:  /home/su/PythonProjects/IT_career_hub/Python_Morning
    [FILE]        2868  practice_tasks_07.txt
    [FILE]        2980  practice_work_08.txt
    [FILE]        3399  tasks.txt
    [FILE]          38  persons.txt
        [FILE]          27  output.txt
        [FILE]          26  input.txt
        [FILE]        1280  triangle_pascale.txt
        [FILE]         238  article.txt
    [FILE]          27  output.txt
    [FILE]        1280  pascal_triangle.txt
    [FILE]          26  input.txt
    [FILE]        1280  triangle_pascale.txt
"""
import os



def list_directory(path):
    for root, dirs, files in os.walk(path):
        dirs.sort()  # Sort directories alphabetically in ascending order
        level = root.replace(path, '').count(os.sep) # counts the number of directory separators, thus giving depth level)
        indent = '    ' * level
        print(f"{indent}[DIR]      {os.path.basename(root)}/")
        sub_indent = '    ' * (level + 1)
        for file in sorted(files):  # Sort files alphabetically in ascending order
            if '.py' in file:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                print(f"{sub_indent}[FILE]       {size:>10} B  {file}")


list_directory("..")
