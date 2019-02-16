#!usr/bin/python

import os
import re
import sys
import json
import shutil

ROOT_DIR = sys.argv[1]

A_LM_DIR = ROOT_DIR + '/app/libMax/java'
C_LM_DIR = ROOT_DIR + '/libs/ihs/libMax'

LM_HEAD_PATH = '.git/modules/libs/ihs/libMax/HEAD'
LM_SHA1_REFS_DIR = '.git/modules/libs/ihs/libMax'

REFS_PATTERN = re.compile(r'refs/\S+')

MODIFIED_FILE_PATH = 'app/libMax/config/modified.text'
SOURCES_FILE_PATH = 'app/libMax/config/sources_path.text'
LM_SHA1_FILE_PATH = 'app/libMax/config/libmax_head.text'

INVALID_DIRS_FOR_SOURCE = [A_LM_DIR + '/com/optimizer/test/module']


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


def getAppLibmaxChangedFilePathList(target):
    filePathList = []
    for parent, dirnames, filenames in os.walk(ROOT_DIR + '/app/libMax/' + target + '/java'):
        for filename in filenames:
            path = os.path.join(parent, filename)
            filePathList.append(path)

    configFile = open('app/libMax/' + target + '/config/modified.text', 'r')
    jsonString = configFile.readline()
    configFile.close()

    modifiedMap = json.loads(jsonString)

    changedFilePathList = []
    keys = modifiedMap.keys()
    for path in filePathList:
        if keys.count(path) == 0:
            changedFilePathList.append(path)
            continue

        diff = modifiedMap[path] - os.stat(path).st_mtime * 1000
        if -100 < diff < 100:
            continue

        changedFilePathList.append(path)

    return changedFilePathList


def evaluateSourcesDir(aPath, sourcesMap, target):
    DIR_NAME = os.path.dirname(aPath)

    dirName = DIR_NAME
    for path in sourcesMap.keys():
        index = path.rfind(r'/')
        if index == -1:
            continue
        if dirName == path[:index]:
            return sourcesMap[path]

    sourcePath = ''
    while dirName:
        for path in sourcesMap.keys():
            if path.find(dirName) != -1:
                sourcePath = sourcesMap[path]
                break
        if sourcePath:
            break
        dirName = os.path.dirname(dirName)

    if not sourcePath:
        return

    if [ROOT_DIR + '/app/libMax/' + target + '/java/com/optimizer/test/module'].count(dirName):
        return

    index = sourcePath.find('/', len(C_LM_DIR) + 1)
    return sourcePath[:index] + '/java' + DIR_NAME[len(ROOT_DIR + '/app/libMax/' + target + '/java'):] + '/'


def copyChangedFileToSubmodulesLibmax(changedFilePathList, target):
    copyFileDict = {}

    sourcesFile = open('app/libMax/config/sources_path.text', 'r')
    jsonString = sourcesFile.readline()
    sourcesFile.close()

    sourcesMap = json.loads(jsonString)
    keys = sourcesMap.keys()

    for path in changedFilePathList:
        if keys.count(path) == 0:
            sourcesDir = evaluateSourcesDir(path, sourcesMap, target)
            if not sourcesDir:
                continue

        else:
            sourcesDir = sourcesMap[path]

        if not os.path.exists(sourcesDir):
            try:
                os.makedirs(sourcesDir)
            except OSError:
                if not os.path.isdir(sourcesDir):
                    raise

        shutil.copy(path, sourcesDir)
        copyFileDict.setdefault(path, sourcesDir)

    return copyFileDict


def mergeLibmaxChangeFile():
    changeTarget = '';
    changeFileList = [];
    for target in os.listdir('app/libMax'):
        if target == 'config' :
            continue
        else:
            fileList = getAppLibmaxChangedFilePathList(target)
            if len(fileList) == 0:
                continue
            elif (changeTarget != ''):
                print 'More than one target changed, please delete useless target in A'
                return
            else:
                changeTarget = target
                changeFileList = fileList;

    if (changeTarget == ''):
        return

    submodulesLibmaxSHA1 = readSubmodulesLibmaxHeadSHA1()

    file = open(LM_SHA1_FILE_PATH, 'r')
    appLibmaxSHA1 = file.readline()
    file.close()

    print 'app libmax SHA-1: ' + appLibmaxSHA1
    print 'submodules libmax SHA-1: ' + submodulesLibmaxSHA1
    if appLibmaxSHA1 != submodulesLibmaxSHA1:
        print 'place check out ' + appLibmaxSHA1
        return

    copyFileDict = copyChangedFileToSubmodulesLibmax(changeFileList, changeTarget)

    appLibmaxLen = len(ROOT_DIR + '/app/libMax/' + changeTarget + '/java') + 1
    submodulesLen = len(C_LM_DIR) + 1

    print "#################### START CopyLibMax ####################"
    print 'app libmax -> submodules libmax'
    for appPath in copyFileDict.keys():
        print '|' + appPath[appLibmaxLen:] + '\n|--> ' + copyFileDict[appPath][submodulesLen:]

    failList = []
    for changePath in changeFileList:
        if not copyFileDict.has_key(changePath):
            failList.append(changePath)

    if len(failList) > 0:
        errorMsg = '\nfailure file list: '
        for path in failList:
            errorMsg += "\n" + path[appLibmaxLen:]
        print errorMsg

    print '\nchanged count = ' + str(len(changeFileList))
    print 'success count = ' + str(len(copyFileDict.keys()))
    print 'fail count    = ' + str(len(failList))

    print "#################### END CopyLibMax ####################"


mergeLibmaxChangeFile()
