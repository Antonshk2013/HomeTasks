"""1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму. Генератор должен использовать
инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме. Если
генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму. Напишите программу,
которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.


Пример вывода:


Введите числа для суммирования (0 для окончания):

Введите число: 3

Текущая сумма: 3

Введите число: 5

Текущая сумма: 8

Введите число: 2

Текущая сумма: 10

Введите число: 0

Текущая сумма: 10
"""
from typing import Any


def my_generator():
    num_sum = 0
    while True:
        received_value = yield num_sum
        received_value = 0 if received_value == None else received_value
        num_sum = num_sum + received_value

"2. Напишите генератор, который будет генерировать арифметическую прогрессию"
def my_generator2():
    new_list_nums = []
    while True:
        list_nums: Any = yield new_list_nums
        list_nums = [0, 0] if list_nums == None else list_nums
        a, b = list_nums
        new_list_nums = [b, (b+(b-a))]


if __name__ == '__main__':
    # gen = my_generator()
    # next(gen)
    # while True:
    #     number = int(input("Введите число: "))
    #     result = gen.send(number)
    #     if number==0:
    #         gen.close()
    #         print(f"Текущая сумма: {str(result)}")
    #         break
    #     print(f"Текущая сумма: {str(result)}")
    #
    #
    #     def word_multiply(word1: str, multiplay: int) -> str:
    #         return word1*2

    gen = my_generator2()
    gen.send(None)
    print(gen.send([1, 2]))
    print(gen.send([5, 12]))
    print(gen.send([7, 100]))
    print(gen.send([-8, -16]))



