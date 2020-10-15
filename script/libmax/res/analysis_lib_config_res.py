# -*- coding: utf-8 -*-

import json

all_module_res = []
app_module_res = {}

op_name = 'app_maxcn_android'
pp_name = 'app_maxsecuritycn_android'
sp_name = 'app_maxcleanercn_android'
fc_name = 'app_fastclearcn_android'
wk_name = 'app_walkcn_android'

config_key = 'config'
no_config_key = 'no_config'

with open('lib_config_res.json', 'r') as f:
    config_res_json = json.load(f)

for name, res_list in config_res_json.items():
    if name not in app_module_res:
        app_module_res[name] = {}
    if config_key not in app_module_res[name]:
        app_module_res[name][config_key] = []

    for res_src in res_list:
        module_res = res_src.split('/')[4]
        if module_res not in all_module_res:
            all_module_res.append(module_res)
        if module_res not in app_module_res[name]:
            app_module_res[name][config_key].append(module_res)

# 排序 all
all_module_res.sort()
print(all_module_res)

# 筛选指定项目未配置的 module
for module_res in all_module_res:
    for name, res_map in app_module_res.items():
        if module_res not in res_map[config_key]:
            if no_config_key not in res_map:
                res_map[no_config_key] = []
            res_map[no_config_key].append(module_res)

# 排序 app
for name, res_map in app_module_res.items():
    if config_key in res_map:
        res_map[config_key].sort()
    if no_config_key in res_map:
        res_map[no_config_key].sort()
print(app_module_res)

all_module_res_js = json.dumps(all_module_res, ensure_ascii=False)
json_file = open('lib_config_res_export_all.json', 'w')
json_file.write(all_module_res_js)

app_module_res_js = json.dumps(app_module_res, ensure_ascii=False)
json_file = open('lib_config_res_export_app.json', 'w')
json_file.write(app_module_res_js)
