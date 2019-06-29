# -*- coding: utf-8 -*-
import csv

list_985 = []
list_first_class_a = []
list_first_class_b = []

with open('985_university_list.txt', 'r') as file_985:
    list_985_lines = file_985.readlines()
    for l in list_985_lines:
        list_985.append(l.replace('\n', ''))
print(list_985)


with open('first_class_university_list.txt', 'r') as file_first_class:
    list_first_class_lines = file_first_class.readlines()

    type = 'A类'
    for l in list_first_class_lines:
        l = l.replace('\n', '')
        if l == '':
            continue
        if 'A类' in l:
            type = 'A类'
            continue
        if 'B类' in l:
            type = 'B类'
            continue
        if l.endswith('大学'):
            if type == 'A类':
                list_first_class_a.append(l)
            elif type == 'B类':
                list_first_class_b.append(l)
print(list_first_class_a)
print(list_first_class_b)

for aa in list_985:
    if aa in list_first_class_a or aa in list_first_class_b:
        pass
    else:
        print('diff', aa)

for bb in list_first_class_a:
    if bb in list_985:
        pass
    else:
        print('diff a', bb)

for cc in list_first_class_b:
    if cc in list_985:
        pass
    else:
        print('diff b', cc)

csv_file = open("2018-GH-ST-First-batch.csv", "r")
reader = csv.reader(csv_file)

for item in reader:
    if reader.line_num == 1:
        continue

    lowest_score_str = item[7]
    ranking_str = item[8]
    university_name = item[2]
    if lowest_score_str == '':
        continue

    lowest_score = int(lowest_score_str)
    ranking = int(ranking_str)

    # print(lowest_score, ranking)
    if 500 <= lowest_score <= 600 and 6000 <= ranking <= 14000:
        # print(item)
        if university_name in list_985:
            print('985:', item)
        if university_name in list_first_class_a:
            print('A类双一流:', item)
        elif university_name in list_first_class_b:
            print('B类双一流:', item)
