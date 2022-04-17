# -*- coding: utf-8 -*-
import json
import os
import time

pixiv_image_folder = 'E:\\Pixiv'


def get_all_files(input_dir):
    names = [name for name in os.listdir(input_dir)
             if os.path.isfile(os.path.join(input_dir, name))]
    return names


def get_all_folders(input_dir):
    names = [name for name in os.listdir(input_dir)
             if os.path.isdir(os.path.join(input_dir, name))]
    return names


if __name__ == '__main__':
    user_folders = get_all_folders(pixiv_image_folder)
    i = 0
    for user_folder in user_folders:
        user_folder_path = os.path.join(pixiv_image_folder, user_folder)
        illust_files = get_all_files(user_folder_path)
        for illust in illust_files:
            # if i > 200:
            #     break
            # i = i + 1
            spl = illust.split('_')
            if len(spl) > 2:
                ends = spl[2].split('.')
                if len(ends) > 1:
                    new_illust = spl[0] + '_' + spl[1] + '_' + ends[0].replace('p', '') + '.' + ends[1]
                    print(illust, new_illust)
                    os.rename(os.path.join(user_folder_path, illust), os.path.join(user_folder_path, new_illust))
