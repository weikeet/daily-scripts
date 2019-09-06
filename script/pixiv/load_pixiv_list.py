# -*- coding: utf-8 -*-
import json
import os

import requests

illegal_image_name_list = []
illegal_image_id_name_list = []

# illust Id
api_pixiv_illust = 'https://api.imjad.cn/pixiv/v1/?type=illust&id='
# member Id
api_pixiv_member = 'https://api.imjad.cn/pixiv/v1/?type=member&id='
# member Id
api_pixiv_member_illust = 'https://api.imjad.cn/pixiv/v1/?type=member_illust&id='
# user Id
api_pixiv_favorite = 'https://api.imjad.cn/pixiv/v1/?type=favorite&id='
api_pixiv_rank = 'https://api.imjad.cn/pixiv/v1/?type=rank&id='

pixiv_image_folder = '/Users/zhengwei.zhang/Pictures/TestPixiv/'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]


def load_illust_detail(file_name, id, end_name):
    res = requests.get(api_pixiv_illust + id)
    res_json = json.loads(res.text)
    if res_json['status'] != 'success':
        print('ResponseStatus:', res_json['status'], 'FileName:', file_name)
        return
    response_json = res_json['response'][0]
    title = response_json['title']
    user = response_json['user']
    user_id = user['id']
    user_name = user['name']
    if end_name == '':
        new_file_name = str(user_id) + '_' + id + '_' + user_name + '_' + title + '.jpg'
    else:
        new_file_name = str(user_id) + '_' + id + '_' + end_name + '_' + user_name + '_' + title + '.jpg'
    try:
        os.rename(pixiv_image_folder + file_name, pixiv_image_folder + new_file_name)
    except FileNotFoundError:
        print('RenameError:', 'OldName:', pixiv_image_folder + file_name, 'NewName:',
              pixiv_image_folder + new_file_name)


for file_name in names:
    if file_name.endswith('.jpg'):
        file_name_s = file_name.split('_')
        if len(file_name_s) == 2 or len(file_name_s) == 3:
            image_id_str = file_name_s[1][:8]
            end_name = ''
            if len(file_name_s) == 3:
                # end_name = 'P' + file_name_s[2].split('.')[0]
                end_name = 'P' + file_name_s[2].replace('.jpg', '')
            try:
                image_id = int(image_id_str)
                load_illust_detail(file_name, image_id_str, end_name)
            except ValueError:
                print('illegal_imageId_name', file_name)
                illegal_image_id_name_list.append(file_name)
        else:
            print('illegal_image_name', file_name)
            illegal_image_name_list.append(file_name)
    else:
        print('illegal_image_name', file_name)
        illegal_image_name_list.append(file_name)
