#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver


def load_ciku(soup):
    downloadUrls = soup.findAll('div', class_='dict_dl_btn')

    dUrl = ''
    for downloadUrl in downloadUrls:
        aLink = downloadUrl.find('a')
        # dUrl = dUrl + aLink.get('href') + '.scel\n'
        list = aLink.get('href').split('&name=', 1)
        fileName = list[1] + '.scel'
        print(fileName)
        urllib.request.urlretrieve(url, fileName)

    # return dUrl


if __name__ == '__main__':
    urlData = {
        '城市信息': 'https://pinyin.sogou.com/dict/cate/index/167', '自然科学': 'https://pinyin.sogou.com/dict/cate/index/1',
        '社会科学': 'https://pinyin.sogou.com/dict/cate/index/76', '工程应用': 'https://pinyin.sogou.com/dict/cate/index/96',
        '农林鱼畜': 'https://pinyin.sogou.com/dict/cate/index/127', '医学医药': 'https://pinyin.sogou.com/dict/cate/index/132',
        '电子游戏': 'https://pinyin.sogou.com/dict/cate/index/436', '艺术设计': 'https://pinyin.sogou.com/dict/cate/index/154',
        '生活百科': 'https://pinyin.sogou.com/dict/cate/index/389', '运动休闲': 'https://pinyin.sogou.com/dict/cate/index/367',
        '人文科学': 'https://pinyin.sogou.com/dict/cate/index/31', '娱乐休闲': 'https://pinyin.sogou.com/dict/cate/index/403'
    }

    print('开始时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    i = 0
    sortRule = '/default/'
    driver = webdriver.Chrome()
    for title, url in urlData.items():
        i = i + 1
        if i > 2:
            break
        driver.get(url)

        page = driver.page_source
        soup = BeautifulSoup(page, 'lxml')
        # dUrl = load_ciku(soup)
        load_ciku(soup)
        print(title + ': load page1 finished')

        dictPageList = soup.find('div', id='dict_page_list')
        if dictPageList is None:
            continue
        linkList = dictPageList.findAll('a')
        if linkList is None:
            continue
        linkCount = len(linkList)
        if linkCount < 2:
            continue
        pageCount = int(linkList[linkCount - 2].string)

        a = 1
        if pageCount >3:
            pageCount = 3
        while a <= pageCount:
            a = a + 1
            driver.get(url + sortRule + str(a))
            page = driver.page_source
            soup = BeautifulSoup(page, 'lxml')
            # dUrl = dUrl + load_ciku(soup)
            load_ciku(soup)
            print(title + ': load page' + str(a) + ' finished')

        # file = open(title + '.txt', "w")
        # file.write(dUrl)
        # file.close()
        # print('load ' + title + ' success')

    print('结束时间: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    driver.close()
