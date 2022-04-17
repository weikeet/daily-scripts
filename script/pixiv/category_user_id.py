# -*- coding: utf-8 -*-
import json
import os
import time

pixiv_image_folder = '/Volumes/Common/PixivPictures/'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]

user_illust_count_map = {}
failed_image_list = []


def pre_handler_file_name(file_name):
    user_id = file_name.split('_')[0]
    if user_id in user_illust_count_map:
        user_illust_count_map[user_id] = user_illust_count_map[user_id] + 1
    else:
        user_illust_count_map[user_id] = 1


def move_file_name(file_name):
    user_id = file_name.split('_')[0]
    try:
        origin_file_name = pixiv_image_folder + file_name
        if user_id in user_illust_count_map and user_illust_count_map[user_id] >= 6:
            new_file_path = pixiv_image_folder + user_id + '/'
            if not os.path.exists(new_file_path):
                os.mkdir(new_file_path)
            os.rename(origin_file_name, new_file_path + file_name)
        else:
            os.rename(origin_file_name, pixiv_image_folder + file_name)
    except FileNotFoundError:
        print('Data size error111#', file_name)
        failed_item_er = {'file_name2': file_name, 'id_str': 'None', 'error_msg': 'Data size error'}
        failed_image_list.append(failed_item_er)


if __name__ == '__main__':
    total_img = len(names)
    for _f_name in names:
        if _f_name.endswith('.jpg'):
            pre_handler_file_name(_f_name)
        elif _f_name.endswith('.png'):
            pre_handler_file_name(_f_name)
        elif _f_name.endswith('.gif'):
            pre_handler_file_name(_f_name)
        else:
            if _f_name != '.DS_Store':
                print('Not is end with .jpg/png/gif#', _f_name)
                failed_item = {'file_name': _f_name, 'id_str': 'None', 'error_msg': 'Not is end with .jpg/png/gif'}
                failed_image_list.append(failed_item)

    for _f_name in names:
        if _f_name.endswith('.jpg'):
            move_file_name(_f_name)
        elif _f_name.endswith('.png'):
            move_file_name(_f_name)
        elif _f_name.endswith('.gif'):
            move_file_name(_f_name)
        else:
            pass

    if len(failed_image_list) > 0:
        failed_image_json_str = json.dumps(failed_image_list, ensure_ascii=False)
        json_file = open('failed_image_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
        json_file.write(failed_image_json_str)
