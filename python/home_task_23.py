"""1. Напишите программу, которая генерирует и выводит квадраты чисел от 1 до N с использованием генераторного
выражения. Реализуйте функцию generate_squares, которая принимает число N в качестве аргумента и использует
генераторное выражение для генерации квадратов чисел. Затем выведите квадраты чисел на экран.
Пример работы программы:
1
4
9
16
25
"""

def generate_squares(n: int):
    list_squares = (x**2 for x in range(1, n+1))
    for i in list_squares:
        print(i)
"""
2. Напишите генератор, который будет генерировать бесконечную последовательность Фибоначчи. Каждый раз, когда 
генератор вызывается, он должен возвращать следующее число последовательности. Напишите программу, которая будет 
использовать этот генератор для вывода первых N чисел Фибоначчи.
Пример вывода:
Введите количество чисел Фибоначчи: 10
Первые 10 чисел Фибоначчи:

0
1
1
2
3
5
8
13
21
34
"""

def gen_fibonacci(n:int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    generate_squares(5)
    gen = gen_fibonacci(10)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))