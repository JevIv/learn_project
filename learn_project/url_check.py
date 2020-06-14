"""Модуль проверяет ссылки"""
import requests
from product_details import get_product_details

def check_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        #return r.text
        get_product_details(r.text)
    except(requests.RequestException, ValueError):
        print(f"{url} : Network Error")
        return False