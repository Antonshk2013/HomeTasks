"""Создайте класс Char, который будет представлять
заглавную латинскую букву от A до Z

    Атрибуты:
        char: заглавная буква от A до Z
        code: код символа char в десятичной кодировке

При создании класса в качестве аргумента возможно строка из нескольких символов
В этом случае остаётся только первый символ, который необходимо перевести
в верхний регистр.
Если он окажется не буковой от A до Z - выбрасывается исключение:
    ValueError(f"Invalid character: {char}")

При выводе на печать объекта - выводится символ.
Допустимо сложение:
  - сложение двух объектов Char
  - или Char + целое число.
(см примеры ниже)
Реализовать вычисление суммы кода символа с целым числом
в виде отдельного защищённого (protected) метода.
"""
from typing import Union


class Char:
    def __init__(self, char: str):
        if char.isalpha():
            self.char = char
            self.code = ord(char)
        else:
            raise ValueError(f"Invalid character: {char}")

    def __add__(self, other: Union['Char', int]) -> 'Char':
        if ...:
            pass
        else:
            raise ValueError("Operand must be either Char or int")

        new_char_code = self._add_char_and_number(add_value)
        return Char(chr(new_char_code))

    def _add_char_and_number(self, number: int) -> int:
        pass

        return new_char_code

    def __repr__(self) -> str:
        return f"Char('{self.char}')"


c1 = Char('A')
print(c1 + c1)  # B

c2 = Char('B')
print(c1 + c2)  # C

c3 = Char('z')
print(c3)  # Z
print(c3 + 1)  # A

c4 = Char('Y')
print(c4 + 3)  # B
print(c4 + -3)  # B
print(c4 + 1000)  # K

c5 = Char('abba')  # A
try:
    c6 = Char('1')  # Должен выбросить ValueError
except ValueError as e:
    print(e)  # Invalid character: 1