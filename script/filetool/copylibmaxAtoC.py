#!usr/bin/python

import os
import re
import sys
import json
import shutil

ROOT_DIR = ''

A_LM_DIR = ROOT_DIR + '/app/libMax/java'
C_LM_DIR = ROOT_DIR + '/libs/ihs/libMax'

def getAppLibmaxChangedFilePathList(target):
    filePathList = []
    for parent, dirnames, filenames in os.walk(ROOT_DIR + '/app/libMax/' + target + '/java'):
        for filename in filenames:
            path = os.path.join(parent, filename)
            filePathList.append(path)

    return filePathList


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
    changeTarget = ''
    changeFileList = []
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
                changeFileList = fileList

    if (changeTarget == ''):
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
