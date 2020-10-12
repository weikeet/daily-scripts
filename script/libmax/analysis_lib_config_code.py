# -*- coding: utf-8 -*-

import os
import json

config_key = 'config'
no_config_key = 'no_config'

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

lib_config_path = '/Users/weicools/Projects/Enerjoy/{name}/app/src/{flavor}/libmaxconfig.json'

with open('lib_config_res_export_all.json', 'r') as fb:
    all_module_res_config = json.load(fb)

with open('lib_config_res_export_all.json', 'r') as fb:
    all_module_name_list = json.load(fb)

app_module_config = {}
all_module_config = []
archive_module_list = []


def read_config(config_path, app_name):
    with open(config_path, 'r') as fb:
        config_json = json.load(fb)

    for mod in config_json:
        module_name = mod['module_name']
        if module_name not in all_module_config:
            all_module_config.append(module_name)

        if app_name not in app_module_config:
            app_module_config[app_name] = {}
        if config_key not in app_module_config[name]:
            app_module_config[app_name][config_key] = []

        if module_name not in app_module_config[app_name][config_key]:
            app_module_config[app_name][config_key].append(module_name)


for name, flavor in project_dict.items():
    tm_path = lib_config_path.format(name=name, flavor=flavor)
    read_config(tm_path, name)

for module in all_module_config:
    for name, res_map in app_module_config.items():
        if module not in res_map[config_key]:
            if no_config_key not in res_map:
                res_map[no_config_key] = []
            res_map[no_config_key].append(module)

for module in all_module_name_list:
    if module in all_module_config or module in all_module_res_config:
        pass
    else:
        archive_module_list.append(module)

for module in all_module_config:
    if module not in all_module_name_list:
        print("Not exist", module)

for module in all_module_res_config:
    if module not in all_module_name_list:
        print("Not exist res", module)

print("archive", archive_module_list)
print()
print("app_config", app_module_config)

all_module_config_js = json.dumps(all_module_config, ensure_ascii=False)
json_file = open('lib_config_code_export_all.json', 'w')
json_file.write(all_module_config_js)

app_module_config_js = json.dumps(app_module_config, ensure_ascii=False)
json_file = open('lib_config_code_export_app.json', 'w')
json_file.write(app_module_config_js)
