# -*- encoding: utf-8 -*-

import json
import subprocess
import time


def compare_brew_tap_list(brew_tap_list_param):
    brew_tap_list_bytes = subprocess.check_output(['brew', 'tap'])
    brew_tap_list_text = brew_tap_list_bytes.decode('utf-8')
    brew_tap_list_local = brew_tap_list_text.split('\n')
    brew_tap_list_local.remove('')

    new_install_tap_names = []
    for local_name in brew_tap_list_local:
        if local_name not in brew_tap_list_param:
            new_install_tap_names.append(local_name)
    print('新引入:', new_install_tap_names, '\n')

    not_install_tap_names = []
    for remote_name in brew_tap_list_param:
        if remote_name not in brew_tap_list_local:
            not_install_tap_names.append(remote_name)
    print('未引入:', not_install_tap_names)

    return new_install_tap_names


def compare_brew_cask_list(brew_cask_list_param):
    brew_cask_list_bytes = subprocess.check_output(['brew', 'list', '--cask'])
    brew_cask_list_text = brew_cask_list_bytes.decode('utf-8')
    brew_cask_list_local = brew_cask_list_text.split('\n')
    brew_cask_list_local.remove('')

    print('已安装Cask:', brew_cask_list_local, '\n')

    brew_cask_list_remote_name = []
    for remote_item in brew_cask_list_param:
        brew_cask_list_remote_name.append(remote_item['name'])

    new_install_cask_names = []
    for local_name in brew_cask_list_local:
        if local_name not in brew_cask_list_remote_name:
            new_install_cask_names.append(local_name)
    print('新安装Cask:', new_install_cask_names, '\n')

    not_install_cask_names = []
    for remote_name in brew_cask_list_remote_name:
        if remote_name not in brew_cask_list_local:
            not_install_cask_names.append(remote_name)
    print('未安装Cask:', not_install_cask_names)

    new_install_cask_items = []
    for local_name in new_install_cask_names:
        new_install_cask_items.append({'name': local_name, 'desc': "", 'tag': "", 'url': "", 'plaid': False, 'crack': ""})
    return new_install_cask_items


def compare_brew_formula_list(brew_formula_list_param, brew_formula_unknown_list_param):
    brew_formula_list_bytes = subprocess.check_output(['brew', 'list', '--formula'])
    brew_formula_list_text = brew_formula_list_bytes.decode('utf-8')
    brew_formula_list_local = brew_formula_list_text.split('\n')
    brew_formula_list_local.remove('')

    brew_formula_list_local_name = []
    for local_name in brew_formula_list_local:
        if local_name in brew_formula_unknown_list_param:
            brew_formula_list_local.remove(local_name)
        else:
            brew_formula_list_local_name.append(local_name)
    print('已安装:', brew_formula_list_local_name, '\n')

    brew_formula_list_remote_name = []
    for remote_item in brew_formula_list_param:
        brew_formula_list_remote_name.append(remote_item['name'])

    new_install_formula_names = []
    for local_name in brew_formula_list_local_name:
        if local_name not in brew_formula_list_remote_name:
            new_install_formula_names.append(local_name)
    print('新安装:', new_install_formula_names, '\n')

    not_install_formula_names = []
    for remote_name in brew_formula_list_remote_name:
        if remote_name not in brew_formula_list_local_name:
            new_install_formula_names.append(remote_name)
    print('未安装:', not_install_formula_names)

    new_install_formula_items = []
    for local_name in new_install_formula_names:
        new_install_formula_items.append({'name': local_name, 'desc': "", 'tag': "", 'url': ""})
    return new_install_formula_items


def sort_by_name(elem):
    return elem['name']


if __name__ == '__main__':
    is_select_update = input('is select update backup.json? yes: Y, no: N =-= ')

    with open('brew_backup_2021070323.json') as backup_file:
        brew_backup_json = json.load(backup_file)

        brew_tap_list = brew_backup_json['brew_tap_list']
        brew_cask_list = brew_backup_json['brew_cask_list']
        brew_formula_list = brew_backup_json['brew_formula_list']
        brew_formula_unknown_list = brew_backup_json['brew_formula_unknown_list']

        print('---------------- tap-start ------------------------')
        new_install_tap_list = compare_brew_tap_list(brew_tap_list)
        print('---------------- tap-start ----------------------\n')

        print('################ cask-start #######################')
        new_install_cask_list = compare_brew_cask_list(brew_cask_list)
        print('################ cask-start #####################\n')

        print('**************** formula-start ********************')
        new_install_formula_list = compare_brew_formula_list(brew_formula_list, brew_formula_unknown_list)
        print('**************** formula-end **********************')

        if is_select_update == 'Y':
            if len(new_install_tap_list) > 0 or len(new_install_formula_list) > 0 or len(new_install_cask_list) > 0:
                for tap_item_new_install in new_install_tap_list:
                    brew_tap_list.append(tap_item_new_install)
                for cask_item_new_install in new_install_cask_list:
                    brew_cask_list.append(cask_item_new_install)
                for item_new_install in new_install_formula_list:
                    brew_formula_list.append(item_new_install)

                brew_tap_list.sort()
                brew_cask_list.sort(key=sort_by_name)
                brew_formula_list.sort(key=sort_by_name)
                brew_formula_unknown_list.sort()

                new_brew_backup_dict = {
                    "brew_tap_list": brew_tap_list,
                    "brew_cask_list": brew_cask_list,
                    "brew_formula_list": brew_formula_list,
                    "brew_formula_unknown_list": brew_formula_unknown_list
                }
                new_brew_backup_json = json.dumps(new_brew_backup_dict, ensure_ascii=False)
                new_brew_backup_json_file = open('brew_backup_' + time.strftime('%Y%m%d%H', time.localtime()) + '.json', 'w')
                new_brew_backup_json_file.write(new_brew_backup_json)
            else:
                print('All is latest')
