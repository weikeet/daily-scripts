# -*- coding: utf-8 -*-
import json
import os
import time

image_file_list = {"Bison倉鼠_22648483.jpg"}
ID_IS_NULL = 'Id is null'


def get_image_file_id(file_name, suffix):
    file_name_s = file_name.split('_')
    for name_item in file_name_s:
        name_item = name_item.replace(suffix, '')
        if 4 < len(name_item) <= 8:
            try:
                image_id = int(name_item)
                return name_item
            except ValueError:
                pass
    return ID_IS_NULL

print(get_image_file_id('Bison倉鼠_22648483.jpg', '.jpg'))


# for name in image_file_list:
#     file_name_s = name.split('_')
#     for name_item in file_name_s:
#         name_item = name_item.replace('.jpg', '').replace('.gif', '').replace('.png', '')
#         if 4 < len(name_item) <= 8:
#             try:
#                 image_id = int(name_item)
#                 print('File name=', name, 'image_id=', image_id)
#             except ValueError:
#                 print('File name=', name, 'Name item=' + name_item)
