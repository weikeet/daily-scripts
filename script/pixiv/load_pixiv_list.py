# -*- coding: utf-8 -*-
import json
import os
import time

import requests

failed_image_list = []
failure_image_list = []

# illust Id
api_pixiv_illust = 'https://api.imjad.cn/pixiv/v1/?type=illust&id='
# member Id
api_pixiv_member = 'https://api.imjad.cn/pixiv/v1/?type=member&id='
# member Id
api_pixiv_member_illust = 'https://api.imjad.cn/pixiv/v1/?type=member_illust&id='
# user Id
api_pixiv_favorite = 'https://api.imjad.cn/pixiv/v1/?type=favorite&id='
api_pixiv_rank = 'https://api.imjad.cn/pixiv/v1/?type=rank&id='

# pixiv_image_folder = '/Users/zhengwei.zhang/Pictures/TestPixiv/'
pixiv_image_folder = '/Volumes/Common/PixivImages/'
# pixiv_image_folder = '/Volumes/Common/PixivPictures/'
new_pixiv_image_folder = '/Volumes/Common/PixivPicturesRename1/'

ID_IS_NULL = 'Id is null'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]


def load_illust_detail(file_name, id_str, end_name, suffix):
    res = requests.get(api_pixiv_illust + id_str)
    res_json = json.loads(res.text)
    if res_json['status'] != 'success':
        print('ResponseStatus#', res_json['status'], 'FileName:', file_name)
        failed_item = {'file_name': file_name, 'id_str': id_str, 'error_msg': res_json['status']}
        failure_image_list.append(failed_item)
        return

    response_json = res_json['response'][0]
    title = response_json['title']
    user = response_json['user']
    user_id = user['id']
    user_name = user['name']

    # NewFileName = 作者ID_作品ID_PX_作者Name_作品Title.jpg/png/gif
    new_file_name = str(user_id) + '_' + id_str + '_' + end_name + '_' + user_name + '_' + title + suffix

    try:
        os.rename(pixiv_image_folder + file_name, new_pixiv_image_folder + new_file_name)
    except FileNotFoundError:
        try:
            # replace('/', ' ') 尽可能避免命名失败
            title = title.replace('/', ' ')
            user_name = user_name.replace('/', ' ')
            new_file_name = str(user_id) + '_' + id_str + '_' + end_name + '_' + user_name + '_' + title + suffix
            os.rename(pixiv_image_folder + file_name, new_pixiv_image_folder + new_file_name)
        except FileNotFoundError:
            print('RenameError:', 'OldName:', pixiv_image_folder + file_name, 'NewName:',
                  new_pixiv_image_folder + new_file_name)
            failed_item = {'file_name': file_name, 'id_str': id_str, 'error_msg': 'File rename error'}
            failed_image_list.append(failed_item)


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


def pre_handler_file_name(suffix):
    file_name_s = file_name.split('_')
    # 作者Name_作品Id.jpg/png/gif or 作者Name_作品Id_x.jpg/png/gif
    if len(file_name_s) == 2 or len(file_name_s) == 3:
        end_name = 'PX'
        if len(file_name_s) == 3:
            # end_name = 'P' + file_name_s[2].split('.')[0]
            end_name = 'P' + file_name_s[2].replace(suffix, '')
        image_id_str = get_image_file_id(file_name, suffix)
        if image_id_str != ID_IS_NULL:
            load_illust_detail(file_name, image_id_str, end_name, suffix)
        else:
            print('File id format error#', file_name)
            failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'File id format error'}
            failed_image_list.append(failed_item)
    else:
        print('Data size error#', file_name)
        failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Data size error'}
        failed_image_list.append(failed_item)


if __name__ == '__main__':
    for file_name in names:
        if file_name.endswith('.jpg'):
            pre_handler_file_name('.jpg')
        elif file_name.endswith('.png'):
            pre_handler_file_name('.png')
        elif file_name.endswith('.gif'):
            pre_handler_file_name('.gif')
        else:
            if file_name != '.DS_Store':
                print('Not is end with .jpg/png/gif#', file_name)
                failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Not is end with .jpg/png/gif'}
                failed_image_list.append(failed_item)

    failed_image_json_str = json.dumps(failed_image_list, ensure_ascii=False)
    json_file = open('failed_image_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
    json_file.write(failed_image_json_str)

    failure_image_json_str = json.dumps(failure_image_list, ensure_ascii=False)
    failure_json_file = open('failure_image_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
    failure_json_file.write(failure_image_json_str)
