"""
1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list,
которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
Выведите измененный список на экран.
Объясните, почему изменения происходят только внутри функции и как работают
изменяемые и неизменяемые параметры.
Список это объект в памяти который содержит ссылку на объект в памяти
При изменении одного элемента списка, изменяется ссылка элемента списка, а не самого списка
Для избежания этого нгеобходимо не видоизменять список, а создавать новый и работать уже с ним
Как создать
объявить и перезаполнить
глубокое копирование списка

Пример вывода:
Введите список чисел, разделенных пробелами: 1 2 3 4 5
Измененный список чисел: [2, 1, 6, 2, 10]
"""

def modify_list(lst):
    return [int(i)*2 if int(int(i) % 2) !=0 else int(int(i)/2) for i in lst.split(" ")]


"""
2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию
calculate_sum, которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию.
Выведите результат на экран.


Пример вывода:
Введите числа, разделенные пробелами: 1 2 3 4 5
Сумма чисел: 15
"""

def calculate_sum(*agr):
    return sum(agr)

if __name__ == '__main__':
    list_for_modif = "1 2 3 4 5 6 7 8 9"
    print(modify_list(list_for_modif))
    list_for_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(calculate_sum(*list_for_sum))