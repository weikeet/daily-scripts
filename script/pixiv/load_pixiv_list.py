# -*- coding: utf-8 -*-
import json
import os

import requests

failed_image_list = []

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
# pixiv_image_folder = '/Volumes/Common/TestPixiv/'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]


def load_illust_detail(file_name, id_str, end_name):
    res = requests.get(api_pixiv_illust + id_str)
    res_json = json.loads(res.text)
    if res_json['status'] != 'success':
        print('ResponseStatus#', res_json['status'], 'FileName:', file_name)
        failed_item = {'file_name': file_name, 'id_str': id_str, 'error_msg': res_json['status']}
        failed_image_list.append(failed_item)
        return

    response_json = res_json['response'][0]
    title = response_json['title']
    user = response_json['user']
    user_id = user['id']
    user_name = user['name']
    if end_name == '':
        new_file_name = str(user_id) + '_' + id_str + '_' + user_name + '_' + title + '.jpg'
    else:
        new_file_name = str(user_id) + '_' + id_str + '_' + end_name + '_' + user_name + '_' + title + '.jpg'

    new_pixiv_image_folder = pixiv_image_folder + 'Rename/'
    try:
        os.rename(pixiv_image_folder + file_name, new_pixiv_image_folder + new_file_name)
    except FileNotFoundError:
        try:
            title = title.replace('/', ' ')
            user_name = user_name.replace('/', ' ')
            if end_name == '':
                new_file_name = str(user_id) + '_' + id_str + '_' + user_name + '_' + title + '.jpg'
            else:
                new_file_name = str(user_id) + '_' + id_str + '_' + end_name + '_' + user_name + '_' + title + '.jpg'
            os.rename(pixiv_image_folder + file_name, new_pixiv_image_folder + new_file_name)
        except FileNotFoundError:
            print('RenameError:', 'OldName:', pixiv_image_folder + file_name, 'NewName:',
                  new_pixiv_image_folder + new_file_name)
            failed_item = {'file_name': file_name, 'id_str': id_str, 'error_msg': 'File rename error'}
            failed_image_list.append(failed_item)


for file_name in names:
    if file_name.endswith('.jpg'):
        file_name_s = file_name.split('_')
        # todo 判断Str size = 8 取ID
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
                print('File id format error#', file_name)
                failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'File id format error'}
                failed_image_list.append(failed_item)
        else:
            print('Data size error#', file_name)
            failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Data size error'}
            failed_image_list.append(failed_item)
    else:
        if file_name == '.DS_Store':
            pass
        else:
            print('Not is end with .jpg#', file_name)
            failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Not is end with .jpg'}
            failed_image_list.append(failed_item)

    failed_image_json_str = json.dumps(failed_image_list, ensure_ascii=False)
    json_file = open('failed_image.json', 'w')
    json_file.write(failed_image_json_str)
