"""Данный модуль собирает информацию со страницы товара и заводит её в словарь"""
from bs4 import BeautifulSoup as bs
from time import sleep
from learn_project.get_html import get_html


def get_product_details(html):
	if not html:
		raise ValueError
	soup = bs(html, 'html.parser')
	product = soup.find('div', class_='item-view js-item-view')	 # контейнер с товаром, все поиски ниже ведутся в нём
	name = product.find('span', class_='title-info-title-text').text
	price = product.find('span', class_='js-item-price').text
	date = product.find('div', class_='title-info-metadata-item-redesign').text
	try:
		text = product.find('div', class_='item-description-text').text
	except(AttributeError):
		text = product.find('div', class_='item-description-html').find('p').text
	address = product.find('span', class_='item-address__string').text
	ad_number = product.find('div', class_='item-view-search-info-redesign').find('span').text
	images_urls = []  # ниже идёт проверка на картинки,
	try:			  # сначала проверяет на список приложенных картинок,
					  # если нету, то забирает главную картинку
		gallery_list = product.find('ul', class_='gallery-list js-gallery-list')
		images = gallery_list.findAll('img')

		for image in images:
			urls = image['src']
			images_urls.append(urls)

	except(AttributeError):
		main_image = product.find('div', class_='item-view-gallery item-view-gallery_type-one-img')
		images = main_image.findAll('img')

		for image in images:
			urls = image['src']
			images_urls.append(urls)

	details = {			# словарь в который собираются данные
		'name': name,
		'price': price,
		'date': date,
		'text': text,
		'address': address,
		'ad_number': ad_number,
		'images_urls': images_urls}
	sleep(5)
	return details
