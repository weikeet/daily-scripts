#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#https://mp.weixin.qq.com/s?__biz=MzAwOTcyNDE1Mw==&mid=2656578247&idx=1&sn=df0830d0baf92c1c399748057c8ff1d3&mpshare=1&scene=25&srcid=1224yFH7rasWJD6O3KhAk9Kn#wechat_redirect

def yingyonghui_crawler(name):

    url = 'http://www.appchina.com/sou/' + name

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = soup.select(' ul > li > div.app-info > h1 > a')[0].get_text()

    times = soup.select(' ul > li > div.app-info > span.download-count')[0].get_text()[:-2]

    print('在应用汇上，' + title + '下载量为：' + times)
def zhushou_crawler(name):

    url = 'http://zhushou.360.cn/search/index/?kw=' + name

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = soup.select(' body > div.warp > div.main > div > ul > li > dl > dd > h3 > a > span')[0].get_text()

    times = soup.select(' body > div.warp > div.main > div > ul > li > div > div.sdlft > p.downNum')[0].get_text()[:-3]

    print('在360手机助手上，' + title + '下载量为：' + times)

def kuan_crawler(name):

    url = 'http://www.coolapk.com/search?q=' + name

    web_data = requests.get(url)

    soup = BeautifulSoup(web_data.text, 'lxml')

    title = soup.select('body > div.warpper > div:nth-child(2) > div.app_left > div.apk_left_one > div > div > div.apk_topbar_mss > p.detail_app_title')[0].get_text()

    times = soup.select('body > div.warpper > div:nth-child(2) > div.app_left > div.apk_left_one > div > div > div.apk_topbar_mss > p.apk_topba_message')[0].get_text()

    comma_location = times.find('，')

    times_tidy = times[int(comma_location) + 1:-5]

    print('在酷安网上，' + title + '下载量为：' + times_tidy)

name = input('请输入想搜索的应用名：')

yingyonghui_crawler(name)

zhushou_crawler(name)

kuan_crawler(name)