# -*- coding: utf-8 -*-
import json
import os
import time

failed_image_list = []
failure_image_list = []

pixiv_image_folder = '/Volumes/Common/PixivPictures/'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]


def pre_handler_file_name(suffix):
    file_name_s = file_name.split('_')
    # 作者Name_作品Id.jpg/png/gif or 作者Name_作品Id_x.jpg/png/gif
    new_file_name = file_name_s[0] + '_' + file_name_s[1]
    if file_name_s[2] == 'PX':
        new_file_name = new_file_name + suffix
        try:
            os.rename(pixiv_image_folder + file_name, pixiv_image_folder + new_file_name)
            os.remove(pixiv_image_folder + file_name)
        except FileNotFoundError:
            failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Data size error'}
            failed_image_list.append(failed_item)

    else:
        pv_num = file_name_s[2].replace('P', '')
        if len(pv_num) < 3:
            new_file_name = new_file_name + '_' + pv_num + suffix
            try:
                os.rename(pixiv_image_folder + file_name, pixiv_image_folder + new_file_name)
                os.remove(pixiv_image_folder + file_name)
            except FileNotFoundError:
                failed_item = {'file_name': file_name, 'id_str': 'None', 'error_msg': 'Data size error'}
                failed_image_list.append(failed_item)
        else:
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
