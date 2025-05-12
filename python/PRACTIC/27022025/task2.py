# Отсортируйте список под двум критериям:
# - по длине слова;
# - по длине слова и количеству гласных слове ('aeiouyAEIOUY');
# - по алфавиту.
#
# words = ["apple", "orange", "banana", "grape", "peach", "melon", "berry", "plum", "kiwi"]
# Сортировка по длине слова:
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']
# Сортировка по длине слова и количеству гласных слове ('aeiouyAEIOUY'):
# ['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana']
# Сортировка по длине слова и алфавиту:
# ['kiwi', 'plum', 'apple', 'berry', 'grape', 'melon', 'peach', 'banana', 'orange']

def sort_lang():
    pass

if __name__ == '__main__':
    words = ["apple", "orange", "banana", "grape", "peach", "melon", "berry", "plum", "kiwi"]
    print(['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana'])
    print(sorted(words, key=lambda word: len(word)))
    print(['plum', 'kiwi', 'apple', 'grape', 'peach', 'melon', 'berry', 'orange', 'banana'])
    print(sorted(words, key=lambda word: (len(word), len([i for i in word if i in 'aeiouyAEIOUY']))))
    print(['kiwi', 'plum', 'apple', 'berry', 'grape', 'melon', 'peach', 'banana', 'orange'])
    print(sorted(words, key=lambda word: (len(word), word)))
    print()