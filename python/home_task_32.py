from datetime import datetime
"""
1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
- Увеличение значения счетчика на заданное число (оператор +=)
- Уменьшение значения счетчика на заданное число (оператор -=)
- Преобразование счетчика в строку (метод __str__)
- Получение текущего значения счетчика (метод __int__)
"""


class Counter:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return f"Counter Value: {self.value}"

    def __int__(self):
        return self.value

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self


"""
2. Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
- Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
- Преобразование письма в строку (метод __str__)
- Получение длины текста письма (метод __len__)
- Получение хеш-значения письма (метод __hash__)
- Проверка наличия текста в письме (метод __bool__)
"""
class Email:
    def __init__(self, sender, recipient, subject, body, cr_date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.cr_date = cr_date

    def __str__(self):
        return f"""
        From: {self.sender}

        To: {self.recipient}

        Subject: {self.subject}
        
        {self.body}
        
        """


    def __len__(self):
        return len(self.body)

    def __hash__(self):
        return hash(self.__str__())

    def __bool__(self):
        return bool(self.body)

    def __lt__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') < datetime.strptime(other.cr_date, '%Y-%m-%d')

    def __gt__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') > datetime.strptime(other.cr_date, '%Y-%m-%d')

    def __le__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') <= datetime.strptime(other.cr_date, '%Y-%m-%d')

    def __ge__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') >= datetime.strptime(other.cr_date, '%Y-%m-%d')

    def __eq__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') == datetime.strptime(other.cr_date, '%Y-%m-%d')

    def __ne__(self, other):
        return datetime.strptime(self.cr_date, '%Y-%m-%d') != datetime.strptime(other.cr_date, '%Y-%m-%d')

if __name__ == '__main__':
    # counter = Counter(5)
    # counter += 3
    # print(counter)  # Вывод: 8
    # counter -= 2
    # print(int(counter))  # Вывод: 6
    email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.",
                   "2022-05-10")
    email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")
    email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

    print(email1)  # Вывод:
    print(len(email2))  # Вывод: 24
    print(hash(email3))  # Вывод: -920444056
    print(bool(email1))  # Вывод: True
    print(email2 > email3)  # Вывод: True
