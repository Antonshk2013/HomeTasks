"""
1. Напишите программу, которая запрашивает у пользователя число N и выводит на экран таблицу умножения от 1 до N.
Используйте вложенный цикл for для создания таблицы умножения.
Выведите результат на экран с помощью команды print.

Пример вывода:
Введите число N: 5
Таблица умножения:
"""

def count_table(num:int):

    for a in range(1,num+1):
        line = ''
        for b in range(1, num+1):
            line += f' {a*b}'
        print(line)

"""
2. Напишите программу, которая принимает два списка одинаковой длины и создает новый список, содержащий пары элементов из исходных списков. Используйте функцию zip() для создания пар элементов. Выведите результат на экран с помощью команды print.
Пример вывода:
Введите элементы первого списка, разделенные пробелом: 1 2 3 4 5
Введите элементы второго списка, разделенные пробелом: A B C D E
Список пар элементов: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]
"""

def convert_list(list1:list, list2:list)->list:
    if len(list1) != len(list2):
        return "Exeption lists have different length"
    return [(list1[i], list2[i]) for i in range(len(list1))]

if __name__ == '__main__':
    count_table(5)
    print(convert_list([1, 2, 3, 4, 5], ['A', 'B', 'C', 'D', 'E'])) #[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')]