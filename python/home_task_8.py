# 1. Напишите программу, которая запрашивает у пользователя целое число и определяет,
# является ли оно палиндромом.
# Число является палиндромом, если оно читается одинаково слева направо и справа налево.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Используйте математические операции. Работу со строками использовать нельзя.
# <
# Пример вывода:
# Введите целое число: 12321
# Число является палиндромом.

def is_polindrome(number: int) -> bool:
    print("Start")
    number1 = number
    number2 = 0
    while number:
        number2 *= 10
        number2 += number % 10
        number = number // 10
    return True if number1 == number2 else False

# 2. Напишите программу, которая запрашивает у пользователя целое число и проверяет,
# является ли оно числом Армстронга.
# Число Армстронга - это число, которое равно сумме своих цифр,
# возведенных в степень,
# равную количеству цифр в числе. Выведите соответствующее сообщение на экран с помощью команды print.
#
#
# Пример вывода:
# Введите целое число: 153
# Число является числом Армстронга.


def is_armstromg_number(number: int) -> bool:
    digit_len = len(str(abs(number)))
    return number == sum([int(i) ** digit_len for i in str(abs(number))])


if __name__ == '__main__':
    print(is_polindrome(12321))
    a = 153
    print(is_armstromg_number(a))
    print(abs(a))
    print(1 ** 3 + 5 ** 3 + 3 ** 3)


