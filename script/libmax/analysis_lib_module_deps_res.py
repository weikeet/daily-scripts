# fraction dimen -> dimens
# color -> colors
# string plurals -> strings
# style -> styles

# exclude attrs.xml, ids.xml

import os
import json
from xml.etree.ElementTree import parse, Element
import xml.etree.ElementTree as Et

app_res_root_path = "/Users/weicools/Projects/Enerjoy/app_maxsecuritycn_android/app/src/main/res/"
lib_max_root_path = "/Users/weicools/Projects/Enerjoy/app_maxsecuritycn_android/libs/ihs/libMax/"

anim_path = "res/anim/"
animator_path = "res/animator/"
drawable_path = "res/drawable/"
drawable_v21_path = "res/drawable-v21/"
drawable_xx_path = "res/drawable-xxhdpi/"
layout_path = "res/layout/"
raw_path = "res/raw/"
values_path = "res/values/"

res_path_list = ['anim', 'animator', 'drawable', 'drawable-v21', 'drawable-v24', 'drawable-xxhdpi', 'layout', 'raw',
                 'values']


def printStrings(value_paths):
    doc = Et.parse(value_paths + 'strings.xml')
    root = doc.getroot()

    # print('root-tag:', root.tag, ',root-attrib:', root.attrib, ',root-text:', root.text)
    for child in root:
        print('child-tag是：', child.tag, ',child.attrib：', child.attrib, ',child.text：', child.text)
        for sub in child:
            print('sub-tag是：', sub.tag, ',sub.attrib：', sub.attrib, ',sub.text：', sub.text)


def traversal_level1_path(root_path):
    traversal_list = []
    all_files = os.listdir(root_path)
    for m_files in all_files:
        m_files_path = os.path.join(root_path, m_files)
        if os.path.isdir(m_files_path):
            if m_files not in traversal_list:
                traversal_list.append(m_files)
    traversal_list.sort()
    return traversal_list


def fetch_all_res_type(app_res_list):
    white_list = ['wifi', 'donepage', 'specificclean', 'setting']
    res_type_list = []
    for app_res in app_res_list:
        if app_res not in white_list:
            continue
        mod_res_type_list = traversal_level1_path(app_res_root_path + app_res)
        for mod_res_type in mod_res_type_list:
            if mod_res_type.startswith('values-'):
                print(app_res, mod_res_type)
            if mod_res_type.startswith('drawable-hdpi'):
                print(app_res, mod_res_type)
            if mod_res_type not in res_type_list:
                res_type_list.append(mod_res_type)

    traversal_lib_max_list = traversal_level1_path(lib_max_root_path)
    for lib_max in traversal_lib_max_list:
        if lib_max in white_list:
            continue
        lib_max_res_path = lib_max_root_path + lib_max + '/res/'
        if not os.path.exists(lib_max_res_path):
            continue
        mod_res_type_list = traversal_level1_path(lib_max_res_path)
        for mod_res_type in mod_res_type_list:
            if mod_res_type.startswith('values-'):
                print(lib_max_res_path, mod_res_type)
            if mod_res_type == 'settinglist':
                print(lib_max_res_path, mod_res_type)
            if mod_res_type not in res_type_list:
                res_type_list.append(mod_res_type)

    res_type_list.sort()
    return res_type_list


app_module_res_list = traversal_level1_path(app_res_root_path)
print(app_module_res_list)

res_type_lista = fetch_all_res_type(app_module_res_list)
print(res_type_lista)
