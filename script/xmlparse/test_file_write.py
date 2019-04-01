#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

baseDp = 360

print('/values-sw%ddp'%12)
print(os.path.abspath('/app/res'))
# print(os.path.)

print(str(720/baseDp))
print('%.4f' %(360/720))

tt = '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <dimen name="dp_1">1dp</dimen>\n    <dimen name="dp_16">16dp</dimen>\n</resources>'
file = open('tt.xml', "w")
file.write(tt)
file.close()