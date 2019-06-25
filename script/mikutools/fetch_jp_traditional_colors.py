# -*- coding: utf-8 -*-

import json

import requests
from bs4 import BeautifulSoup

res = requests.get('http://nipponcolors.com/#omeshicha')
res.encoding = 'utf-8'
html_text = res.text

soup = BeautifulSoup(html_text, 'lxml')

jp_color_desc = {}
for i in range(250):
    idt = i + 1
    if idt < 10:
        ids = 'col00' + str(idt)
    elif idt < 100:
        ids = 'col0' + str(idt)
    else:
        ids = 'col' + str(idt)

    color_li = soup.find(id=ids)
    _a = color_li.findAll('a')
    color_desc = _a[0].get_text()
    color_desc_s = color_desc.split(', ', 1)
    color_name = color_desc_s[0]
    color_pinyin = color_desc_s[1]
    jp_color_desc[color_name] = color_pinyin

res = requests.get('https://miku.tools/japan_colors')
res.encoding = 'utf-8'
html_text = res.text

soup = BeautifulSoup(html_text, 'lxml')
color_block_divs = soup.findAll('div', class_='color-block')
print(len(color_block_divs))

all_color_list = []
for color_block in color_block_divs:
    bg_div = color_block.find('div', class_='bg')
    bg_style = bg_div.get('style')
    color_hex_value = bg_style[17:24]

    if ';' in color_hex_value:
        print(color_hex_value)
        color_hex_value = color_hex_value[0:4]
        x = color_hex_value[1:2]
        y = color_hex_value[2:3]
        z = color_hex_value[3:4]
        color_hex_value = '#' + x + x + y + y + z + z

    color_rgb_r = str(int(color_hex_value[1:3], 16))
    color_rgb_g = str(int(color_hex_value[3:5], 16))
    color_rgb_b = str(int(color_hex_value[5:7], 16))
    color_rgb_value = color_rgb_r + ',' + color_rgb_g + ',' + color_rgb_b

    name_div = color_block.find('div', class_='name-n')
    color_name = str(name_div.string)
    # 移除 \n 空格 ' '
    color_name = ' '.join(color_name.replace('\n', '').split())

    color_pinyin = jp_color_desc.get(color_name)
    color_item = {'color_name': color_name, 'color_pinyin': color_pinyin, 'color_hex_value': color_hex_value,
                  'color_rgb_value': color_rgb_value}
    all_color_list.append(color_item)

color_json_str = json.dumps(all_color_list, ensure_ascii=False)
json_file = open('jp_colors.json', 'w')
json_file.write(color_json_str)
