from learn_project.get_html import get_all_pages, get_html
from learn_project.url_scraping import get_products_urls
from learn_project.config import TARGET_URL
from learn_project.product_details import get_product_details


def parse():
    lst_of_html_items = get_all_pages(TARGET_URL)

    product_urls = [get_products_urls(html_item) for html_item in lst_of_html_items]

    products_htmls = [get_html(url) for url in product_urls]

    lst_of_product_details = []
    for products_html in products_htmls:
        lst_of_product_details.append(get_product_details(products_html))

    return lst_of_product_details


if __name__ == "__main__":
    parse()
