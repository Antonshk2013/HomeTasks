from functools import reduce
from itertools import accumulate


"""Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (
comprehension) для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы. Затем
программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате программа
должна вывести новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре."""
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']


# Решение №1 в одну строку, оч все как то непонятно
def convert_list_words(list_words: list[str]) -> list[str]:
    return list(map(str.capitalize, (word for word in list_words if word.lower()[0] in vowels)))

# Решение №2 в Функциональном стиле(немного избыточно, но как есть)

def to_capitalize (word: str) -> str:
    return word.capitalize()

def is_vowels(word: str) -> bool:
    return word.lower()[0] in vowels

def main1() -> list[str]:
    list_words = input("Введите пожалуйста список слов: ").split()
    clean_list_words = [word for word in list_words if is_vowels(word)]
    clean_and_vowels_list_words = list(map(to_capitalize, clean_list_words))
    print(clean_and_vowels_list_words)



"""Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля 
functools, чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию 
itertools.accumulate для накопления произведений чисел в новом списке. В результате программа должна вывести список, 
содержащий накопленные произведения."""

def main2():
    list_numbers = [int(number) for number in input("Введите пожалуйста список чисел: ").split()]
    multi = reduce(lambda x, y: x * y, list_numbers)
    multi_list = list(accumulate(list_numbers, lambda x, y: x * y))
    print(multi_list)


if __name__ == '__main__':
    list_words = ["Она", "нет", "он", "Зато", "Изя"]
    # print(convert_list_words(list_words))
    # main()
    main2()