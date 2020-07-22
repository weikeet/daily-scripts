# -*- coding: utf-8 -*-
import requests
import json
import os

user_id_failed_list = []
user_id_success_list = []

px_image_folder = '/Volumes/Common/PixivPictures/'

user_ids = [name for name in os.listdir(px_image_folder)
            if os.path.isdir(os.path.join(px_image_folder, name))]

# member id api
api_px_member = 'https://api.imjad.cn/pixiv/v1/?type=member&id='


def load_user_info(user_id):
    req_result = requests.get(api_px_member + user_id)
    res_text_json = json.loads(req_result.text)

    response_status = res_text_json['status']
    if response_status != 'success':
        print('load_user_info#', response_status, 'Id:', user_id)
        user_id_failed_list.append({"id": user_id, "reason": response_status})
        return

    response_json = res_text_json['response'][0]
    user_name = response_json['name']

    try:
        os.rename(px_image_folder + user_id, px_image_folder + user_id + '_' + user_name)

        user_dict = {"id": user_id, "name": user_name}
        user_id_success_list.append(user_dict)
    except FileNotFoundError:
        user_id_failed_list.append({"id": user_id, "reason": "renameUserInfoFailed"})


if __name__ == '__main__':
    for user_id in user_ids:
        if user_id == "Others":
            continue
        load_user_info(user_id)

    if len(user_id_success_list) > 0:
        user_id_success_js = json.dumps(user_id_success_list, ensure_ascii=False)
        json_file = open('user_id_success_js.json', 'w')
        json_file.write(user_id_success_js)

    if len(user_id_failed_list) > 0:
        user_id_failed_js = json.dumps(user_id_failed_list, ensure_ascii=False)
        json_file = open('user_id_failed_js.json', 'w')
        json_file.write(user_id_failed_js)
