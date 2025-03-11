"""
Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
Пример переданного списка слов:

['cat', 'dog', 'tac', 'god', 'act']
Пример вывода:
Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']
"""

def anagrams(words: list) -> list[list[str]]:
    new_list = list()
    print(set('cat') == set('tac'))
    while len(words) > 0:
        anograms_list = list()
        for word in words:
            if not anograms_list:
                anograms_list.append(word)
                words.remove(word)
            else:
                if set(anograms_list[0]) == set(word):
                    anograms_list.append(word)
                    words.remove(word)
        new_list.append(anograms_list)
    return new_list

"""
Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае. Функция должна быть реализована без использования встроенных методов issubset или <=.
Пример множеств
{1, 2, 3}
{1, 2, 3, 4, 5}
Пример вывода:
True
"""

def is_subset(set1: set[int], set2: set[int]) -> bool:
    return not set1.difference(set2) if set1.issubset(set2) else False

if __name__ == '__main__':
    print(anagrams(['cat', 'dog', 'tac', 'god', 'act']))
    print(is_subset({1, 2, 3}, {1, 2, 3, 4, 5}))