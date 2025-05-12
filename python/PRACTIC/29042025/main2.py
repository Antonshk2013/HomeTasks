"""Реализуйте класс библиотеки Library,
с атрибутом
    - shelf: список, представляющий полку библиотеки
и методом
    - add_book: добавляет новую книгу на полку библиотеки,
                используя метод Book.create_book()..

Также необходимо создать (переопределить) некоторые dunder методы (см.примеры вывода)
"""


from main import Book



class Library:
    def __init__(self):
        self.shelf = []

    def __str__(self):
        print(f"The total number of books in the library is {len(self.shelf)}:")
        [print(f"- {book}") for book in self.shelf]
        return "End"

    def __getitem__(self, item):
        return self.shelf[item]

    def add_book(self, title, author):
        book=Book(title=title, author=author)
        self.shelf.append(book)



library = Library()

library.add_book("War and Peace", "Leo Tolstoy")
library.add_book("Pride and Prejudice", "Jane Austen")
library.add_book("Ten Little Niggers", "Agatha Christie")
library.add_book("Gone with the Wind", "Margaret Mitchell")


print(library[:2])
# ['Book War and Peace by Leo Tolstoy', 'Book Pride and Prejudice by Jane Austen']

print(library[0])
# Book War and Peace by Leo Tolstoy

print(library)
# The total number of books in the library is 3:
#  - Book "War and Peace" by Leo Tolstoy
#  - Book "Pride and Prejudice" by Jane Austen
#  - Book "Ten Little Niggers" by Agatha Christie