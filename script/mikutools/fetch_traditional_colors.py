# -*- coding: utf-8 -*-

import time
import json

from bs4 import BeautifulSoup

with open('ch-colors.html', 'r', encoding='utf-8') as color_html_file:
    htmlStr = color_html_file.read()

    color_data = {}

    soup = BeautifulSoup(htmlStr, 'lxml')
    color_block_divs = soup.findAll('div', class_='color-block')
    for color_block in color_block_divs:
        bg_div = color_block.find('div', class_='bg')
        bg_style = bg_div.get('style')
        color_hex_value = bg_style[17:24]
        name_div = color_block.find('div', class_='name-n')
        color_name = str(name_div.string)
        # print(color_name, type(color_name))
        # color_name = (color_name.encode('utf-8')).decode('utf-8')

        color_data[color_name] = color_hex_value

    color_json_str = json.dumps(str(color_data))
    print(color_json_str)

    json_file = open('ch-colors.json', 'w')
    json_file.write(color_json_str)

