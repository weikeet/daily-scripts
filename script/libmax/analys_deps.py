# -*- coding: utf-8 -*-

import os

lib_max_root_path = "/Users/weicools/Projects/Enerjoy/TempSpace/app_maxcn_android/libs/ihs/libMax"
package_path = "/com/optimizer/test/module/"

all_module_name_list = []
aa = ['main', 'recommendrule', 'utils', 'view', 'widget']

re_mod = {}


def file_name_walk(module_name):
    white_module_list = [module_name, 'adwrapper', 'common', 'donepage', 'externalcontrol', 'fonts', 'glidex',
                         'packagemanager', 'permission', 'setting', 'umpush', 'userpresent']
    file_dir = lib_max_root_path + '/' + module_name + '/java' + package_path + module_name
    for root, dirs, files in os.walk(file_dir):
        # print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件
        des = True
        for java_file in files:
            java_file_path = root + '/' + java_file
            f = open(java_file_path, "r")
            lines = f.readlines()
            for line in lines:
                if line.startswith('import '):
                    if 'module' in line:
                        count = 0
                        for white_module in white_module_list:
                            if white_module not in line:
                                count = count + 1
                        if count == len(white_module_list):
                            if des:
                                re_mod[module_name] = ''
                                print(java_file_path.replace(
                                    '/Users/weicools/Projects/Enerjoy/TempSpace/app_maxcn_android/libs/ihs/libMax/'
                                    + module_name + '/java/', ''))
                                des = False
                            print(line.replace('\n', ''))
            if not des:
                print('\n')
            des = True


def get_all_module_name_list(file_dir):
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        if os.path.isdir(files):
            all_module_name_list.append(files)


def fetch_import_class():
    for module_name in all_module_name_list:
        file_name_walk(module_name)
        print('\n\n')
    print(re_mod)
    print('all_module_name_list', len(all_module_name_list), 're_mod', len(re_mod))


get_all_module_name_list(lib_max_root_path)
fetch_import_class()
