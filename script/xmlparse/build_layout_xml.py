#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

moduleName = 'swalltest'
rootPath = os.path.abspath('')
resPath = rootPath + '/' + moduleName + '/src/main/res'


def build_layout_xml(xml_name, start, end):
    xmlData = '<?xml version="1.0" encoding="utf-8"?>' \
              '\n<FrameLayout' \
              '\n  xmlns:android="http://schemas.android.com/apk/res/android"' \
              '\n  android:layout_width="match_parent"' \
              '\n  android:layout_height="match_parent">'

    while start < end:
        row = '\n\n  <View' \
              '\n    android:layout_width="%ddp"' \
              '\n    android:layout_height="%ddp"' \
              '\n    android:background="@color/colorAccent" />' % (start, start + 1)
        xmlData = xmlData + row
        start = start + 2
    xmlData = xmlData + '\n</FrameLayout>'

    xmlPath = resPath + '/layout/'
    isExists = os.path.exists(xmlPath)
    if not isExists:
        os.makedirs(xmlPath)

    file = open(xmlPath + xml_name, "w")
    file.write(xmlData)
    file.close()

    print('build layout xml finished')


def build_sw_layout_xml(xml_name, start, end):
    xmlData = '<?xml version="1.0" encoding="utf-8"?>' \
              '\n<FrameLayout' \
              '\n  xmlns:android="http://schemas.android.com/apk/res/android"' \
              '\n  android:layout_width="match_parent"' \
              '\n  android:layout_height="match_parent">'

    while start < end:
        row = '\n\n  <View' \
              '\n    android:layout_width="@dimen/dp_%d"' \
              '\n    android:layout_height="@dimen/dp_%d"' \
              '\n    android:background="@color/colorAccent" />' % (start, start + 1)
        xmlData = xmlData + row
        start = start + 2
    xmlData = xmlData + '\n</FrameLayout>'

    xmlPath = resPath + '/layout/'
    isExists = os.path.exists(xmlPath)
    if not isExists:
        os.makedirs(xmlPath)

    file = open(xmlPath + xml_name, "w")
    file.write(xmlData)
    file.close()

    print('build layout xml finished')


if __name__ == '__main__':
    build_layout_xml('activity_001_080.xml', 1, 80)
    build_layout_xml('activity_081_160.xml', 81, 160)
    build_layout_xml('activity_161_240.xml', 161, 240)

    build_sw_layout_xml('activity_sw_001_080.xml', 1, 80)
    build_sw_layout_xml('activity_sw_081_160.xml', 81, 160)
    build_sw_layout_xml('activity_sw_161_240.xml', 161, 240)
