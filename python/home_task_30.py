'''1. Создайте класс Rectangle для представления прямоугольника. Класс должен иметь атрибуты width (ширина) и height
(высота) со значениями по умолчанию, а также методы calculate_area() для вычисления площади прямоугольника и
calculate_perimeter() для вычисления периметра прямоугольника. Переопределить методы __str__, __repr__. Затем
создайте экземпляр класса Rectangle и выведите информацию о нем, его площадь и периметр.'''

class Rectangle:

    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'width = {self.width} height = {self.height}'

    def __repr__(self):
        return f"{self.__class__.__name__}({' '.join([f'{k!r}={v!r}'for k,v in self.__dict__.items()])})"
'''2. Создайте класс BankAccount для представления банковского счета. Класс должен иметь атрибуты account_number (
номер счета) и balance (баланс), а также методы deposit() для внесения денег на счет и withdraw() для снятия денег со 
счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег. Выведите 
оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля. В этом 
случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int):
        self.balance = self.balance + amount
        return f"Текуший баланс составляет {self.balance}"

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise Exception("Недостаточно средств на счете")
        self.balance = self.balance - amount
        return f"Текуший баланс составляет {self.balance}"



if __name__ == '__main__':
    rect = Rectangle(2,5)
    print(rect.__str__())
    print(rect.__repr__())


    acount = BankAccount('26000000000001')
    print(acount.deposit(100))
    print(acount.withdraw(20))
    print(acount.withdraw(20))
    print(acount.withdraw(20))
    print(acount.withdraw(20))
    print(acount.withdraw(20))
    print(acount.withdraw(20))
