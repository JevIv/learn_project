from bs4 import BeautifulSoup as bs
from fake_headers import Headers
from time import sleep
from learn_project.config import PROXY
import re
import requests


def get_html(url, page_number=None):  # Забирает одну страницу

    header = Headers(headers=True)    # добавляет в request header рандомный user agent

    if not page_number:
        params = {}
    else:
        page_number = 1
        params = {'p': page_number}

    try:
        response = requests.get(url, params=params, headers=header.generate())  # сюда падает текст из ответа на get
        response.raise_for_status()
        sleep(5)
        return response.text
    except(requests.RequestException, ValueError, AttributeError):
        raise response.status_code
        return False


def last_page(text):  # Находит номер последней страницу в категории
    soup = bs(text, 'html.parser')
    pagination = soup.find_all('span', class_="pagination-item-1WyVp")  # Находит 'кнопки' в разделе pagination
    if pagination:
        digits = re.findall(r'\d{2,4}', pagination[-2]['data-marker'],)  # Вытаскивает цифры из предпоследней кнопки
        last_page = int(digits[0])  # Преобрузует цифры в int
    else:
        last_page = 1
    return last_page


def get_all_pages(url):  # Делает итерацию по страницам
    all_pages = []
    max_page = last_page(get_html(url)) + 1  # Определает, сколько циклу надо итераций
    for page_number in range(1, max_page):
        all_pages.append(get_html(url, page_number))  # Добавляет страницу (str) как элемент списка
    return all_pages
