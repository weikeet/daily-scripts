# -*- coding: utf-8 -*-

import os
import json

base_project_path = '/Users/weicools/Projects/Enerjoy/'
sp_lib_config_path = base_project_path + 'app_maxcleanercn_android/app/src/oneAppMaxCleanerCN/libmaxconfig.json'
op_lib_config_path = base_project_path + 'app_maxcn_android/app/src/oneAppMaxCN/libmaxconfig.json'
pp_lib_config_path = base_project_path + 'app_maxsecuritycn_android/app/src/oneAppMaxSecurityProCN/libmaxconfig.json'
fc_lib_config_path = base_project_path + 'app_fastclearcn_android/app/src/fastClear/libmaxconfig.json'
wk_lib_config_path = base_project_path + 'app_walkcn_android/app/src/walkK/libmaxconfig.json'

sp_lib_max_root_path = base_project_path + "app_maxcleanercn_android/libs/ihs/libMax/"
op_lib_max_root_path = base_project_path + "app_maxcn_android/libs/ihs/libMax/"
pp_lib_max_root_path = base_project_path + "app_maxsecuritycn_android/libs/ihs/libMax/"
fc_lib_max_root_path = base_project_path + "app_fastclearcn_android/libs/ihs/libMax/"
wk_lib_max_root_path = base_project_path + "app_walkcn_android/libs/ihs/libMax/"

all_module_res_config = ['appinstallationmonitor', 'appmanagement', 'common', 'umpush', 'appprotect', 'fastboost',
                         'permission', 'whostealdata', 'upgradealert', 'acquire', 'promote', 'setting', 'security',
                         'recyclebin', 'view', 'notificationorganizer', 'privatemessage', 'filescan', 'recommendrule',
                         'cpucooler', 'memoryboost', 'main', 'gameboost', 'smartlocker', 'widget', 'bigfiles',
                         'callassistant', 'newsfeed', 'batterysaver', 'junkclean', 'donepage', 'about', 'ratealert',
                         'photomanager', 'fonts', 'safebox', 'splash', 'clipboardmanager', 'chargingimprover',
                         'wifispeedmonitor', 'wifisafe', 'shakeboost', 'scheduledscan', 'notificationtoggle',
                         'wechatcleaner', 'externalcontrol', 'appupgrade', 'privacyalert', 'dailynews', 'smartmanager',
                         'shortvideoclean', 'wifispeedtest', 'safebrowsing', 'specificclean', 'userfeedback',
                         'authoritycenter', 'autobooster', 'datamonitor', 'redpacket', 'userquestionnaire',
                         'accelerator', 'bytepower', 'goldcoin', 'interstitialproxy', 'networkanalysis', 'promotealert',
                         'purchase', 'prizewheel', 'wifiboost', 'riskapp', 'maxbrowsing']

sp_config = []
op_config = []
pp_config = []
fc_config = []
wk_config = []

sp_no_config = []
op_no_config = []
pp_no_config = []
fc_no_config = []
wk_no_config = []

all_module_config = []
all_module_name_list = []

archive_module_list = []


def traversal_lib_max(file_dir):
    all_files = os.listdir(file_dir)
    for m_files in all_files:
        m_files_path = os.path.join(file_dir, m_files)
        if os.path.isdir(m_files_path):
            if m_files not in all_module_name_list:
                all_module_name_list.append(m_files)


def read_config(config_path):
    with open(config_path, 'r') as f:
        config_json = json.load(f)

    for mod in config_json:
        module_name = mod['module_name']
        if module_name not in all_module_config:
            all_module_config.append(module_name)

        if config_path == "":
            pass
        elif config_path == sp_lib_config_path:
            if module_name not in sp_config:
                sp_config.append(module_name)
        elif config_path == op_lib_config_path:
            if module_name not in op_config:
                op_config.append(module_name)
        elif config_path == pp_lib_config_path:
            if module_name not in pp_config:
                pp_config.append(module_name)
        elif config_path == fc_lib_config_path:
            if module_name not in fc_config:
                fc_config.append(module_name)
        elif config_path == wk_lib_config_path:
            if module_name not in wk_config:
                wk_config.append(module_name)


traversal_lib_max(sp_lib_max_root_path)
traversal_lib_max(op_lib_max_root_path)
traversal_lib_max(pp_lib_max_root_path)
traversal_lib_max(fc_lib_max_root_path)
traversal_lib_max(wk_lib_max_root_path)

read_config(sp_lib_config_path)
read_config(op_lib_config_path)
read_config(pp_lib_config_path)
read_config(fc_lib_config_path)
read_config(wk_lib_config_path)

for module in all_module_config:
    if module not in sp_config:
        sp_no_config.append(module)
    elif module not in op_config:
        op_no_config.append(module)
    elif module not in pp_config:
        pp_no_config.append(module)
    elif module not in fc_config:
        fc_no_config.append(module)
    elif module not in wk_config:
        wk_no_config.append(module)

for module in all_module_name_list:
    if module in all_module_config:
        # print(module)
        pass
    else:
        archive_module_list.append(module)

for module in all_module_config:
    if module not in all_module_name_list:
        print("Not exist", module)

for module in all_module_res_config:
    if module not in all_module_name_list:
        print("Not exist res", module)

print()
print("archive", archive_module_list)
print()

print("sp_config", sp_config)
print("op_config", op_config)
print("pp_config", pp_config)
print("fc_config", fc_config)
print("wk_config", wk_config)
print()

print("sp_no_config", sp_no_config)
print("op_no_config", op_no_config)
print("pp_no_config", pp_no_config)
print("fc_no_config", fc_no_config)
print("wk_no_config", wk_no_config)
