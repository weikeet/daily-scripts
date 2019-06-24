# -*- coding: utf-8 -*-

import time
import json

from bs4 import BeautifulSoup

with open('ch-colors.html', 'r', encoding='utf-8') as color_html_file:
    htmlStr = color_html_file.read()

    all_color_list = []
    all_color_category_data = {}

    # Tag: 红、橙黄、绿、青、蓝、紫、粉、白、灰、棕、其他
    red_color_list = []
    orange_color_list = []
    yellow_color_list = []
    green_color_list = []
    cyan_color_list = []
    blue_color_list = []
    purple_color_list = []
    pink_color_list = []
    white_color_list = []
    gray_color_list = []
    brown_color_list = []
    others_color_list = []

    soup = BeautifulSoup(htmlStr, 'lxml')
    color_block_divs = soup.findAll('div', class_='color-block')
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
        color_rgb_value = color_rgb_r +',' + color_rgb_g + ',' + color_rgb_b

        name_div = color_block.find('div', class_='name-n')
        color_name = str(name_div.string)
        # 移除 \n
        color_name = color_name.replace('\n', '')
        # 移除 空格 ' '
        color_name = ' '.join(color_name.split())

        color_item = {'color_name': color_name, 'color_hex_value': color_hex_value, 'color_rgb_value': color_rgb_value}
        all_color_list.append(color_item)

        if color_name.endswith('红') or '银朱' in color_name or '榲桲舡' in color_name:
            # 银朱:?, 榲桲舡:?
            red_color_list.append(color_item)

        elif color_name.endswith('橙') or '金驼' in color_name or '槟榔综' in color_name or '醉瓜肉' in color_name:
            # 金驼:?, 槟榔综:?, 醉瓜肉:?
            orange_color_list.append(color_item)

        elif color_name.endswith('黄') or '肉色' in color_name:
            # 肉色:?, 淡肉色:?
            yellow_color_list.append(color_item)

        elif color_name.endswith('绿'):
            green_color_list.append(color_item)

        elif color_name.endswith('青'):
            cyan_color_list.append(color_item)

        elif color_name.endswith('蓝'):
            blue_color_list.append(color_item)

        elif color_name.endswith('紫') or '青莲' in color_name:
            # 青莲: 淡蓝紫, https://baike.baidu.com/item/%E9%9D%92%E8%8E%B2%E8%89%B2/1123639
            purple_color_list.append(color_item)

        elif color_name.endswith('粉') or '藕荷' in color_name or '淡绯' in color_name:
            # 藕荷:浅紫而略带粉红, https://baike.baidu.com/item/%E8%97%95%E8%8D%B7%E8%89%B2
            # 淡绯:?
            pink_color_list.append(color_item)

        elif color_name.endswith('白') or '汉白玉' in color_name or '米色' in color_name:
            # 汉白玉:?, 米色:?
            white_color_list.append(color_item)

        elif color_name.endswith('灰') or '淡松烟' in color_name:
            # 淡松烟:?
            gray_color_list.append(color_item)

        elif color_name.endswith('棕') or color_name.endswith('褐') \
                or '赭石' in color_name or '驼色' in color_name \
                or '豆沙' in color_name or '咖啡' in color_name\
                or '淡赭' in color_name or '中灰驼' in color_name:
            # 赭石:?, 驼色:?, 淡驼色:?, 豆沙:?, 淡豆沙:?, 咖啡:?, 淡咖啡:?, 淡赭:?, 中灰驼:?
            brown_color_list.append(color_item)

        else:
            # 米色 淡赭 豆沙 淡豆沙 藕荷 赭石 淡绯 榲桲舡 淡松烟 金驼 驼色 浅驼色
            others_color_list.append(color_item)

    all_color_category_data['tag_red'] = red_color_list
    all_color_category_data['tag_orange'] = orange_color_list
    all_color_category_data['tag_yellow'] = yellow_color_list
    all_color_category_data['tag_green'] = green_color_list
    all_color_category_data['tag_cyan'] = cyan_color_list
    all_color_category_data['tag_blue'] = blue_color_list
    all_color_category_data['tag_purple'] = purple_color_list
    all_color_category_data['tag_pink'] = pink_color_list
    all_color_category_data['tag_white'] = white_color_list
    all_color_category_data['tag_gray'] = gray_color_list
    all_color_category_data['tag_brown'] = brown_color_list
    all_color_category_data['tag_others'] = others_color_list

    color_json_str = json.dumps(all_color_list, ensure_ascii=False)
    json_file = open('ch-colors.json', 'w')
    json_file.write(color_json_str)

    color_category_json_str = json.dumps(all_color_category_data, ensure_ascii=False)
    category_json_file = open('ch-colors-category.json', 'w')
    category_json_file.write(color_category_json_str)
