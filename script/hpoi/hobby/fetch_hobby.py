# -*- coding: utf-8 -*-

import lxml
import requests
from bs4 import BeautifulSoup


def download(file_path, picture_url):
    r = requests.get(picture_url)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def fetch_emoji(html_path):
    with open(html_path, 'r') as f:
        html_str = f.read()
        soup = BeautifulSoup(html_str, 'lxml')
        # Find element which have href attr
        # el = soup.find(href=True)

        # Print href value
        # print(el['href'])
        # li_emoji = soup.findAll('a', class_='emoji')
        # for li in li_emoji:
        #     li_img = li.find('img')
        #     src_url = li_img['src']
        #     print(src_url)


download("157513.html", "https://www.hpoi.net/album/157513")

# fetch_emoji('img.html')
