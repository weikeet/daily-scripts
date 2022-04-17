# -*- coding: utf-8 -*-
import json
import os

import requests

pixiv_image_folder = 'E:\\Pixiv\\10127539_月水月'

names = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isfile(os.path.join(pixiv_image_folder, name))]

print("xx", len(names))
for file_name in names:
    print(file_name)
