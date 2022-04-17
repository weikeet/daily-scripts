# -*- coding: utf-8 -*-
import json
import os
import time

import requests

failed_image_list = []
failure_image_list = []

# illust Id 通过插画ID获取插画信息
api_px_illust = 'https://api.obfs.dev/api/pixiv/illust?id='
# # member Id 通过用户ID获取用户信息
# api_px_member = 'https://api.kyomotoi.moe/api/pixiv/member?id='
# # member Id 通过用户ID获取用户作品列表
# api_px_member_illust = 'https://api.kyomotoi.moe/api/pixiv/member_illust?id='
# # user Id 查看用户收藏
# api_px_favorite = 'https://api.imjad.cn/pixiv/v1/?type=favorite&id='

pixiv_image_folder = 'E:\\MiPictures\\PixivPictures'

ID_IS_NULL = 'Id is null'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]


def load_illust_detail(file_name, id_str, px, suffix):
    print(file_name, id_str, px)
    res = requests.get(api_px_illust + id_str)
    res_json = json.loads(res.text)
    if 'illust' not in res_json:
        print(id_str, 'not found')
        failure_image_list.append({'file_name': file_name, 'id_str': id_str, 'error_msg': 'not found illust'})
        return

    response_json = res_json['illust']
    # title = response_json['title']
    user = response_json['user']
    user_id = user['id']
    print(user_id)
    # user_name = user['name']

    # NewFileName = 作者ID_作品ID_px.jpg/png/gif
    if px == '':
        new_file_name = str(user_id) + '_' + id_str + suffix
    else:
        new_file_name = str(user_id) + '_' + id_str + '_' + px + suffix

    try:
        origin_path = os.path.join(pixiv_image_folder, file_name)
        target_path = os.path.join(pixiv_image_folder, new_file_name)
        os.rename(origin_path, target_path)
        os.remove(origin_path)
    except FileNotFoundError:
        failed_image_list.append({'file_name': file_name, 'id_str': id_str, 'error_msg': 'File rename error'})


def get_image_file_id(file_name, suffix):
    for name_item in file_name.split('_'):
        name_item = name_item.replace(suffix, '')
        if 4 < len(name_item) <= 8:
            try:
                int(name_item)  # check id valid
                return name_item
            except ValueError:
                pass
    return ID_IS_NULL


def pre_handler_file_name(file_name, suffix):
    file_name_s = file_name.split('_')
    # 作者Name_作品Id.jpg/png/gif or 作者Name_作品Id_x.jpg/png/gif
    if len(file_name_s) == 2 or len(file_name_s) == 3:
        px = ''
        if len(file_name_s) == 3:
            px = 'p' + file_name_s[2].replace(suffix, '')
        image_id_str = get_image_file_id(file_name, suffix)
        if image_id_str != ID_IS_NULL:
            load_illust_detail(file_name, image_id_str, px, suffix)
        else:
            failed_image_list.append({'file_name': file_name, 'id_str': 'None', 'error_msg': 'File id format error'})
    else:
        failed_image_list.append({'file_name': file_name, 'id_str': 'None', 'error_msg': 'Data size error'})


if __name__ == '__main__':
    for _f_name in names:
        if _f_name.endswith('.jpg'):
            pre_handler_file_name(_f_name, '.jpg')
        elif _f_name.endswith('.png'):
            pre_handler_file_name(_f_name, '.png')
        elif _f_name.endswith('.gif'):
            pre_handler_file_name(_f_name, '.gif')
        else:
            if _f_name != '.DS_Store':
                failed_image_list.append({'file_name': _f_name, 'id_str': 'None', 'error_msg': 'Not is end with .jpg/png/gif'})

    time_str = time.strftime('%Y%m%d%H', time.localtime())
    if len(failed_image_list) > 0:
        failed_image_json_str = json.dumps(failed_image_list, ensure_ascii=False)
        json_file = open('failed_image_' + time_str + '.json', 'w')
        json_file.write(failed_image_json_str)

    if len(failure_image_list) > 0:
        failure_image_json_str = json.dumps(failure_image_list, ensure_ascii=False)
        failure_json_file = open('failure_image_' + time_str + '.json', 'w')
        failure_json_file.write(failure_image_json_str)
