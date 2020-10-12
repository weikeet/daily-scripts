# -*- coding: utf-8 -*-

import os
import json

op_name = 'app_maxcn_android'
pp_name = 'app_maxsecuritycn_android'
sp_name = 'app_maxcleanercn_android'
fc_name = 'app_fastclearcn_android'
wk_name = 'app_walkcn_android'

project_dict = {
    op_name: "oneAppMaxCN",
    pp_name: "oneAppMaxSecurityProCN",
    sp_name: "oneAppMaxCleanerCN",
    fc_name: "fastClear",
    wk_name: "walkK"
}

lib_root_path = '/Users/weicools/Projects/Enerjoy/{name}/libs/ihs/libMax/'

all_module_name_list = []


def traversal_lib_max(root_path):
    all_files = os.listdir(root_path)
    for m_files in all_files:
        m_files_path = os.path.join(root_path, m_files)
        if os.path.isdir(m_files_path):
            if m_files not in all_module_name_list:
                all_module_name_list.append(m_files)


for name, flavor in project_dict.items():
    tm_path = lib_root_path.format(name=name)
    traversal_lib_max(tm_path)

if ".idea" in all_module_name_list:
    all_module_name_list.remove(".idea")

all_module_name_list_js = json.dumps(all_module_name_list, ensure_ascii=False)
json_file = open('traversal_lib_max.json', 'w')
json_file.write(all_module_name_list_js)
