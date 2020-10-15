# -*- coding: utf-8 -*-

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

app_module_code_config = {}
all_module_code_config = []


def read_code_config(config_path, app_name):
    with open(config_path, 'r') as config_file:
        config_json = json.load(config_file)

    for config in config_json:
        module_name = config['module_name']
        if module_name not in all_module_code_config:
            all_module_code_config.append(module_name)

        if app_name not in app_module_code_config:
            app_module_code_config[app_name] = {}
        if config_key not in app_module_code_config[name]:
            app_module_code_config[app_name][config_key] = []
        if module_name not in app_module_code_config[app_name][config_key]:
            app_module_code_config[app_name][config_key].append(module_name)


# 读取所有项目的lib max config
for name, flavor in project_dict.items():
    tm_path = lib_config_path.format(name=name, flavor=flavor)
    read_code_config(tm_path, name)

# 排序 all
all_module_code_config.sort()
print("all_config", app_module_code_config)

# 筛选指定项目未配置的 module
for module in all_module_code_config:
    for name, res_map in app_module_code_config.items():
        if module not in res_map[config_key]:
            if no_config_key not in res_map:
                res_map[no_config_key] = []
            res_map[no_config_key].append(module)

# 排序 app
for name, res_map in app_module_code_config.items():
    if config_key in res_map:
        res_map[config_key].sort()
    if no_config_key in res_map:
        res_map[no_config_key].sort()

print("app_config", app_module_code_config)

all_module_config_js = json.dumps(all_module_code_config, ensure_ascii=False)
json_file = open('code/lib_config_code_export_all.json', 'w')
json_file.write(all_module_config_js)

app_module_config_js = json.dumps(app_module_code_config, ensure_ascii=False)
json_file = open('code/lib_config_code_export_app.json', 'w')
json_file.write(app_module_config_js)
