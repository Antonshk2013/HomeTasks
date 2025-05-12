"""Даны четыре функции (см репозиторий).
Необходимо написать декоратор @timer_execution,
который позволит замерить время их работы.
"""
from functools import wraps
import time


def tmp(*args):
    """Функция-пустышка, используем для анпакинга итераторов,
    для "exhausting the iterator" ("израсходывания итераторов")
    """
    pass


def timer_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return result
    return wrapper




@timer_execution
def create_with_map(num):
    for _ in range(num):
        x = map(lambda n: 'a' * n, range(num))
        tmp(*x)


@timer_execution
def create_with_list_compr(num):
    for _ in range(num):
        x = ['a' * n for n in range(num)]
        tmp(*x)


@timer_execution
def create_with_generator_expression(num):
    for _ in range(num):
        x = ('a' * n for n in range(num))
        tmp(*x)


@timer_execution
def create_with_loop(num):
    for _ in range(num):
        x = []
        for n in range(num):
            x.append('a' * n)
        tmp(*x)


n_max = 3000
create_with_map(n_max)
create_with_list_compr(n_max)
create_with_generator_expression(n_max)
create_with_loop(n_max)

# Время работы функции create_with_map:  0.0000
# Время работы функции create_with_lst_compr:  0.0000
# Время работы функции create_with_generator_expression:  0.00000
# Время работы функции create_with_loop:  0.00000