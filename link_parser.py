import requests
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://tula-online.org/items/browse?f=books&page='


def fetch_links(cookies):
    file = open("book_links.txt", "a")

    for page in range(240):
        r = requests.get(
            f'{BASE_URL}{page}', cookies)

        soup = BeautifulSoup(r.content, 'html.parser')
        book_link_tags = soup.find_all("a", {"class": 'book book--vertical'})
        for tag in book_link_tags:
            file.write(f'https://tula-online.org{tag["href"]}\n')
