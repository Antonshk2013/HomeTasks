"""Пишем программу, которая обходит директорию и выводит информацию в формате,
максимально похожем на ls в linux/macos (dir в windows).
Делаем то же самое для директории и всех вложенных директорий.


[DIR]      ./
[FILE]          1042  practice_work_01_3_scandir.py
[FILE]          1120  practice_work_01_2_listdir.py
[FILE]          1150  practice_work_02.py
[FILE]           825  practice_work_01.py
[DIR]      homework/
    [FILE]             1  homework_02.py
    [FILE]             0  homework_01.py
[DIR]      total_recall/
    [FILE]             0  task_02.py
    [FILE]             0  task_01.py
    [FILE]             0  task_03.py
[DIR]      theory/
    [FILE]           633  theory_08_os_path.py
    [FILE]           169  theory_10_pathlab.py

"""

import os
import argparse

def list_directory(path):
    for root, dirs, files in os.walk(path):
        dirs.sort()  # Sort directories alphabetically in ascending order
        level = root.replace(path, '').count(os.sep) # counts the number of directory separators, thus giving depth level)
        indent = '    ' * level
        print(f"{indent}[DIR]      {os.path.basename(root)}/")
        sub_indent = '    ' * (level + 1)
        for file in sorted(files):  # Sort files alphabetically in ascending order
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{sub_indent}[FILE]       {size:>10} B  {file}")


parser = argparse.ArgumentParser(description="List directory contents.")
parser.add_argument("path", nargs="?", default="./",
                    help="Path to the directory to list.\nExample usage:\npython w1.py ./"
)
args = parser.parse_args()




list_directory("..")