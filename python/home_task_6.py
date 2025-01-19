import random
# 1. Напишите программу, которая генерирует случайное число от 1 до 100, а затем предлагает пользователю
# угадать это число. Если пользователь угадывает число, программа выводит сообщение о победе.
# Если пользователь не угадывает число, программа сообщает, больше или меньше загаданное число и предлагает попробовать
# снова. Используйте цикл с инструкцией break, чтобы остановить выполнение цикла, когда число угадано.
#
# Пример вывода:
# Угадайте число от 1 до 100: 50
# Загаданное число меньше.
# Попробуйте снова: 75
# Загаданное число больше.
# Попробуйте снова: 63
# Поздравляю! Вы угадали число 63!

message = {
        0: "Enter a number between 1 and 100: ",
        1: "Попробуйте снова: ",
        2: "Загаданное число меньше.",
        3: "Загаданное число больше.",
        4: "Введите целое положительное число: ",
        5: "Число {input_number} не является простым",
        6: "Число {input_number} является простым"
    }

def get_number(n: int):
    input_number = abs(int(input(message.get(n))))
    return input_number

def number_win():
    number = random.randint(1, 100)
    input_number = get_number(0)
    while input_number != number:
        if input_number > number:
            print(message.get(2))
            input_number = get_number(1)
        elif input_number < number:
            print(message.get(3))
            input_number = get_number(1)
    else:
        print(f"Поздравляю! Вы угадали число {number}!")

#
# 2. Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи.
# Числа Фибоначчи - это последовательность чисел, где каждое следующее число является суммой двух предыдущих чисел
# (начиная с 0 и 1). Используйте цикл while для решения задачи. Выведите числа через запятую с помощью команды print.
#
# Пример вывода:
# Введите число N: 7
# Первые 7 чисел Фибоначчи: 0, 1, 1, 2, 3, 5, 8

def fibonacci_sequence(n:int):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a)
        i += 1
        a, b = b, a + b

# 3. Напишите программу, которая запрашивает у пользователя целое положительное число и проверяет, является ли
# оно простым. Простое число - это число, которое делится только на 1 и на само себя без остатка. Используйте цикл
# while и проверку деления числа на все числа от 2 до N-1 для решения задачи.
# Выведите соответствующее сообщение на экран с помощью команды print.

# Пример вывода:
# Введите целое положительное число: 17
# Число 17 является простым.

def is_prime():
    count_dec = 0
    a = 3
    input_number = abs(int(input(message.get(4))))
    if input_number <= 1:
        print(message.get(5).format(input_number=input_number))
    elif input_number == 2:
        print(message.get(6).format(input_number=input_number))
    else:
        while a <= input_number:
            print(f"Числитель {a}")
            if input_number % a == 0:
                count_dec += 1
                if count_dec > 1:
                    print(message.get(5).format(input_number=input_number))
                    break
            a += 1
        else:
            print(message.get(6).format(input_number=input_number))




if __name__ == '__main__':
    # number_win()
    # fibonacci_sequence(7)
    is_prime()


