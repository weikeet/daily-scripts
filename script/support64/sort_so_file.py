# -*- coding: utf-8 -*-

import os
import csv
import json

def print_so_item(pages):
    with open(pages, 'r') as f:
        so_row = []
        line_values = f.readlines()
        for v in line_values:
            sos = v.split('/')
            #print(sos)
            if len(sos) < 3:
                continue
            so_row.append(sos[2].replace('\n', ''))
        
        so_row.sort()
        for so in so_row:
            print(so)


# print('arm64-v8a')
# print_so_item('arm64-v8a_so.md')
# print('  ')
# print('armabi-v7a')
# print_so_item('armabi-v7a_so.md')
# print('  ')
# print('armabi')
# print_so_item('armabi_so.md')


# print('  ')
# print('space03_arm64-v8a')
# print_so_item('space03_arm64-v8a.md')
# print('  ')
# print('space03_armeabi-v7a')
# print_so_item('space03_armeabi-v7a.md')
# print('  ')
# print('space03_armeabi')
# print_so_item('space03_armeabi.md')


print('  ')
print('app-space10-arm64-v8a-debug-1222')
print_so_item('app-space10-arm64-v8a-debug-1222.md')
print('  ')
print('app-space10-armeabi-v7a-debug-1222')
print_so_item('app-space10-armeabi-v7a-debug-1222.md')
