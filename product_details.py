import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    r = requests.get(url)
    return r.text

def get_product_details(html):
 	if html:
 		soup = bs(html, 'html.parser')
 		product = soup.find('div', class_ = 'item-view js-item-view')
 		try:
 			name = product.find('span', class_ = 'title-info-title-text').text
 		except:
 			name = ''
 		try:
 			price = product.find('span', class_ = 'js-item-price').text
 		except:
 			price = ''
 		try:
 			date = product.find('div', class_ = 'title-info-metadata-item-redesign').text
 		except:
 			date = ''
 		try:
 			text = product.find('div', class_ = 'item-description-text').text
 		except:
 			text = ''
 		try:
 			address = product.find('span', class_ = 'item-address__string').text
 		except:
 			address = ''
 		try:
 			ad_number = product.find('div', class_ = 'item-view-search-info-redesign').find('span').text
 		except:
 			ad_number = ''
 		images_urls = []
 		try:
	 		gallery_list = product.find('ul', class_ = 'gallery-list js-gallery-list')
	 		images = gallery_list.findAll('img')
	 		for image in images:
	 			urls = image['src']
	 			images_urls.append(urls)
	 	except:
	 		main_image = product.find('div', class_ = 'item-view-gallery item-view-gallery_type-one-img')
	 		images = main_image.findAll('img')
	 		for image in images:
	 			urls = image['src']
	 			images_urls.append(urls)
	 	print(name)


if __name__ == '__main__':
	url = "https://www.avito.ru/moskva/tovary_dlya_kompyutera/videokarta_rx_470_4_gb_asus_strix_1945905515"
	get_product_details(get_html(url))