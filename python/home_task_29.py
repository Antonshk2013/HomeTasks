"""1. Создайте класс Rectangle для представления прямоугольника. Класс должен иметь атрибуты width (ширина) и height
(высота), а также метод calculate_area(), который вычисляет площадь прямоугольника. Затем создайте экземпляр класса
Rectangle с заданными значениями ширины и высоты и выведите его площадь."""

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

"""2. Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст), 
а также метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student с 
заданным именем и возрастом и вызовите метод display_info()."""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

if __name__ == '__main__':
    rectangle = Rectangle(5, 5)

    print(rectangle.calculate_area())
    student = Student(name='Vasia', age=53)
    print(student.display_info())
