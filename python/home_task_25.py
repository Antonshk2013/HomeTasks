from decimal import Decimal
from typing import List, Union
"""
1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
 Аннотируйте типы аргументов и возвращаемого значения функции.
Пример вызова функции и ожидаемого вывода:
words = ["apple", "banana", "cherry", "dragonfruit"]
result = find_longest_word(words)
print(result)  # Ожидаемый вывод: "dragonfruit"
"""

def find_longest_word(words:list[str]) -> str:
    return max(words, key=len)

"""
2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для 
аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt", в котором каждая строка будет 
содержать информацию о продукте в формате "название, цена, количество". Например:

Apple, 1.50, 10
Banana, 0.75, 15

В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую 
стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на 
составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите 
результат. Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода. Потому что в реальных 
задачах обычно этого нет. Нужно самому придумывать даже самые простые тестовые данные, содержимое тестовых файлов и 
т.п. В случае с классами (будут чуть позже) особенно."""



def calculate_total_price(orders: List[str])->Union[float|int]:
    total_price = 0
    for product in orders:
        name, count, price = product.split(", ")
        total_price += float(Decimal(count)) * float(Decimal(price))
    return total_price


if __name__ == '__main__':
    print(find_longest_word(["apple", "banana", "cherry", "dragonfruit"]))
    with open('additional_files/products.txt', 'r', encoding='utf8') as f:
        product_list = [line for line in f]
        print(calculate_total_price(product_list))
