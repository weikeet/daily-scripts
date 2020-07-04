# -*- coding: utf-8 -*-

insert_package_list = []

f = open("topgames.txt", "r")
lines = f.readlines()
for line in lines:
    a = '(\'' + line.replace('\n', '') + '\')'
    if a in insert_package_list:
        continue
    insert_package_list.append(a)
f.close()

pack_list = ''
for insert_package in insert_package_list:
    pack_list = pack_list + insert_package + ', '
print(pack_list)

db_inset_file = open('dbinset.txt', 'w+')
db_inset_file.write(pack_list)
db_inset_file.close()