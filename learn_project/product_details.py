"""Данный модуль собирает информацию со страницы товара и заводит её в словарь"""
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import locale
import re


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
	date = product.find('div', class_='title-info-metadata-item-redesign').text
	date = parse_date(date)
	try:
		text = product.find('div', class_='item-description-text').text
	except(AttributeError):
		text = product.find('div', class_='item-description-html').find('p').text
	address = product.find('span', class_='item-address__string').text
	ad_number = product.find('div', class_='item-view-search-info-redesign').find('span').text
	images_url_list = []  # ниже идёт проверка на картинки,
	try:			  # сначала проверяет на список приложенных картинок,
					# если нету, то забирает главную картинку
		gallery_list = product.find('ul', class_='gallery-list js-gallery-list')
		images = gallery_list.findAll('img')

		for image in images:
			urls = image['src']
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
	locale.setlocale(locale.LC_ALL, "ru_RU")
	relative_day = re.findall(r'Сегодня|Вчера', date)

	if relative_day:
		date_starts_with = date[0:5]
		if date_starts_with == 'Вчера':
			delta = timedelta(days=1)
		if date_starts_with == 'Сегод':
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
		date = f'{year},{date}'
		try:
			right_date = datetime.strptime(date, '%Y,%d %B в %H:%M')
		except(ValueError):
			right_date = datetime.now()
		return(right_date)
