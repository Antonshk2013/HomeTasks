"""Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов только четных чисел из списка,
используя функциональные подходы (например, map, filter и reduce).

Пример вывода:
Введите числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
Результат: 72
"""
from functools import reduce


def sum_squares_evens_var_1(*agrs: list[int]) -> int:
    return sum(agr**2 for agr in agrs if agr % 2 == 0)


def sum_squares_evens_var_2(*agrs: list[int]) -> int:
    return sum(i**2 for i in filter(lambda x: x % 2 == 0, agrs))


def sum_squares_evens_var_3(*agrs: list[int]) -> int:
    filter_obj = filter(lambda x: x % 2 == 0, agrs)
    reduce_obj = reduce(lambda acc, x: acc + x**2, filter_obj, 0)
    return reduce_obj

"""Напишите функцию, которая принимает на вход список функций и значение, а затем применяет композицию этих функций к 
значению, возвращая конечный результат.
Пример использования:
add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3
functions = [add_one, double, subtract_three]
compose_functions(functions, 5) должно вывести 9
"""


def compose_functions(functions: list[callable], x: int) -> list[int]:
    for func in functions:
        x = func(x)
    return x


def compose_functions_2(functions: list[callable], x: int) -> list[int]:
    return reduce(lambda acc, f: f(acc), functions, x)



if __name__ == '__main__':
    list_numbers = [4, 6, 3, 4, 2, 3, 9, 0, 7]
    # print(sum_squares_evens_var_1(*list_numbers))
    # print(sum_squares_evens_var_2(*list_numbers))
    # print(sum_squares_evens_var_3(*list_numbers))
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    subtract_three = lambda x: x - 3
    functions = [add_one, double, subtract_three]
    print(compose_functions(functions, 5))
    print(compose_functions_2(functions, 5))
