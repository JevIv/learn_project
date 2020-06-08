import requests
from bs4 import BeautifulSoup as bs

def check_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except(requests.RequestException, ValueError):
        print(f"{url} : Network Error")
        return False