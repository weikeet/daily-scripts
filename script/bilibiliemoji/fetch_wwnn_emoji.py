# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def download(file_path, picture_url):
    r = requests.get(picture_url)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def fetch_emoji(html_path, prefix):
    with open(html_path, 'r') as f:
        html_str = f.read()
        soup = BeautifulSoup(html_str, 'lxml')
        li_emoji = soup.findAll('li', class_='emoji')
        for li in li_emoji:
            li_img = li.find('img')
            src_url = li_img['src']
            print(src_url)

            # title = title.replace("[", "").replace("]", "")
            # url = style.split('(')[1].split(')')[0].replace("\"", "")
            # img_url = "https:" + url
            # img_path = "./media/" + prefix + title + ".png"
            # download(img_path, img_url)


fetch_emoji('Wwnn_20210906.html', "Bilibili_")
