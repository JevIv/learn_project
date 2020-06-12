from bs4 import BeautifulSoup as bs
import re
import requests


def get_html(url):  # Забирает одну страницу
    try:
        response = requests.get(url)  # сюда падает текст из ответа на get
        response.raise_for_status()
        return response.text
    except(requests.RequestException, ValueError):
        return False


def last_page(text):  # Находит номер последней страницу в категории 
    soup = bs(text, 'html.parser')
    pagination = soup.find_all('span', class_="pagination-item-1WyVp")  # Находит 'кнопки' в разделе pagination
    digits = re.findall(r'\d{2}', pagination[-2]['data-marker'],)  # Вытаскивает цифры из предпоследней кнопки
    last_page = int(digits[0])  # Преобрузует цифры в int
    return last_page


def get_all_pages(url):  # Делает итерацию по страницам
    all_pages = []
    max_page = last_page(get_html(url))  # Определает, сколько циклу надо итераций
    for page_number in range(1, max_page):
        all_pages.append(get_html(url, page_number))  # Добавляет страницу (str) как элемент списка 
    return all_pages
