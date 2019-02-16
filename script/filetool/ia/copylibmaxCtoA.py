#!usr/bin/python
# -*- coding:utf-8 -*-
import os
import re
import sys
import json
import shutil
import time

ROOT_DIR = sys.argv[1]

LIBMAX_A_DIR = ROOT_DIR + '/app/libMax/java'
LIBMAX_C_DIR = ROOT_DIR + '/libs/ihs/libMax'

LIBMAX_C_HEAD_PATH = '.git/modules/libs/ihs/libMax/HEAD'
LIBMAX_C_REFS_DIR = '.git/modules/libs/ihs/libMax'

MODIFIED_FILE_PATH = 'app/libMax/config/modified.text'
SOURCES_FILE_PATH = 'app/libMax/config/sources_path.text'
LIBMAX_A_SHA1_FILE_PATH = 'app/libMax/config/libmax_head.text'

LIBMAX_CONFIG_FILE_PATH = 'app/libmaxconfig.json'

REFS_PATTERN = re.compile(r'refs/\S+')
LIBMAX_GRADLE_CONFIG_PATTERN = re.compile(r'deflibMaxClassConfig=\[((\w|\'|,)*)\]')


def getLibmaxcSHA1():
    libmaxcHeadFile = open(LIBMAX_C_HEAD_PATH, 'r')
    sha1 = libmaxcHeadFile.readline()
    libmaxcHeadFile.close()

    match = REFS_PATTERN.search(sha1)

    if match:
        libmaxcHeadFile = open(LIBMAX_C_REFS_DIR + '/' + match.group(), 'r')
        sha1 = libmaxcHeadFile.readline()
        libmaxcHeadFile.close()

    return sha1[:40]


def getLibmaxConfigList(target):
    if os.path.exists('app/src/' + target + '/libmaxconfig.json'):
        content = ""
        file = open('app/src/' + target + '/libmaxconfig.json', "r")
        for line in file.readlines():
            content += re.sub('\s', "", line)
        file.close()

        return json.loads(content)
    else:  # GradleCtoA使用python推广后需要删除
        content = ""
        file = open('app/build.gradle', "r")
        for line in file.readlines():
            content += re.sub('\s', "", line)
        file.close()

        match = LIBMAX_GRADLE_CONFIG_PATTERN.search(content)
        moduleList = re.sub('\'', "", match.group(1)).split(',')

        configList = []
        for module in moduleList:
            map = {"module_name": module,
                   "java_code_file": {"include": [], "exclude": []}}
            configList.append(map)

        return configList


def getLibmaxaChangedFilePathList(target):
    addedFilePathList = []
    removedFilePathList = []
    changedFilePathList = []

    libmaxaFilePathList = []
    for parent, dirnames, filenames in os.walk(ROOT_DIR + '/app/libMax/' + target + '/java'):
        for filename in filenames:
            path = os.path.join(parent, filename)
            libmaxaFilePathList.append(path)

    if not os.path.exists('app/libMax/' + target + '/config/modified.text'):
        return libmaxaFilePathList, removedFilePathList, changedFilePathList

    modifiedFile = open('app/libMax/' + target + '/config/modified.text', 'r')
    jsonString = modifiedFile.readline()
    modifiedFile.close()

    modifiedMap = json.loads(jsonString)
    configFilePathList = modifiedMap.keys()
    configFilePathList.remove('time')

    for path in libmaxaFilePathList:
        if configFilePathList.count(path) == 0:
            addedFilePathList.append(path)
            continue

        diff = modifiedMap[path] - os.stat(path).st_mtime * 1000
        if -100 < diff < 100:
            continue

        changedFilePathList.append(path)

    for path in configFilePathList:
        if libmaxaFilePathList.count(path) == 0:
            removedFilePathList.append(path)

    return addedFilePathList, removedFilePathList, changedFilePathList


def main():
    print "\n#################### START CopyLibMax C to A ####################"
    startTime = time.time()

    libmaxcSHA1 = getLibmaxcSHA1()
    print 'LibmaxC SHA-1: ' + libmaxcSHA1

    if not os.path.exists('app/libMax/config'):
        try:
            os.makedirs('app/libMax/config')
        except OSError:
            if not os.path.isdir('app/libMax/config'):
                raise

    for target in os.listdir('app/src'):
        if target == 'main':
            continue
        else:
            hasChangedFile = checkChangeFile(target)
            if hasChangedFile:
                print '\nPlease process change file'
                print '\nExcute time = ' + str(time.time() - startTime) + ' ms'
                print "#################### END CopyLibMax C to A ####################"
                return

    sourcePathMap = {'sources': ROOT_DIR + '/app/libMax/config/'}

    for target in os.listdir('app/src'):
        if os.path.isdir('app/src/' + target) and os.path.exists('app/src/' + target + '/libmaxconfig.json'):
            sourcePathMap = copyTargetLibMax(target, sourcePathMap)

    libmaxshaFile = open(LIBMAX_A_SHA1_FILE_PATH, 'w+')
    libmaxshaFile.write(libmaxcSHA1)
    libmaxshaFile.close()

    sourcePathMapFile = open(SOURCES_FILE_PATH, 'w+')
    sourcePathMapFile.write(json.dumps(sourcePathMap))
    sourcePathMapFile.close()

    print '\nCopy Success, Excute time = ' + str(time.time() - startTime) + ' ms'
    print "#################### END CopyLibMax C to A ####################"

