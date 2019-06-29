# -*- coding: utf-8 -*-
import csv

list_985 = []

with open('985_university_list.txt', 'r') as file_985:
    list_985_lines = file_985.readlines()
    for l in list_985_lines:
        list_985.append(l.replace('\n', ''))
print(list_985)

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
    if university_name in list_985:
        print(item)
