# -*- coding: utf-8 -*-
import json
import os
import time
import requests

pixiv_image_folder = 'E:\\Pixiv'
pixiv_image_folder_other = 'E:\\Pixiv\\Others'

user_id_folder_map = {}

remove_ids = []
move_ids = []

# illust Id 通过插画ID获取插画信息
api_px_illust = 'https://api.obfs.dev/api/pixiv/illust?id='


def get_all_files(input_dir):
    names = [name for name in os.listdir(input_dir)
             if os.path.isfile(os.path.join(input_dir, name))]
    return names


def get_all_folders(input_dir):
    names = [name for name in os.listdir(input_dir)
             if os.path.isdir(os.path.join(input_dir, name))]
    return names


def pre_handler_file_name(f_folder, f_name, sub):
    idx = f_name.split('_')
    user_id_folder_map[idx[0]] = os.path.join(pixiv_image_folder, f_folder)


def move_file(f_folder, f_name, sub):
    idx = f_name.split('_')
    user_id = idx[0]
    if user_id in user_id_folder_map:
        move_ids.append(f_name)
        os.rename(os.path.join(f_folder, f_name), os.path.join(user_id_folder_map[user_id], f_name))
    else:
        pass


user_illust_count_map = {}
user_illust_name_map = {}
user_illust_name_fail = []


def calc_user_illust_count(f_folder, f_name, sub):
    fns = f_name.split('_')
    user_id = fns[0]
    if user_id in user_illust_count_map:
        user_illust_count_map[user_id] = user_illust_count_map[user_id] + 1
    else:
        user_illust_count_map[user_id] = 1
        # if len(fns) > 2:
        #     id_str = fns[1]
        # else:
        #     id_str = fns[1].replace(sub, '')
        # print('calc', f_name, id_str)
        # res = requests.get(api_px_illust + id_str)
        # res_json = json.loads(res.text)
        # if 'illust' not in res_json:
        #     print(id_str, 'not found')
        #     # failure_image_list.append({'file_name': file_name, 'id_str': id_str, 'error_msg': 'not found illust'})
        #     return
        # response_json = res_json['illust']
        # user = response_json['user']
        # user_name = user['name']
        # user_illust_name_map[user_id] = user_name


def create_move_file(f_folder, f_name, sub):
    fns = f_name.split('_')
    user_id = fns[0]
    # print(f_name, user_illust_count_map[user_id])
    if user_illust_count_map[user_id] > 3:
        if user_id in user_illust_name_map:
            create_folder = os.path.join(pixiv_image_folder, user_id + '_' + user_illust_name_map[user_id])
        else:
            create_folder = os.path.join(pixiv_image_folder, user_id)
        if not os.path.exists(create_folder):
            os.mkdir(create_folder)
        print('move create', create_folder, f_name)
        os.rename(os.path.join(pixiv_image_folder_other, f_name), os.path.join(create_folder, f_name))
        # os.remove(os.path.join(pixiv_image_folder_other, f_name))


if __name__ == '__main__':
    # user_folders = get_all_folders(pixiv_image_folder)
    # for user_folder in user_folders:
    #     if user_folder == 'Others':
    #         break
    #     user_folder_path = os.path.join(pixiv_image_folder, user_folder)
    #     illust_files = get_all_files(user_folder_path)
    #     for illust in illust_files:
    #         if illust.endswith('.jpg'):
    #             pre_handler_file_name(user_folder, illust, '.jpg')
    #         elif illust.endswith('.png'):
    #             pre_handler_file_name(user_folder, illust, '.png')
    #         elif illust.endswith('.gif'):
    #             pre_handler_file_name(user_folder, illust, '.gif')
    #
    # i_files = get_all_files(pixiv_image_folder_other)
    # for illf in i_files:
    #     if illf.endswith('.jpg'):
    #         move_file(pixiv_image_folder_other, illf, '.jpg')
    #     elif illf.endswith('.png'):
    #         move_file(pixiv_image_folder_other, illf, '.png')
    #     elif illf.endswith('.gif'):
    #         move_file(pixiv_image_folder_other, illf, '.gif')
    #
    # print(move_ids)

    i_files = get_all_files(pixiv_image_folder_other)
    for illf in i_files:
        if illf.endswith('.jpg'):
            calc_user_illust_count(pixiv_image_folder_other, illf, '.jpg')
        elif illf.endswith('.png'):
            calc_user_illust_count(pixiv_image_folder_other, illf, '.png')
        elif illf.endswith('.gif'):
            calc_user_illust_count(pixiv_image_folder_other, illf, '.gif')
    print('------------------------------------------------------')
    for illf in i_files:
        if illf.endswith('.jpg'):
            create_move_file(pixiv_image_folder_other, illf, '.jpg')
        elif illf.endswith('.png'):
            create_move_file(pixiv_image_folder_other, illf, '.png')
        elif illf.endswith('.gif'):
            create_move_file(pixiv_image_folder_other, illf, '.gif')