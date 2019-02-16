#!usr/bin/python

import os
import re
import sys
import json

ROOT_DIR = sys.argv[1]
FILE_PATH = sys.argv[2]

A_LM_DIR = ROOT_DIR + '/app/libMax/java'
B_APP_DIR = ROOT_DIR + '/app/src/main/java'
C_LM_DIR = ROOT_DIR + '/libs/ihs/libMax'

LM_HEAD_PATH = '.git/modules/libs/ihs/libMax/HEAD'
LM_SHA1_REFS_DIR = '.git/modules/libs/ihs/libMax'

REFS_PATTERN = re.compile(r'refs/\S+')

SOURCES_FILE_PATH = 'app/libMax/config/sources_path.text'
LM_SHA1_FILE_PATH = 'app/libMax/config/libmax_head.text'


INVALID_DIRS_FOR_SOURCE = [A_LM_DIR + '/com/optimizer/test/module']

def getBAppDir(target):
    return ROOT_DIR + '/app/src/' + target + '/java'

def getCLibmaxPathFromA(apath):
    sourcesFile = open(SOURCES_FILE_PATH, 'r')
    jsonString = sourcesFile.readline()
    sourcesFile.close()

    sourcesMap = json.loads(jsonString)

    if os.path.isfile(apath):
        if not apath in sourcesMap.keys():
            print 'fail, not find file, path = ' + apath
            return

        index = apath.rfind('/') + 1
        return sourcesMap[apath] + apath[index:]
    else:
        for f in os.listdir(apath):
            subpath = os.path.join(apath, f)
            if not os.path.isfile(subpath):
                continue
            if subpath in sourcesMap.keys():
                index = subpath.rfind('/') + 1
                return os.path.dirname(sourcesMap[subpath] + subpath[index:])


def getCLibmaxPathFromB(bpath, targets, bAppDir):
    sourcesFile = open(SOURCES_FILE_PATH, 'r')
    jsonString = sourcesFile.readline()
    sourcesFile.close()

    sourcesMap = json.loads(jsonString)

    basename = ""
    bdir = bpath
    if os.path.isfile(bpath):
        bdir = os.path.dirname(bpath)
        basename = '/' + os.path.basename(bpath)

    for path in sourcesMap.keys():
        index = path.rfind(r'/')
        if index == -1:
            continue

        for target in targets:
            if ROOT_DIR + '/app/libMax/' + target + '/java' + bdir[len(bAppDir):] == path[:index]:
                clibmaxdir = sourcesMap[path]
                return clibmaxdir[:len(clibmaxdir) - 1] + basename

    sourcePath = ''
    while bdir:
        for path in sourcesMap.keys():
            for target in targets:
                if path.find(ROOT_DIR + '/app/libMax/' + target + '/java' + bdir[len(bAppDir):]) != -1:
                    sourcePath = sourcesMap[path]
                    break
            if sourcePath:
                break
        if sourcePath:
            break
        bdir = os.path.dirname(bdir)

    if not sourcePath:
        return
    for target in targets:
        if [ROOT_DIR + '/app/libMax/' + target + '/java/com/optimizer/test/module'].count(ROOT_DIR + '/app/libMax/' + target + '/java' + bdir[len(bAppDir):]):
            return

    index = sourcePath.find('/', len(C_LM_DIR) + 1)
    return sourcePath[:index] + '/java' + bpath[len(bAppDir):]


def function():
    print "Select path: " + FILE_PATH

    targets = [];

    for target in os.listdir('app/libMax'):
        if target == 'config' :
            continue
        else:
            targets.append(target)
            if FILE_PATH[:len(ROOT_DIR + '/app/libMax/' + target + '/java')] == ROOT_DIR + '/app/libMax/' + target + '/java':
                clibmaxpath = getCLibmaxPathFromA(FILE_PATH)
                print "C Libmax path: " + clibmaxpath
                os.system("studio diff " + FILE_PATH + " " + clibmaxpath)
                return

    isBFile = False;
    for target in os.listdir('app/src'):
        bAppDir = ROOT_DIR + '/app/src/' + target + '/java'
        if FILE_PATH[:len(bAppDir)] == bAppDir:
            isBFile = True
            clibmaxpath = ''
            if target == 'main' :
                clibmaxpath = getCLibmaxPathFromB(FILE_PATH, targets, bAppDir)
            else:
                clibmaxpath = getCLibmaxPathFromB(FILE_PATH, [target], bAppDir)
            print "C Libmax path: " + clibmaxpath
            if os.path.exists(clibmaxpath):
                os.system("studio diff " + FILE_PATH + " " + clibmaxpath)
            else:
                print "C Libmax path not exists"

    if not isBFile:
        print 'please select valid file or dir(libmax A or B)'


function()
