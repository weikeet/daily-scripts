# -*- coding: utf-8 -*-
import os
import sys
import shutil

fixed = "fixed"
unfixed = "unfixed"

projects = "/Users/weicools/Projects/"
appcloudbox = "/app/src/main/java/net/appcloudbox/"

am = projects + "Enerjoy/app_ambercn_android" + appcloudbox
fc = projects + "Enerjoy/app_fastclearcn_android" + appcloudbox
sp = projects + "Enerjoy/app_maxcleanercn_android" + appcloudbox
op = projects + "Enerjoy/app_maxcn_android" + appcloudbox
pp = projects + "Enerjoy/app_maxsecuritycn_android" + appcloudbox
wk = projects + "Enerjoy/app_walkcn_android" + appcloudbox

source_common = "/Users/weicools/Projects/PyCharm/awesome-script/script/autopilot/origin/"
source_autopilot = source_common + "autopilot"
source_autopilotfuck = source_common + "autopilotfuck"

if len(sys.argv) == 3:
    options = sys.argv[1]
    product = sys.argv[2]

    print(options, product)

    if product == "am":
        app_project = am
    elif product == "fc":
        app_project = fc
    elif product == "sp":
        app_project = sp
    elif product == "op":
        app_project = op
    elif product == "pp":
        app_project = pp
    else:
        app_project = wk

    if options == fixed:
        source_path = source_autopilot
        target_path = app_project + "autopilot"
        delete_path = app_project + "autopilotfuck"
    else:
        source_path = source_autopilotfuck
        target_path = app_project + "autopilotfuck"
        delete_path = app_project + "autopilot"

    if os.path.exists(delete_path):
        shutil.rmtree(delete_path)

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for fff in files:
                src_file = os.path.join(root, fff)
                shutil.copy(src_file, target_path)
                print(src_file)
