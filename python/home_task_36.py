"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку Beautiful Soup
для парсинга HTML и выводит список всех ссылок на странице.
"""
import requests
from bs4 import BeautifulSoup

def get_links_from_html(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('a')
    except requests.exceptions.RequestException:
        return None

"""
Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков, а затем 
использует библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом.
"""
def get_headers_bey_level(url, header_level=1):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all(f'h{header_level}')
        return headers
    except requests.exceptions.RequestException:
        return None

if __name__ == '__main__':
    # print(get_links_from_html("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D0%BA%D0%BB%D0%B0%D0%B2_2025_%D0%B3%D0%BE%D0%B4%D0%B0"))
    print(get_headers_bey_level("https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BD%D0%BA%D0%BB%D0%B0%D0%B2_2025_%D0%B3%D0%BE%D0%B4%D0%B0", 2))