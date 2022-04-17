# -*- coding: utf-8 -*-
import json
import os
import time

pixiv_image_folder = 'E:\\Pixiv'
pixiv_image_folder_other = 'E:\\Pixiv\\Others'
pixz = 'E:\\WeiweiMi6\\pixez'

pic_id_folder_map = {}

remove_ids = []
move_ids = []


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
    if len(idx) > 2:
        idss = idx[1]
        pic_id_folder_map[idss] = os.path.join(pixiv_image_folder, f_folder)
    else:
        idss = idx[1].replace(sub, '')
        pic_id_folder_map[idss] = os.path.join(pixiv_image_folder, f_folder)


def move_file(f_folder, f_name, sub):
    idx = f_name.split('_')
    if len(idx) > 2:
        idss = idx[1]
        if idss in pic_id_folder_map:
            remove_ids.append(f_name)
            os.remove(os.path.join(f_folder, f_name))
        else:
            print('move other', f_name)
            move_ids.append(f_name)
            os.rename(os.path.join(f_folder, f_name), os.path.join(pixiv_image_folder_other, f_name))
    else:
        idss = idx[1].replace(sub, '')
        if idss in pic_id_folder_map:
            remove_ids.append(f_name)
            os.remove(os.path.join(f_folder, f_name))
        else:
            print('move other', f_name)
            move_ids.append(f_name)
            os.rename(os.path.join(f_folder, f_name), os.path.join(pixiv_image_folder_other, f_name))


if __name__ == '__main__':
    user_folders = get_all_folders(pixiv_image_folder)
    for user_folder in user_folders:
        user_folder_path = os.path.join(pixiv_image_folder, user_folder)
        illust_files = get_all_files(user_folder_path)
        for illust in illust_files:
            if illust.endswith('.jpg'):
                pre_handler_file_name(user_folder, illust, '.jpg')
            elif illust.endswith('.png'):
                pre_handler_file_name(user_folder, illust, '.png')
            elif illust.endswith('.gif'):
                pre_handler_file_name(user_folder, illust, '.gif')

    i_files = get_all_files(pixz)
    for illf in i_files:
        if illf.endswith('.jpg'):
            move_file(pixz, illf, '.jpg')
        elif illf.endswith('.png'):
            move_file(pixz, illf, '.png')
        elif illf.endswith('.gif'):
            move_file(pixz, illf, '.gif')
