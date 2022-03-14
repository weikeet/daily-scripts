# -*- coding: utf-8 -*-

import lxml
import requests
from bs4 import BeautifulSoup


# ignore alert

def fetch_emoji(html_path):
    i = 0
    lll = []
    with open(html_path, 'r') as f:
        html_str = f.read()
        soup = BeautifulSoup(html_str, 'lxml')
        span_list = soup.findAll('span', class_='icon-name mat-caption')
        print(len(span_list))
        for span in span_list:
            name = str(span.text)
            name = name.replace(" ", "_").lower()
            if i < 100 and name not in lll:
                i += 1
                lll.append(name)
    print(lll)


fetch_emoji("md_action.html")
fetch_emoji("md_audio_video.html")
fetch_emoji("md_device.html")
fetch_emoji("md_image.html")
fetch_emoji("md_maps.html")
