# -*- coding: utf-8 -*-

import requests

num_list = range(243810, 243847 + 1)
index = 1
for num in num_list:
    comment_url = 'https://comment.bilibili.com/' + str(num) + '.xml'
    comment_data = requests.get(comment_url)
    with open('仙剑奇侠传三_' + str(index) + '.xml', 'wb') as f:
        f.write(comment_data.content)
        index = index + 1
