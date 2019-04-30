# -*- coding: utf-8 -*-
import getpass
import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = {}
data_type = 0
file_name = ''
email = 'zhengwei.zhang@ihandysoft.com'
password = 'Weico@12138'


def write_data2file():
    with open(file_name + '.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['时间', '报告数量', '影响数量'])
        for key, value in data.items():
            myWriter.writerow([key, value[0], value[1]])


def load_page_data(target_url, email, pw):
    driver = webdriver.Chrome()
    driver.get(target_url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
    # account_element = driver.find_element_by_xpath('//*[@id="identifierId"]')
    account_element = driver.find_element_by_id('identifierId')
    account_element.send_keys(email)
    identifier_next = driver.find_element_by_id('identifierNext')
    identifier_next.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
    password_element = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_element.send_keys(pw)
    password_next = driver.find_element_by_id('passwordNext')
    password_next.click()

    print('开始时间: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    if data_type == 0:
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[3]/div/button')))
    else:
        # next page
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[1]/div[2]/span[2]/div/button[2]')))

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    gwt_container = soup.findAll('div', class_='gwt-viz-container')
    tbody = gwt_container[0].find('tbody')
    trs = tbody.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        data[tds[0].string] = [tds[1].string, tds[2].string]

    driver.close()

    write_data2file()
    print('结束时间: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if __name__ == '__main__':
    url = input('Please input anr/crash url: ')

    if url is None or url == '':
        url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR&clusterName=apps/com.mobile.security.antivirus.applock.wifi/clusters/c820f9e3&detailsAppVersion=PRODUCTION&detailsSpan=30'

    if 'errorType=ANR' in url:
        data_type = 0
        file_name = 'table_anr_' + time.strftime("%Y%m%d_%H.%M.%S", time.localtime())
    else:
        data_type = 1
        file_name = 'table_crash_' + time.strftime("%Y%m%d_%H.%M.%S", time.localtime())

    load_page_data(url, email, password)
