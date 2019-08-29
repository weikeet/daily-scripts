# -*- encoding: utf-8 -*-
import os
import json
import time
import subprocess


def compare_brew_tap_list(brew_tap_list):
    brew_tap_list_bytes = subprocess.check_output(['brew', 'tap'])
    brew_tap_list_text = brew_tap_list_bytes.decode('utf-8')
    brew_tap_list_local = brew_tap_list_text.split('\n')
    brew_tap_list_local.remove('')

    diff_local_with_remote = []
    for local_item in brew_tap_list_local:
        if local_item not in brew_tap_list:
            diff_local_with_remote.append(local_item)
    print('新引入:', diff_local_with_remote)
    print('\n')

    diff_remote_with_local = []
    for remote_item in brew_tap_list:
        
        if remote_item not in brew_tap_list_local:
            diff_remote_with_local.append(remote_item)
    print('未引入:', diff_remote_with_local)

    return diff_local_with_remote


def compare_brew_list(brew_list):
    brew_list_bytes = subprocess.check_output(['brew', 'list'])
    brew_list_text = brew_list_bytes.decode('utf-8')
    brew_list_local = brew_list_text.split('\n')
    brew_list_local.remove('')

    brew_list_remote = []
    brew_list_remote_unknown = []
    for brew_item in brew_list:
        if brew_item['tag'] == 'unknown':
            brew_list_remote_unknown.append(brew_item['name'])
        else:
            brew_list_remote.append(brew_item['name'])
    print('Unknown:', brew_list_remote_unknown)
    print('\n')

    diff_local_with_remote = []
    item_list_new_install = []
    for local_item in brew_list_local:
        if local_item in brew_list_remote_unknown:
            pass
        elif local_item not in brew_list_remote:
            local_item_dict = {}
            local_item_dict['name'] = local_item
            local_item_dict['desc'] = ""
            local_item_dict['tag'] = ""
            local_item_dict['url'] = ""
            item_list_new_install.append(local_item_dict)
            diff_local_with_remote.append(local_item)
    print('新安装:', diff_local_with_remote)
    print('\n')

    diff_remote_with_local = []
    for remote_item in brew_list_remote:
        if remote_item not in brew_list_local:
            diff_remote_with_local.append(remote_item)
    print('未安装:', diff_remote_with_local)

    return item_list_new_install


def compare_brew_cask_list(brew_cask_list):
    brew_cask_list_bytes = subprocess.check_output(['brew', 'cask', 'list'])
    brew_cask_list_text = brew_cask_list_bytes.decode('utf-8')
    brew_cask_list_local = brew_cask_list_text.split('\n')
    brew_cask_list_local.remove('')

    brew_cask_list_remote = []
    for brew_cask_item in brew_cask_list:
        brew_cask_list_remote.append(brew_cask_item['name'])

    diff_local_with_remote = []
    cask_item_list_new_install = []
    for local_item in brew_cask_list_local:
        if local_item not in brew_cask_list_remote:
            local_item_dict = {}
            local_item_dict['name'] = local_item
            local_item_dict['desc'] = ""
            local_item_dict['tag'] = ""
            local_item_dict['url'] = ""
            local_item_dict['plaid'] = False
            local_item_dict['crack'] = ""
            cask_item_list_new_install.append(local_item_dict)
            diff_local_with_remote.append(local_item)
    print('新安装Cask:', diff_local_with_remote)
    print('\n')

    diff_remote_with_local = []
    for remote_item in brew_cask_list_remote:
        if remote_item not in brew_cask_list_local:
            diff_remote_with_local.append(remote_item)
    print('未安装Cask:', diff_remote_with_local)

    return cask_item_list_new_install


def sort_by_name(elem):
    return elem['name']


with open('brew_backup_2019081823.json') as backup_file:
    brew_backup_json = json.load(backup_file)

    brew_tap_list = brew_backup_json['brew_tap']
    brew_list = brew_backup_json['brew_list']
    brew_cask_list = brew_backup_json['brew_cask_list']

    print('--------------------------------')
    tap_item_list_new_install = compare_brew_tap_list(brew_tap_list)
    print('--------------------------------\n')
    
    print('********************************')
    item_list_new_install = compare_brew_list(brew_list)
    print('********************************\n')
    
    print('################################')
    cask_item_list_new_install = compare_brew_cask_list(brew_cask_list)
    print('################################')

    if len(tap_item_list_new_install) > 0 or len(item_list_new_install) > 0 or len(cask_item_list_new_install) > 0:
        for tap_item_new_install in tap_item_list_new_install:
            brew_tap_list.append(tap_item_new_install)
        for item_new_install in item_list_new_install:
            brew_list.append(item_new_install)
        for cask_item_new_install in cask_item_list_new_install:
            brew_cask_list.append(cask_item_new_install)

        brew_list.sort(key=sort_by_name)
        brew_cask_list.sort(key=sort_by_name)

        new_brew_backup_dict = {"brew_tap": brew_tap_list,
                                "brew_list": brew_list, "brew_cask_list": brew_cask_list}
        new_brew_backup_json = json.dumps(
            new_brew_backup_dict, ensure_ascii=False)
        new_brew_backup_json_file = open(
            'brew_backup_'+time.strftime('%Y%m%d%H', time.localtime())+'.json', 'w')
        new_brew_backup_json_file.write(new_brew_backup_json)
    
    else:
        print('All is latest')
