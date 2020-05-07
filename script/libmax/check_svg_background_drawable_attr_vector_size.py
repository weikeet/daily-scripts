# -*- coding: utf-8 -*-

import os
import re
import sys

# ROOT_DIR = sys.argv[1]
# flavor = sys.argv[2]
# print("ROOT_DIR=", ROOT_DIR, "flavor=", flavor)

# app_src_main_res_path = ROOT_DIR + "/app/src/main/res/"
# app_src_cn_res_path = ROOT_DIR + "/app/src/" + flavor + "/res/"
# lib_root_path = ROOT_DIR + "/libs/ihs/libMax/"

app_src_main_res_path = "/Users/weicools/Projects/Enerjoy/app_maxcn_android/app/src/main/res/"
app_src_cn_res_path = "/Users/weicools/Projects/Enerjoy/app_maxcn_android/app/src/oneAppMaxCN/res/"
lib_root_path = "/Users/weicools/Projects/Enerjoy/app_maxcn_android/libs/ihs/libMax/"
vector_size_white_list_path = "vector_size_white_list.text"

lib_drawable_key_path = "/res/drawable/"
lib_layout_key_path = "/res/layout/"
app_drawable_key_path = "/drawable/"
app_layout_key_path = "/layout/"

module_path_list = []

layout_file_path_list = []

drawable_file_path_list = []

vector_drawable_file_list = []
vector_drawable_file_path_list = []
vector_size_white_list = []

layout_error_bg_dict = {}
drawable_error_attr_dict = {}
vector_warning_size_dict = {}


def is_vector_file(drawable_file_path):
    f = open(drawable_file_path, "r")
    lines = f.readlines()
    for line in lines:
        if "<vector" in line:
            f.close()
            return True
    f.close()
    return False


def get_module_path_list(file_dir):
    if not os.path.exists(file_dir):
        return
    for files in os.listdir(file_dir):
        if os.path.isdir(file_dir + files):
            # print("get__module_path_list", files)
            module_path_list.append(file_dir + files)


def get_all_drawable_file_path():
    for module_path in module_path_list:
        drawable_path = ""
        if os.path.exists(module_path + lib_drawable_key_path):
            drawable_path = module_path + lib_drawable_key_path
        elif os.path.exists(module_path + app_drawable_key_path):
            drawable_path = module_path + app_drawable_key_path
        if drawable_path == "":
            continue

        for files in os.listdir(drawable_path):
            drawable_file_path = drawable_path + files
            if os.path.isfile(drawable_file_path) and files.endswith(".xml"):
                # print("get_all_drawable_file", files)
                drawable_file_path_list.append(drawable_file_path)

                if is_vector_file(drawable_file_path):
                    # print("get_all_drawable_file is vector", files)
                    vector_drawable_file_list.append(files)
                    vector_drawable_file_path_list.append(drawable_file_path)


def get_all_layout_file_path():
    for module_path in module_path_list:
        layout_path = ""
        if os.path.exists(module_path + lib_layout_key_path):
            layout_path = module_path + lib_layout_key_path
        elif os.path.exists(module_path + app_layout_key_path):
            layout_path = module_path + app_layout_key_path
        if layout_path == "":
            continue

        for files in os.listdir(layout_path):
            layout_file_path = layout_path + files
            if os.path.isfile(layout_file_path):
                # print("get_all_layout_file", files)
                layout_file_path_list.append(layout_file_path)


def check_svg_background():
    for layout_file_path in layout_file_path_list:
        layout_f = open(layout_file_path, "r")
        lines = layout_f.readlines()
        error_bg_tip_list = []

        for index, line in enumerate(lines):
            line = line.replace(' ', '')
            if "android:background=\"@drawable/" not in line:
                continue

            drawable_re = re.search(r'@drawable/(.*?)\"', line)
            if drawable_re is None:
                continue
            drawable = drawable_re.group(1)
            if drawable is not None:
                drawable_file = drawable + ".xml"
                if drawable_file in vector_drawable_file_list:
                    error_bg_tip_list.append(drawable_file + ", line in " + str(index + 1))
                    print("check_svg_background, error_layout=", layout_file_path, "error_bg=", drawable_file,
                          "line in ", str(index + 1))
        layout_f.close()

        if len(error_bg_tip_list) > 0:
            layout_error_bg_dict[layout_file_path] = error_bg_tip_list


