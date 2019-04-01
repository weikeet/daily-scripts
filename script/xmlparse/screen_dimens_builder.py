#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from xml.dom.minidom import parse
import xml.dom.minidom

baseDp = 360
dimenTypes = [300, 320, 360, 384, 392, 411, 440, 480, 533, 592, 640]

moduleName = 'app'
rootPath = os.path.abspath('')
resPath = rootPath + '/' + moduleName + '/src/main/res'


def writeXmlData(dimenType, dimenData):
    xmlData = '<?xml version="1.0" encoding="utf-8"?>\n<resources>'
    for key, value in dimenData.items():
        temp = int(value.replace('dp', ''))
        dimenValue = '%.4f' % (temp * dimenType / baseDp)
        row = '\n    <dimen name="%s">%sdp</dimen>' % (key, dimenValue)
        xmlData = xmlData + row
    xmlData = xmlData + '\n</resources>'

    xmlPath = resPath + '/values-sw%ddp' % dimenType
    isExists = os.path.exists(xmlPath)
    if not isExists:
        os.makedirs(xmlPath)

    file = open(xmlPath + '/dimens.xml', "w")
    file.write(xmlData)
    file.close()


if __name__ == '__main__':
    root = xml.dom.minidom.parse(resPath + '/values/dimens.xml').documentElement
    dimens = root.getElementsByTagName('dimen')

    dimenData = {}
    for dimen in dimens:
        dimenData[dimen.getAttribute('name')] = dimen.firstChild.data

    # for key, value in dimenData.items():
    #     print('name: %s, value: %s' % (key, value))

    for dimenType in dimenTypes:
        writeXmlData(dimenType, dimenData)
