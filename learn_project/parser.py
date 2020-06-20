from learn_project.get_html import get_all_pages, get_html
from learn_project.url_scraping import get_products_urls, unfold_list
from learn_project.config import TARGET_URL
from learn_project.product_details import get_product_details
from learn_project.save_to_db import save_products


def parse():
    # принимает url категории товаров, возвращает список с html страницами этой категории
    lst_of_html_items = get_all_pages(TARGET_URL)
    print(f'total html pages {len(lst_of_html_items)}')

    # принимает список с str html страницами, возвращает список со списками url
    list_of_url_lists = [get_products_urls(html_item) for html_item in lst_of_html_items]
    print(f'total url lists {len(list_of_url_lists)}')
    print(f'url in first lists {len(list_of_url_lists[0])}')

    # принимает список со списками url, возвращает плоский список url
    flat_url_list = unfold_list(list_of_url_lists)
    print(f'total urls {len(flat_url_list)}')

    # принимает список url товаров, возвращает список str html товаров
    products_htmls = [get_html(url) for url in flat_url_list]
    print(f'total product htmls {len(products_htmls)}')

    # принимает список html страниц товаров, пишет результаты парсинга в бд
    details_list = []
    for products_html in products_htmls:
        details_list.append(get_product_details(products_html))
    save_products(details_list)


if __name__ == '__main__':
    parse()
