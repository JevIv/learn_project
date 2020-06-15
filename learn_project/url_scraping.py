"""Модуль парсит страницы товаров"""
import requests
from bs4 import BeautifulSoup as bs
from learn_project.get_html import get_html


def get_products_urls(html):
	if not html:
		raise ValueError
	soup = bs(html, 'html.parser')
	all_products = soup.find_all('div', class_ = 'item__line') #поиск всех тэгов div с классом item__line - вернёт список
	prod_url = [] 	#список в который записываем ссылки товаров
	for product in all_products:
		url = product.find('h3', class_ = 'snippet-title').find('a')['href']
		url = "https://www.avito.ru" + url
		prod_url.append(url)
	return prod_url

def unfold_list(folded_list):
	unfolded_list = [url for url_list in folded_list for url in url_list]
	return unfolded_list



#if __name__ == '__main__':
#	url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw"
#	print(get_products_urls(get_html(url)))

