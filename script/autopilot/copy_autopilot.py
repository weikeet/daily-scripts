# -*- coding: utf-8 -*-
import os
import shutil

base_path = "/Users/weicools/test/"
base_origin_path = "/Volumes/Common/Projects/PyCharmProjects/awesome-script/script/autopilot/origin/"

autopilot = base_path + "autopilot"
autopilotfuck = base_path + "autopilotfuck"

origin_autopilot = base_origin_path + "autopilot"
origin_autopilotfuck = base_origin_path + "autopilotfuck"

if os.path.exists(autopilot):
    shutil.rmtree(autopilot)

target_path = autopilotfuck
source_path = origin_autopilotfuck

if not os.path.exists(target_path):
    os.makedirs(target_path)

if os.path.exists(source_path):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(source_path):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, target_path)
            print(src_file)
