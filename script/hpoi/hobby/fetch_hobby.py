# -*- coding: utf-8 -*-

import sys
import lxml
import requests
import wget
from bs4 import BeautifulSoup


# def download(file_path, picture_url):
#     r = requests.get(picture_url)
#     with open(file_path, 'wb') as f:
#         f.write(r.content)


# download("157513.html", "https://www.hpoi.net/album/157513")


def fetch_emoji(dp, hi):
    with open(hi, 'r') as f:
        html_str = f.read()
        soup = BeautifulSoup(html_str, 'lxml')

        li_emoji = soup.findAll('a')
        index = 0
        for li in li_emoji:
            img_url = li['href']
            img_url_arr = img_url.split('/')
            image_file_name = img_url_arr[-1]
            print(image_file_name)
            if index < 10:
                aa = "00"+str(index)
            elif index < 100:
                aa = "0"+str(index)
            else:
                aa = str(index)
            wget.download(img_url, out=dp + "/" + aa+"_"+image_file_name)
            index += 1

if __name__ == '__main__':
    print(sys.argv[1], sys.argv[2])
    download_path = sys.argv[1]
    hobby_img_html = sys.argv[2]
    fetch_emoji(download_path, hobby_img_html)
