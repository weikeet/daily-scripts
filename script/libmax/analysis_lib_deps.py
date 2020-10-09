# -*- coding: utf-8 -*-

import os
import json

lib_max_root_path = "/Users/weicools/Projects/Enerjoy/app_maxcn_android/libs/ihs/libMax/"
package_path = "/com/optimizer/test/module/"

exist_dep_module = {}

all_module_name_list = []

white_module_list = ['adwrapper', 'common', 'donepage', 'externalcontrol', 'fonts', 'glidex',
                     'packagemanager', 'permission', 'setting', 'umpush', 'userpresent']


def file_name_walk(module_name):
    file_dir = lib_max_root_path + module_name + '/java' + package_path + module_name
    # root 当前目录路径, dirs 当前路径下所有子目录, files当前路径下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        for java_file in files:
            java_file_path = root + '/' + java_file
            f = open(java_file_path, "r")
            lines = f.readlines()
            for line in lines:
                if line.startswith('import ') and '.module' in line:
                    line_module = line.split('.')[4]
                    if line_module not in white_module_list and line_module != module_name:
                        class_na = java_file_path.replace(lib_max_root_path + module_name + '/java/', '')
                        if module_name not in exist_dep_module:
                            exist_dep_module[module_name] = {}
                        if class_na not in exist_dep_module[module_name]:
                            exist_dep_module[module_name][class_na] = []
                        exist_dep_module[module_name][class_na].append(line.replace('\n', ''))


def get_all_module_name_list(file_dir):
    for m_files in os.listdir(file_dir):
        m_files_path = os.path.join(file_dir, m_files)
        if os.path.isdir(m_files_path):
            all_module_name_list.append(m_files)


def fetch_import_class():
    for module_name in all_module_name_list:
        file_name_walk(module_name)
    exist_dep_module_js = json.dumps(exist_dep_module, ensure_ascii=False)
    json_file = open('exist_dep_module.json', 'w')
    json_file.write(exist_dep_module_js)
    print('all_module_name_list', len(all_module_name_list), 're_mod', len(exist_dep_module))


get_all_module_name_list(lib_max_root_path)
fetch_import_class()
