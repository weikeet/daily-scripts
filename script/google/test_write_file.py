# -*- coding: utf-8 -*-
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')

print('adfds'+str(1))
#
# with open('t.csv','wb') as myFile:
#     myWriter=csv.writer(myFile)
#     myWriter.writerow(['信息', '位置', '报告', '受影响用户数量', '错误信息链接'])