
"""
1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает объект
ответа. Затем выведите следующую информацию об ответе:
- Код состояния (status code)
- Текст ответа (response text)
- Заголовки ответа (response headers)
"""
import requests
import re
from requests.models import Response
from collections import Counter

def get_response(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.ConnectionError as e:
        fake_response = Response()
        fake_response.status_code = 505
        fake_response._content = str(e).encode('utf-8')
        return fake_response



"""
2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее 
часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы с 
помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать 
количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
"""

def find_common_words(url_list):
    counter = Counter()

    for url in url_list:
        try:
            response = get_response(url)
            if response.status_code == 200:
                text = re.sub(r'<[^>]+>', ' ', response.text)
                words = re.findall(r'\b\w+\b', text)
                counter.update(words)

        except requests.exceptions.ConnectionError as e:
            print(e)
    return counter.most_common()


if __name__ == '__main__':
    url = "https://api.example.com"
    response = get_response(url)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    print("Response Headers:", response.headers)
    urls = ["https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D0%BA%D0%BB%D0%B0%D0%B2_2025_%D0%B3%D0%BE%D0%B4%D0%B0"]
    print(find_common_words(urls))
