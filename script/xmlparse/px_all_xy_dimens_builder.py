#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from xml.dom.minidom import parse
import xml.dom.minidom

basePx = [1280, 720]
dimenTypes = {800: 480, 960: 540, 1920: 1080, 2280: 1080, 2560: 1440, 2960: 1440}

moduleName = 'pxalltest'
rootPath = os.path.abspath('')
resPath = rootPath + '/' + moduleName + '/src/main/res'


def write_xml_data(height, width, dimen_data):
    xmlData = '<?xml version="1.0" encoding="utf-8"?>\n<resources>'
    for key, value in dimen_data.items():
        temp = int(value.replace('px', ''))
        if 'x' in key:
            dimenValue = '%.4f' % (temp * width / basePx[1])
        else:
            dimenValue = '%.4f' % (temp * height / basePx[0])
        row = '\n    <dimen name="%s">%spx</dimen>' % (key, dimenValue)
        xmlData = xmlData + row
    xmlData = xmlData + '\n</resources>'

    xmlPath = resPath + '/values-%1dx%2d' % (height, width)
    isExists = os.path.exists(xmlPath)
    if not isExists:
        os.makedirs(xmlPath)

    file = open(xmlPath + '/dimens.xml', "w")
    file.write(xmlData)
    file.close()


def generate_default_dimens():
    xmlXData = '<?xml version="1.0" encoding="utf-8"?>\n<resources>'
    dimenXValue = 1
    while dimenXValue <= basePx[1]:
        row = '\n    <dimen name="%s">%spx</dimen>' % ('x%d' % dimenXValue, dimenXValue)
        xmlXData = xmlXData + row
        dimenXValue = dimenXValue + 1
    xmlXData = xmlXData + '\n</resources>'

    xmlXPath = resPath + '/values'
    isExists = os.path.exists(xmlXPath)
    if not isExists:
        os.makedirs(xmlXPath)

    file = open(xmlXPath + '/lay_x.xml', "w")
    file.write(xmlXData)
    file.close()

    xmlYData = '<?xml version="1.0" encoding="utf-8"?>\n<resources>'
    dimenYValue = 1
    while dimenYValue <= basePx[0]:
        row = '\n    <dimen name="%s">%spx</dimen>' % ('y%d' % dimenYValue, dimenYValue)
        xmlYData = xmlYData + row
        dimenYValue = dimenYValue + 1
    xmlYData = xmlYData + '\n</resources>'

    xmlYPath = resPath + '/values'
    isExists = os.path.exists(xmlYPath)
    if not isExists:
        os.makedirs(xmlYPath)

    file = open(xmlYPath + '/lay_y.xml', "w")
    file.write(xmlYData)
    file.close()

    print('generate default dimens finished')


if __name__ == '__main__':
    generate_default_dimens()

    root = xml.dom.minidom.parse(resPath + '/values/dimens.xml').documentElement
    dimens = root.getElementsByTagName('dimen')

    dimenData = {}
    for dimen in dimens:
        dimenData[dimen.getAttribute('name')] = dimen.firstChild.data

    for height, width in dimenTypes.items():
        write_xml_data(height, width, dimenData)
