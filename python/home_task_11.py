"""
1. Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания,
а затем выводит их в следующем формате:
"Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
Вместо {0}, {1} и {2} подставьте соответствующие значения.
Используйте метод format() для форматирования строки.
Потом попробуйте использовать f-строку.
Выведите результат на экран с помощью команды print.
Пример вывода:
Введите ваше имя: Alice
Введите ваш возраст: 25
Введите ваше место проживания: London
Привет, меня зовут Alice. Мне 25 лет. Я живу в London.
"""

def format_string1(name: str, age: int, location: str) -> str:
    # return f"Привет, меня зовут {name}. Мне {age}. Я живу в {location}"
    return "Привет, меня зовут {0}. Мне {1}. Я живу в {2}".format(name, age, location)

"""
2. Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму 
и произведение в следующем формате:
"Сумма: {sum:.2f}, Произведение: {product:.2f}"
Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, 
округленные до двух десятичных знаков. 
Используйте f-строки с использованием форматных спецификаторов для форматирования чисел. 
Выведите результат на экран с помощью команды print.

Пример вывода:
Введите первое число: 3.14159
Введите второе число: 2.71828
Сумма: 5.86, Произведение: 8.54
"""


def format_string2(a: float, b: float) -> str:
    return f"Сумма: {a+b:.2f}, Произведение: {a*b:.2f}"


if __name__ == '__main__':
    print(format_string1(name="Alice", age=25, location="London"))
    print(format_string2(a=3.14159, b=2.71828))