def checkChangeFile(target):
    addedFilePathList, removedFilePathList, changeFilePathList = getLibmaxaChangedFilePathList(target)

    libmaxaPathPreLen = len(ROOT_DIR) + 1
    hasChangedFile = False

    if addedFilePathList and len(addedFilePathList) > 0:
        hasChangedFile = True
        print '\nLibmaxA added ' + str(len(addedFilePathList)) + ' files: '
        for path in addedFilePathList:
            print '|_ ' + path[libmaxaPathPreLen:]

    if removedFilePathList and len(removedFilePathList) > 0:
        hasChangedFile = True
        print '\nLibmaxA removed ' + str(len(removedFilePathList)) + ' files: '
        for path in removedFilePathList:
            print '|_ ' + path[libmaxaPathPreLen:]

    if changeFilePathList and len(changeFilePathList) > 0:
        hasChangedFile = True
        print '\nLibmaxA changed ' + str(len(changeFilePathList)) + ' files: '
        for path in changeFilePathList:
            print '|_ ' + path[libmaxaPathPreLen:]

    return hasChangedFile;


def copyTargetLibMax(target, sourcePathMap):
    print
    print '>>>>>>>>>>>>>>>>start copy ' + target

    if os.path.exists('app/libMax/' + target):
        shutil.rmtree('app/libMax/' + target)

    overrideFilePathList = []

    for configMap in getLibmaxConfigList(target):
        # 处理 java 文件
        srcModuleRootDir = 'libs/ihs/libMax/' + configMap["module_name"] + '/java'
        preLength = len(srcModuleRootDir) + 1

        for parent, dirnames, filenames in os.walk(srcModuleRootDir):
            for filename in filenames:
                if filename == '.DS_Store':
                    continue

                path = os.path.join(parent, filename)

                if configMap.has_key("java_code_file"):
                    if configMap["java_code_file"].has_key("include"):
                        includeList = configMap["java_code_file"]["include"]
                        if len(includeList) > 0:
                            iscontain = False
                            packagePath = re.sub('/', ".", path[preLength:])
                            for filepath in includeList:
                                if packagePath.find(filepath) == 0:
                                    iscontain = True
                                    break

                            if not iscontain:
                                continue

                    if configMap["java_code_file"].has_key("exclude"):
                        excludeList = configMap["java_code_file"]["exclude"]
                        if len(excludeList) > 0:
                            iscontain = False
                            packagePath = re.sub('/', ".", path[preLength:])
                            for filepath in excludeList:
                                if packagePath.find(filepath) == 0:
                                    iscontain = True
                                    break

                            if iscontain:
                                continue

                if os.path.exists('app/src/main/java/' + path[preLength:]) or os.path.exists('app/src/' + target + '/java/' + path[preLength:]):
                    noteMap = {}
                    noteMap["filename"] = filename
                    noteMap["package"] = parent[preLength:]
                    noteMap["modulename"] = configMap["module_name"]
                    overrideFilePathList.append(noteMap)
                    continue

                srcPath = ROOT_DIR + '/' + path
                desPath = ROOT_DIR + '/app/libMax/' + target + '/java' + '/' + path[preLength:]

                srcDir = ROOT_DIR + '/' + parent + '/'
                desDir = ROOT_DIR + '/app/libMax/' + target + '/java' + '/' + parent[preLength:] + '/'

                if not os.path.exists(desDir):
                    try:
                        os.makedirs(desDir)
                    except OSError:
                        if not os.path.isdir(desDir):
                            raise

                shutil.copy(srcPath, desDir)
                sourcePathMap[desPath] = srcDir

    # 添加或更新 libmax config
    if not os.path.exists('app/libMax/' + target + '/config'):
        try:
            os.makedirs('app/libMax/' + target + '/config')
        except OSError:
            if not os.path.isdir('app/libMax/' + target + '/config'):
                raise

    modifiedTimeMap = {'time': time.time()}
    for parent, dirnames, filenames in os.walk('app/libMax/' + target + '/java'):
        for filename in filenames:
            path = os.path.join(parent, filename)
            modifiedTimeMap[ROOT_DIR + "/" + path] = int(os.stat(path).st_mtime * 1000)

    modifiedTImeMapFile = open('app/libMax/' + target + '/config/modified.text', 'w+')
    modifiedTImeMapFile.write(json.dumps(modifiedTimeMap))
    modifiedTImeMapFile.close()

    overrideInfoFile = open('app/libMax/' + target + '/config/libmax_override_info.json', 'w+')
    overrideInfoFile.write(json.dumps(overrideFilePathList))
    overrideInfoFile.close()

    return sourcePathMap


main()
# 运行autopilot脚本
os.system("python " + ROOT_DIR + "/libs/ihs/libMax/iatools/autopilothelper/parseAutopilot.py " + ROOT_DIR)
