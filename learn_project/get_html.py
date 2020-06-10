from bs4 import BeautifulSoup as bs
import re
import requests

# Забирает одну страницу
def get_html(url):
    try:
        response = requests.get(url) # сюда падает текст из ответа на get
        response.raise_for_status()
        return response.text
    except(requests.RequestException, ValueError):
        return False

# Находит номер последней страницу в категории 
def last_page(text):
    soup = bs(text, 'html.parser')
    pagination = soup.find_all('span', class_ = "pagination-item-1WyVp") # Находит 'кнопки' в разделе pagination
    digits = re.findall(r'\d{2}', pagination[-2]['data-marker'],) # Вытаскивает цифры из предпоследней кнопки
    last_page = int(digits[0]) # Преобрузует цифры в int
    return last_page

# Делает итерацию по страницам
def get_all_pages(url):
    all_pages = []
    max_page = last_page(get_html(url)) # Определает, сколько циклу надо итераций
    for page_number in range(1, max_page):
        all_pages.append(get_html(url, page_number)) # Добавляет страницу (str) как элемент списка 
    return all_pages

