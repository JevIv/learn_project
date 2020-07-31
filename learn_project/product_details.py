"""Данный модуль собирает информацию со страницы товара и заводит её в словарь"""
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import locale
import re

locale.setlocale(locale.LC_ALL, "ru_RU")


def get_product_details(html):
	if not html:
		raise ValueError
	soup = bs(html, 'html.parser')
	product = soup.find('div', class_='item-view js-item-view')  # контейнер с товаром, все поиски ниже ведутся в нём
	name = product.find('span', class_='title-info-title-text').text

	try:
		price = product.find('span', class_='js-item-price').text
	except(AttributeError):
		price = product.find('span', class_='price-value-string js-price-value-string').text

	try:
		date = product.find('div', class_='title-info-metadata-item-redesign').text
		date = parse_date(date)
	except(AttributeError):
		date = datetime.now.strftime('%d %B в %H:%M')

	try:
		text = product.find('div', class_='item-description-text').text
	except(AttributeError):
		text = product.find('div', class_='item-description-html').find('p').text

	address = product.find('span', class_='item-address__string').text
	ad_number = product.find('div', class_='item-view-search-info-redesign').find('span').text
	images_url_list = []  # ниже идёт проверка на картинки,
	try:			  # сначала проверяет на список приложенных картинок,
					# если нету, то забирает главную картинку
		gallery_list = product.find('div', class_='gallery-imgs-container js-gallery-imgs-container')
		images = gallery_list.findAll('div', 'gallery-img-frame js-gallery-img-frame')

		for image in images:
			urls = image['data-url']
			images_url_list.append(urls)

	except(AttributeError):
		main_image = product.find('div', class_='item-view-gallery item-view-gallery_type-one-img')
		images = main_image.findAll('img')

		for image in images:
			urls = image['src']
			images_url_list.append(urls)

	details = {			# словарь в который собираются данные
		'name': name,
		'price': price,
		'date': date,
		'text': text,
		'address': address,
		'ad_number': ad_number,
		'images_url_list': images_url_list}
	return details


def parse_date(date: str) -> datetime:
	relative_day = re.findall(r'сегодня|вчера', date)
	if relative_day:
		if relative_day[0] == 'вчера':
			delta = timedelta(days=1)
		if relative_day[0] == 'сегодня':
			delta = timedelta(days=0)
		day = datetime.today().date() - delta
		day = str(day)
		time = re.findall(r'\d{1,2}[:-]\d{2}', date)
		time = time[0]
		right_date = f'{day} {time}'
		try:
			right_date = datetime.strptime(right_date, '%Y-%m-%d %H:%M')
		except(ValueError):
			right_date = datetime.now()
		return(right_date)

	else:
		year = datetime.today().year
		date = f'{year},{date.strip()}'
		try:
			right_date = datetime.strptime(date, '%Y,%d %B в %H:%M')
		except(ValueError):
			right_date = datetime.now()
		return(right_date)
