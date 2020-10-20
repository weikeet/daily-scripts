# -*- coding: utf-8 -*-

import json

archive_module_list = []

with open('code/lib_config_code_export_all.json', 'r') as fb:
    all_module_code_config = json.load(fb)

with open('res/lib_config_res_export_all.json', 'r') as fb:
    all_module_res_config = json.load(fb)

with open('traversal_lib_max.json', 'r') as fb:
    traversal_lib_max_list = json.load(fb)

# 检查LibMax模块是否被配置到 代码/资源中
for module in traversal_lib_max_list:
    if module in all_module_code_config or module in all_module_res_config:
        pass
    else:
        archive_module_list.append(module)

# 检查资源配置中的模块在LibMax是否存在
for module in all_module_code_config:
    if module not in traversal_lib_max_list:
        print("Not exist", module)

# 检查代码配置中的模块在LibMax是否存在
for module in all_module_res_config:
    if module not in traversal_lib_max_list:
        print("Not exist res", module)

# 检查代码配置中的模块在LibMax是否存在
for module in all_module_res_config:
    if module not in all_module_code_config:
        print("Only exist res", module)

# 检查代码配置中的模块在LibMax是否存在
for module in all_module_code_config:
    if module not in all_module_res_config:
        print("Only exist code", module)

print("archive", len(archive_module_list), archive_module_list)

# Only exist res promote
# Only exist res redpacket
# Only exist code advance
# Only exist code adwrapper
# Only exist code alipush
# Only exist code batterymonitor
# Only exist code blockednotificationdata
# Only exist code crosspromotion
# Only exist code friendsgreeting
# Only exist code glidex
# Only exist code jpush
# Only exist code junkmanager
# Only exist code ktx
# Only exist code launchbadge
# Only exist code onetapboost
# Only exist code packagemanager
# Only exist code remind
# Only exist code shortvideo
# Only exist code topappmonitor
# Only exist code userpresent
# Only exist code utils
# Only exist code wificommon
# ['apkfilemonitor', 'appboost', 'applockthemepage', 'chargingreport',
# 'cloudobject', 'fetchnews', 'h5games', 'junknotification',
# 'messagesecurity', 'notificationsystem', 'ownawaymonitor',
# 'systemshortcutcenter', 'timepoint', 'webprotection']
