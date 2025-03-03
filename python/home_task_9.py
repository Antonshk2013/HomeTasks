"""

1. Напишите программу, которая запрашивает у пользователя строку и определяет, является ли она панграммой.
Панграмма - это фраза, содержащая все буквы алфавита. Программа должна игнорировать регистр букв и пробелы при
проверке панграммы. Выведите соответствующее сообщение на экран с помощью команды print. Решить задачу для латиницы.
Пример вывода:
Введите строку: The quick brown fox jumps over the lazy dog
Строка является панграммой.
"""

def is_panogram(sentence):
    alfabet='abcdefghijklmnopqrstuvwxyz'
    for i in sentence.replace(" ", "").lower():
        alfabet = alfabet.replace(i, '')
    return not alfabet


"""
2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран количество гласных и согласных букв 
в ней. Используйте функцию len() для подсчета количества букв. 
Выведите результат на экран с помощью команды print. Решить задачу для латиницы.
Пример вывода:
Введите строку: Hello World
Количество гласных букв: 3
Количество согласных букв: 7
"""


def count_vowels_and_consonants(sentence):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    print(f'Количество гласных букв: {len([i for i in sentence.lower() if i in vowels])}')
    print(f'Количество согласных букв: {len([i for i in sentence.lower() if i in consonants])}')

if __name__ == '__main__':
    sentence = "The quick brown fox jumps over the lazy dog"
    print(is_panogram(sentence))
    sentence2 = "Hello World"
    count_vowels_and_consonants(sentence2)
