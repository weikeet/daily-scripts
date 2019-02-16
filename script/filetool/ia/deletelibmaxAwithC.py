#!usr/bin/python

import os
import re
import sys
import json

ROOT_DIR = sys.argv[1]
FILE_PATH = sys.argv[2]

A_LM_DIR = ROOT_DIR + '/app/libMax/java'
C_LM_DIR = ROOT_DIR + '/libs/ihs/libMax'

LM_HEAD_PATH = '.git/modules/libs/ihs/libMax/HEAD'
LM_SHA1_REFS_DIR = '.git/modules/libs/ihs/libMax'

REFS_PATTERN = re.compile(r'refs/\S+')

SOURCES_FILE_PATH = 'app/libMax/config/sources_path.text'
LM_SHA1_FILE_PATH = 'app/libMax/config/libmax_head.text'


def readSubmodulesLibmaxHeadSHA1():
    headFile = open(LM_HEAD_PATH, 'r')
    headSHA1 = headFile.readline()
    headFile.close()

    match = REFS_PATTERN.search(headSHA1)

    if match:
        headFile2 = open(LM_SHA1_REFS_DIR + '/' + match.group(), 'r')
        headSHA1 = headFile2.readline()
        headFile2.close()

    return headSHA1[:40]


def deleteLibmaxFile(filePath):
    sourcesFile = open(SOURCES_FILE_PATH, 'r')
    jsonString = sourcesFile.readline()
    sourcesFile.close()

    sourcesMap = json.loads(jsonString)
    if not filePath in sourcesMap.keys():
        print 'fail, not find releate file'
        print 'path: ' + filePath
        return

    index = filePath.rfind('/') + 1
    releateFilePath = sourcesMap[filePath] + filePath[index:]
    os.remove(filePath)
    os.remove(releateFilePath)

    submodulesLen = len(C_LM_DIR) + 1
    print releateFilePath[submodulesLen:]


def autoDeleteLibmax():
    submodulesLibmaxSHA1 = readSubmodulesLibmaxHeadSHA1()

    file = open(LM_SHA1_FILE_PATH, 'r')
    appLibmaxSHA1 = file.readline()
    file.close()

    print 'app libmax SHA-1: ' + appLibmaxSHA1
    print 'submodules libmax SHA-1: ' + submodulesLibmaxSHA1
    if appLibmaxSHA1 != submodulesLibmaxSHA1:
        print 'place check out ' + appLibmaxSHA1
        return

    print '\ndelete:'
    print FILE_PATH

    isAFile = False
    for target in os.listdir('app/libMax'):
        if target == 'config' :
            continue
        else:
            if FILE_PATH[:len(ROOT_DIR + '/app/libMax/' + target + '/java')] == ROOT_DIR + '/app/libMax/' + target + '/java':
                isAFile = True
                if os.path.isfile(FILE_PATH):
                    deleteLibmaxFile(FILE_PATH)
                else:
                    filePathList = []
                    for parent, dirnames, filenames in os.walk(FILE_PATH):
                        for filename in filenames:
                            path = os.path.join(parent, filename)
                            filePathList.append(path)
                    for path in filePathList:
                        deleteLibmaxFile(path)
                    try:
                        os.rmdir(FILE_PATH)
                    except OSError:
                        if not os.path.exists(FILE_PATH):
                            raise
    if not isAFile:
        print '\nplace delete app libmax file'


autoDeleteLibmax()
