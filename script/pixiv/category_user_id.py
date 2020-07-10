# -*- coding: utf-8 -*-
import json
import os
import time

failed_image_list = []

pixiv_image_folder = '/Volumes/Common/PixivPictures/'
new_pixiv_image_folder = '/Volumes/Common/PixivPicturesRename/'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]

id_dc = {}


def pre_handler_file_name():
    file_name_s = file_name.split('_')
    if file_name_s[0] in id_dc:
        id_dc[file_name_s[0]] = id_dc[file_name_s[0]] + 1
    else:
        id_dc[file_name_s[0]] = 1


def move_file_name():
    file_name_s2 = file_name2.split('_')
    try:
        if file_name_s2[0] in id_dc and id_dc[file_name_s2[0]] >= 6:
            new_file_path = new_pixiv_image_folder + file_name_s2[0] + '/'
            if not os.path.exists(new_file_path):
                os.mkdir(new_file_path)
            os.rename(pixiv_image_folder + file_name2, new_file_path + file_name2)
        else:
            os.rename(pixiv_image_folder + file_name2, new_pixiv_image_folder + file_name2)
    except FileNotFoundError:
        print('Data size error111#', file_name2)
        failed_item_er = {'file_name2': file_name2, 'id_str': 'None', 'error_msg': 'Data size error'}
        failed_image_list.append(failed_item_er)


if __name__ == '__main__':
    total_img = len(names)
    for file_name in names:
        if file_name.endswith('.jpg'):
            pre_handler_file_name()
        elif file_name.endswith('.png'):
            pre_handler_file_name()
        elif file_name.endswith('.gif'):
            pre_handler_file_name()
        else:
            if file_name != '.DS_Store':
                print('Not is end with .jpg/png/gif#', file_name)
                failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Not is end with .jpg/png/gif'}
                failed_image_list.append(failed_item)

    for file_name2 in names:
        if file_name2.endswith('.jpg'):
            move_file_name()
        elif file_name2.endswith('.png'):
            move_file_name()
        elif file_name2.endswith('.gif'):
            move_file_name()
        else:
            pass

    if len(failed_image_list) > 0:
        failed_image_json_str = json.dumps(failed_image_list, ensure_ascii=False)
        json_file = open('failed_image_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
        json_file.write(failed_image_json_str)