def check_drawable_attr():
    for drawable_file_path in drawable_file_path_list:
        if drawable_file_path in vector_drawable_file_path_list:
            continue

        drawable_f = open(drawable_file_path, "r")
        lines = drawable_f.readlines()
        error_attr_tip_list = []

        for index, line in enumerate(lines):
            line = line.replace(' ', '')
            if "?attr/" not in line and "?android:attr/" not in line:
                continue

            attr_name_re = re.search(r'attr/(.*?)\"', line)
            if attr_name_re is not None:
                attr_name = attr_name_re.group(1)
                error_attr_tip_list.append(attr_name + ", line in " + str(index))
                print("check_drawable_attr, error_drawable=", drawable_file_path, "error_attr=", attr_name,
                      "line in ", str(index + 1))
            android_attr_name_re = re.search(r'android:attr/(.*?)\"', line)
            if android_attr_name_re is not None:
                android_attr_name = attr_name_re.group(1)
                error_attr_tip_list.append(android_attr_name + ", line in " + str(index))
                print("check_drawable_attr, error_drawable=", drawable_file_path, "error_attr=", android_attr_name,
                      "line in ", str(index + 1))
        drawable_f.close()

        if len(error_attr_tip_list):
            drawable_error_attr_dict[drawable_file_path] = error_attr_tip_list


def check_vector_size():
    vector_size_white_f = open(vector_size_white_list_path, "r")
    vector_size_white_text = vector_size_white_f.read()
    # print(vector_size_white_text)
    vector_size_white_f.close()

    for vector_drawable_file_path in vector_drawable_file_path_list:
        if os.path.basename(vector_drawable_file_path) in vector_size_white_text:
            continue

        vector_drawable_f = open(vector_drawable_file_path, "r")
        lines = vector_drawable_f.readlines()
        warning_size_tip_list = []

        for index, line in enumerate(lines):
            line = line.replace(' ', '')

            if "android:width=" in line:
                width_re = re.search(r'android:width=\"(.*?)dp\"', line)
                if width_re is not None:
                    width = width_re.group(1)
                    if float(width) > 200:
                        warning_size_tip_list.append("width=" + width)

            if "android:height=" in line:
                height_re = re.search(r'android:height=\"(.*?)dp\"', line)
                if height_re is not None:
                    height = height_re.group(1)
                    if float(height) > 200:
                        warning_size_tip_list.append("height=" + height)

        vector_drawable_f.close()
        if len(warning_size_tip_list) > 0:
            print("check_vector_size, warning vector=" + vector_drawable_file_path,
                  "warningInfo=", warning_size_tip_list)
            vector_warning_size_dict[vector_drawable_file_path] = warning_size_tip_list


get_module_path_list(lib_root_path)
get_module_path_list(app_src_main_res_path)
get_module_path_list(app_src_cn_res_path)
get_all_drawable_file_path()
get_all_layout_file_path()

check_svg_background()
print("check_svg_background end")

check_drawable_attr()
print("check_drawable_attr end")

check_vector_size()
print("check_vector_size end")

need_interrupt = False
if len(layout_error_bg_dict) > 0:
    need_interrupt = True
    print("Cannot reference svg res in android:background")
if len(drawable_error_attr_dict) > 0:
    need_interrupt = True
    print("Cannot reference attr in drawable res")
if len(vector_warning_size_dict) > 0:
    # need_interrupt = True
    print("Svg size cannot over 200dpx200dp")

print("check_svg_background_drawable_attr_vector_size.py end")
if need_interrupt:
    raise Exception("check_svg_background_drawable_attr_vector_size.py error")
