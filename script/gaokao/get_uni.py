# -*- coding: utf-8 -*-
import csv

csv_file = open("2018-GH-ST-First-batch.csv", "r")
reader = csv.reader(csv_file)

for item in reader:
    if reader.line_num == 1:
        continue

    lowest_score_str = item[7]
    ranking_str = item[8]
    if lowest_score_str == '':
        continue

    lowest_score = int(lowest_score_str)
    ranking = int(ranking_str)

    # print(lowest_score, ranking)
    if 500 <= lowest_score <= 600 and 6000 <= ranking <= 14000:
        print(item)
