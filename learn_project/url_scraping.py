"""Модуль парсит страницы товаров"""
import requests
from bs4 import BeautifulSoup as bs
from url_check import check_url

def get_html(urls):
	for url in urls:
	    r = requests.get(url)
	   #return r.text
	    get_products(r.text)

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
	#return prod_url
	for url in prod_url:
		check_url(url)

#if __name__ == '__main__':
#	url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw"
#	print(get_products_urls(get_html(url)))

