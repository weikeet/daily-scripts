# -*- coding: utf-8 -*-

import os
import json

base_project_path = '/Users/weicools/Projects/Enerjoy/'
space_lib_config_path = base_project_path + 'app_maxcleanercn_android/app/src/oneAppMaxCleanerCN/libmaxconfig.json'
ppp_lib_config_path = base_project_path + 'app_maxsecuritycn_android/app/src/oneAppMaxSecurityProCN/libmaxconfig.json'
op_lib_config_path = base_project_path + 'app_maxcn_android/app/src/oneAppMaxCN/libmaxconfig.json'
fc_lib_config_path = base_project_path + 'app_fastclearcn_android/app/src/fastClear/libmaxconfig.json'
wk_lib_config_path = base_project_path + 'app_walkcn_android/app/src/walkK/libmaxconfig.json'

lib_max_root_path = "/Users/weicools/Projects/Enerjoy/app_maxcn_android/libs/ihs/libMax/"

all_module_config = []
all_module_name_list = []


def get_all_module_name_list(file_dir):
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        all_module_name_list.append(files)
        if os.path.isdir(files):
            pass


def read_config(config_path):
    with open(config_path, 'r') as f:
        config_json = json.load(f)

    for mod in config_json:
        all_module_config.append(mod['module_name'])


get_all_module_name_list(lib_max_root_path)
read_config(space_lib_config_path)
read_config(ppp_lib_config_path)
read_config(op_lib_config_path)
read_config(fc_lib_config_path)
read_config(wk_lib_config_path)

# print(all_module_config)
# for module in all_module_config:
#     print(module)

for module in all_module_name_list:
    if module not in all_module_config:
        print(module)
