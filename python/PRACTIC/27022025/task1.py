


"""
Необходимо написать функцию raising_to_power, которая принимает список чисел nums и степень power.
Функция возвращает список этих чисел, возведённых в указанную степень.

Важно: и список nums, и значение переменной power, после выполнения функции должны остаться неизменными.
"""
def raising_to_power(nums, value):
    return [i**value for i in nums]


"""Написать функцию sum_of_even, которая принимает произвольное число параметров (целые числа) и 
возвращает сумму всех чётных чисел.
# 14
"""


def even_power_2(*args: list[int]) -> int:
    return sum([i for i in args if i % 2 == 0])


if __name__ == '__main__':
    # nums = [1, 2, 3]
    # value = 2
    # print(raising_to_power(nums, value)) # [1, 4, 9]
    # print((lambda nums1, value1: [i**value1 for i in nums1])(nums, value)) # [1, 4, 9]
    # print(nums) # [1, 2, 3]
    # print(value) # 2

    print(even_power_2(1, 4, 5, 10))