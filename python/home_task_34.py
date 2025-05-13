import re
"""
Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста
и возвращает их в виде списка.
"""
def extract_emails(text):
    pattern = r'[a-z]+@[a-z]+\.[a-z]+'
    return re.findall(pattern, text)


"""
Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте, 
окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
"""

def highlight_keywords(text, keywords):
    text = text.lower()
    for keyword in keywords:
        text = re.sub(keyword, fr"*{keyword}*", text, flags=re.IGNORECASE)
    return text

if __name__ == '__main__':
    # #Task 1
    # text = "Contact us at info@example.com or support@example.com for assistance."
    # emails = extract_emails(text)
    # print(emails)  # Вывод: ['info@example.com', 'support@example.com']

    #Task 2
    text = "This is a sample text. We need to highlight Python and programming."
    keywords = ["python", "programming"]
    highlighted_text = highlight_keywords(text, keywords)
    print(highlighted_text)
    # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."