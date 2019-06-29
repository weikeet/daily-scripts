# -*- coding: utf-8 -*-
import csv

list_985 = []
list_first_class_a = []
list_first_class_b = []

list_211 = []
list_211_ex985 = []

with open('985_university_list.txt', 'r') as file_985:
    list_985_lines = file_985.readlines()
    for l in list_985_lines:
        list_985.append(l.replace('\n', ''))
# print(list_985)

with open('first_class_university_list.txt', 'r') as file_first_class:
    list_first_class_lines = file_first_class.readlines()

    type = 'A类'
    for lfc in list_first_class_lines:
        lfc = lfc.replace('\n', '')
        if lfc == '':
            continue
        if 'A类' in lfc:
            type = 'A类'
            continue
        if 'B类' in lfc:
            type = 'B类'
            continue
        if lfc.endswith('大学'):
            if type == 'A类':
                list_first_class_a.append(lfc)
            elif type == 'B类':
                list_first_class_b.append(lfc)
# print(list_first_class_a)
# print(list_first_class_b)
# for aa in list_985:
#     if aa in list_first_class_a or aa in list_first_class_b:
#         pass
#     else:
#         print('diff', aa)
#
# for bb in list_first_class_a:
#     if bb in list_985:
#         pass
#     else:
#         print('diff a', bb)
#
# for cc in list_first_class_b:
#     if cc in list_985:
#         pass
#     else:
#         print('diff b', cc)

u211_file = open("211_university_list.csv", "r")
reader_211 = csv.reader(u211_file)

for item in reader_211:
    if reader_211.line_num == 1:
        continue
    name_211 = item[0]
    list_211.append(name_211)
    if name_211 not in list_985:
        list_211_ex985.append(name_211)
# print(list_211_ex985)

sel_985_and_a = []
sel_985_and_b = []
sel_b = []
sel_211 = []
total_count = 0

csv_file = open("2018-GZ-First-batch.csv", "r")
reader = csv.reader(csv_file)
for item in reader:
    if reader.line_num == 1:
        print(item)
        continue
    total_count = total_count + int(item[4])

    lowest_score_str = item[7]
    ranking_str = item[8]
    university_name = item[2]
    if lowest_score_str == '':
        continue

    lowest_score = int(lowest_score_str)
    ranking = int(ranking_str)

    # print(lowest_score, ranking)
    if 500 <= lowest_score <= 600 and 4000 <= ranking <= 14000:
        if university_name in list_985 and university_name in list_first_class_a:
            sel_985_and_a.append(item)
        elif university_name in list_985 and university_name in list_first_class_b:
            sel_985_and_b.append(item)
        elif university_name in list_first_class_b:
            sel_b.append(item)

    if lowest_score <= 600 and university_name in list_211_ex985 and item[3] == '普通类':
        sel_211.append(item)

print('total:', total_count)
print('--------------------------------985 和 A类双一流--------------------------------')
for item_985_a in sel_985_and_a:
    print('985 和 A类双一流:', item_985_a)
print('--------------------------------985 和 B类双一流--------------------------------')
for item_985_b in sel_985_and_b:
    print('985 和 B类双一流:', item_985_b)
print('------------------------------------B类双一流------------------------------------')
for item_b in sel_b:
    print('B类双一流:', item_b)
print('---------------------------------------211---------------------------------------')
for item_211 in sel_211:
    print('211:', item_211)

