"""
Написать программу, вычисляющую факториал числа.
Решить задачу с помощью рекурсии.
"""

def factorial(n, accumulation=1):
    if n == 0:
        return accumulation
    return n * factorial(n - 1, accumulation)


"""
Напишите программу, которая использует рекурсию для вычисления суммы цифр числа. Создайте функцию sum_digits, 
которая принимает один аргумент - число, для которого нужно вычислить сумму цифр. 
Используйте условие выхода из рекурсии, когда число состоит из одной цифры. Выведите результат на экран.
"""

def sum_digits(n, accumulator=0):
    if n < 10:
        return accumulator + n
    return sum_digits(n // 10, accumulator + n % 10)

if __name__ == '__main__':
    print(factorial(5))
    print(sum_digits(15))


