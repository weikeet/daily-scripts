#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import time
import logging
import filecmp
#日志文件配置
log_filename ='synchro.log'
#日志输出格式化
log_format = '%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG) 
#日志输出到日志文件
fileLogger = logging.getLogger('fileLogger')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fileLogger.addHandler(fh);
#需要同步的文件夹路径,可以使用绝对路径,也可以使用相对路径
synchroPath1 = r'/Users/zhengwei.zhang/ProjectSpace/WebStorm/awesome-script/script'
synchroPath2 = r'/Users/zhengwei.zhang/Documents/script'

#同步方法
def synchro(synchroPath1,synchroPath2):
        leftDiffList = filecmp.dircmp(synchroPath1,synchroPath2).left_only
        rightDiffList = filecmp.dircmp(synchroPath1,synchroPath2).right_only
        commondirsList =filecmp.dircmp(synchroPath1,synchroPath2).common_dirs
        for item in leftDiffList:
                copyPath = synchroPath1 + '/' + item
                pastePath = synchroPath2 + '/' + item
                if(os.path.isdir(copyPath)):
                        copyDir(copyPath,pastePath)
                else :
                        shutil.copy2(copyPath,pastePath)
                        fileLogger.info('copy '+copyPath +" to "+pastePath)
        for item in rightDiffList:
                copyPath = synchroPath2 + '/' + item
                pastePath = synchroPath1 +'/' + item
                if(os.path.isdir(copyPath)):
                        copyDir(copyPath,pastePath)
                else :
                        shutil.copy2(copyPath,pastePath)
                        fileLogger.info('copy '+copyPath +" to "+pastePath)
        for item in commondirsList:
                copyPath = synchroPath2 + '/' + item
                pastePath = synchroPath1 +'/' + item
                syncDir(copyPath,pastePath)
#拷贝文件夹,如果文件夹不存在创建之后直接拷贝全部,如果文件夹已存在那么就同步文件夹                
def copyDir(copyPath,pastePath):
        if(os.path.exists(pastePath)):
                synchro(copyPath,pastePath)
        else :
                os.mkdir(pastePath)
                shutil.copytree(copyPath,pastePath)
#子文件夹左右两侧文件夹都包含,就同步两侧子文件夹
def syncDir(copyPath,pastePath):
         copyDir(copyPath,pastePath)
         copyDir(pastePath,copyPath)
while(True):
        synchro(synchroPath1,synchroPath2)
        logging.debug('synchro run')
        #阻塞方法,上一步执行结束后等待五秒
        time.sleep(5)