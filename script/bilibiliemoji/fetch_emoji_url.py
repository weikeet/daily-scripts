# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def download(file_path, picture_url):
    r = requests.get(picture_url)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def fetch_emoji(html_path, prefix):
    file_object = open(html_path)
    try:
        html_str = file_object.read()
        soup = BeautifulSoup(html_str)
        li_emoji = soup.findAll('li', class_='emoji')
        for li in li_emoji:
            li_div = li.find('div')
            title = li_div['title']
            style = li_div['style']
            print(title, style)

            title = title.replace("[", "").replace("]", "")
            url = style.split('(')[1].split(')')[0].replace("\"", "")
            img_url = "https:" + url
            img_path = "./media/" + prefix + title + ".png"
            download(img_path, img_url)
    finally:
        file_object.close()


fetch_emoji('Bilibili_2233娘.html', "Bilibili_")
fetch_emoji('Bilibili_Emoji.html', "Bilibili_Emoji_")
fetch_emoji('Bilibili_TV.html', "Bilibili_")
fetch_emoji('Bilibili_三周年.html', "Bilibili_")
fetch_emoji('Bilibili_热词系列.html', "Bilibili_")
fetch_emoji('Bilibili_蛆音娘.html', "Bilibili_")
