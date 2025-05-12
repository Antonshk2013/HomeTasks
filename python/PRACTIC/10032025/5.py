# from pprint import pprint
# from collections import Counter
#
# def words_dict_sort(words: str) -> dict:
#     new_collection = Counter()
#     words_list = words.lower().replace('.', '').replace(',', '').replace('\n', '').split(' ')
#     print(words_list)
#     for word in words_list:
#         if word:
#             new_collection + Counter(word)
#
#     # return sorted(new_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
#     return sorted())
#
# if __name__ == '__main__':
#
#     text = """
#     В качестве текста использовать текст этой задачи.
#
#     Необходимо посчитать сколько раз встретилось каждое слово и вывести в топ слов,
#     упорядоченный сначала по убыванию встречаемости,
#     а при равенстве частот в соответствии с упорядочиванием в лексикографическом порядке.
#
#     Слова должны быть переведены в нижний регистр и из них должны быть удалены все небуквенные символы.
#
#     Решить задачу с помощью использования изученных классов.
#     """
#
#
#     pprint(words_dict_sort(text))