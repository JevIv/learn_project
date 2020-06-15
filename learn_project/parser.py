from learn_project.get_html import get_all_pages, get_html
from learn_project.url_scraping import get_products_urls, unfold_list
from learn_project.config import TARGET_URL
from learn_project.product_details import get_product_details


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

    # принимает список html страниц товаров, возвращает список словарей с инфой о товарах
    lst_of_product_details = []
    for products_html in products_htmls:
        lst_of_product_details.append(get_product_details(products_html))
    print(f'total detail dicts {len(lst_of_product_details)}')
    return lst_of_product_details


if __name__ == "__main__":
    parse()
