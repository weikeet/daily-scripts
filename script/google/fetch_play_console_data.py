# -*- coding: utf-8 -*-
import getpass
import time
import csv

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# key: errorLocation + errorDescription
# value: [errorLocation, errorDescription, reportsTotal, numAffected, hrefList]
# hrefList: [href, href, ...]
data = {}
# 0: ANR, 1: Crash
data_type = 0
file_name = ''


def get_detail_anr(html):
    soup = BeautifulSoup(html, 'lxml')
    div_detail = soup.find('div', class_='CVP2USC-Dc-b')
    if div_detail is not None:
        div_detail_item = div_detail.findAll('div', class_='CVP2USC-Vp-d CVP2USC-xd-b')
        div_error_title = div_detail_item[0].find('div', class_='gwt-HTML')
        div_error_infos = div_detail_item[0].findAll('div', class_='gwt-Label CVP2USC-dq-b')

        detailErrorInfo = ' '.join(div_error_title.string.replace('\n', ' ').split()) + '\n'
        for div_error_info in div_error_infos:
            s1 = div_error_info.string.replace('\n', ' ')
            s2 = ' '.join(s1.split())
            detailErrorInfo = detailErrorInfo + s2 + '\n'
        return detailErrorInfo

    else:
        div_detail = soup.find('div', class_='F3HRQGD-Kc-b')
        div_detail_item = div_detail.findAll('div', class_='F3HRQGD-bq-d F3HRQGD-Qd-b')
        div_error_title = div_detail_item[0].find('div', class_='gwt-HTML')
        div_error_infos = div_detail_item[0].findAll('div', class_='gwt-Label F3HRQGD-hq-b')

        detailErrorInfo = ' '.join(div_error_title.string.replace('\n', ' ').split()) + '\n'
        for div_error_info in div_error_infos:
            s1 = div_error_info.string.replace('\n', ' ')
            s2 = ' '.join(s1.split())
            detailErrorInfo = detailErrorInfo + s2 + '\n'
        return detailErrorInfo


def get_detail_crash(html):
    soup = BeautifulSoup(html, 'lxml')
    div_detail = soup.find('div', class_='CVP2USC-Vp-d')
    if div_detail is not None:
        div_error_title = div_detail.find('div', class_='gwt-HTML')
        div_error_infos = div_detail.findAll('div', class_='gwt-Label CVP2USC-dq-b')

        if div_error_title.string is not None:
            detailErrorInfo = ' '.join(div_error_title.string.replace('\n', ' ').split()) + '\n'
        else:
            strong = div_error_title.find('strong')
            detailErrorInfo = ' '.join(strong.string.replace('\n', ' ').split()) + '\n'
        for div_error_info in div_error_infos:
            s1 = div_error_info.string.replace('\n', ' ')
            s2 = ' '.join(s1.split())
            detailErrorInfo = detailErrorInfo + s2 + '\n'
        return detailErrorInfo

    else:
        div_detail = soup.findAll('div', class_='F3HRQGD-bq-d')
        detailErrorInfo = ''
        for detail in div_detail:
            div_error_title = detail.find('div', class_='gwt-HTML')
            div_error_infos = detail.findAll('div', class_='gwt-Label F3HRQGD-hq-b')

            if div_error_title.string is not None:
                detailErrorInfo = ' '.join(div_error_title.string.replace('\n', ' ').split()) + '\n'
            else:
                strong = div_error_title.find('strong')
                detailErrorInfo = ' '.join(strong.string.replace('\n', ' ').split()) + '\n'
            for div_error_info in div_error_infos:
                s1 = div_error_info.string.replace('\n', ' ')
                s2 = ' '.join(s1.split())
                detailErrorInfo = detailErrorInfo + s2 + '\n'
        return detailErrorInfo


def get_table_data(session_table):
    trs = session_table.findAll('tr')
    for tr in trs:
        # link
        a = tr.find('a')
        if a is None:
            continue

        pv = tr.findAll('p')
        errorDescription = ''
        errorLocation = ''
        reportsTotal = 0
        numAffected = 0
        for p in pv:
            if p.get('data-type') == 'errorDescription':
                errorDescription = p.get_text().replace('\n', ' ')
            elif p.get('data-type') == 'errorLocation':
                errorLocation = p.get_text().replace('\n', ' ')
            elif p.get('data-type') == 'reportsTotal':
                reportsTotal = int(p.get_text().replace('\n', ' '))
            elif p.get('data-type') == 'numAffected':
                numAffected = int(p.get_text().replace('\n', ' '))

        href = 'https://play.google.com/apps/publish/?account=8505122062204140606' + a.get('href')
        print(errorLocation + ' -- ' + errorDescription + ' -- ' + str(reportsTotal) + ' -- ' + str(
            numAffected) + ' -- ' + href)

        key = errorLocation + errorDescription
        if key in data:
            value = data[key]
            reportsTotal = reportsTotal + value[2]
            numAffected = numAffected + value[3]
            hrefList = value[4]
            if href in hrefList:
                continue
            hrefList.insert(len(hrefList), href)
        else:
            hrefList = [href]
        data[key] = [errorLocation, errorDescription, reportsTotal, numAffected, hrefList]


def pre_handle_data(html):
    soup = BeautifulSoup(html, 'lxml')
    session_tables = soup.findAll('section')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table)


def write_data2file():
    with open(file_name + '.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['位置', '描述信息', '报告', '影响数量', '详细错误信息', '详细错误链接'])
        for k, v in data.items():
            myWriter.writerow([v[0], v[1], str(v[2]), str(v[3]), v[5], str(v[4])])


def load_page_data(target_url, email, pw, page_count):
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

    print('开始时间:' + str(time.time()))

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')))
    html = driver.page_source
    pre_handle_data(html)
    print('第1页数据加载完成')

    curr_page = 1
    while curr_page < page_count:
        next_page_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')
        next_page_button.click()

        print('start wait next page: ' + str(time.time()))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/table/tbody[1]/tr[1]/td[5]/div/button')))
        print('end wait next page: ' + str(time.time()))

        html = driver.page_source
        pre_handle_data(html)

        curr_page = curr_page + 1
        print('第' + str(curr_page) + '页数据加载完成')

    print('开始加载每项数据的详细错误信息')
    for k, v in data.items():
        curr_page_url = v[4][0]
        print('当前页面: ' + curr_page_url)
        driver.get(curr_page_url)

        if data_type == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[3]/div/button')))
        else:
            # next page
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[1]/div[2]/span[2]/div/button[2]')))

        detail_html = driver.page_source
        if data_type == 0:
            detailErrorInfo = get_detail_anr(detail_html)
        else:
            detailErrorInfo = get_detail_crash(detail_html)
        v.insert(len(v), detailErrorInfo)
    print('每项数据的详细错误信息加载完成')

    driver.close()

    write_data2file()
    print('结束时间: ' + str(time.time()))


if __name__ == '__main__':
    url = input('Please input anr/crash url: ')
    page_count = input('Please input page count: ')
    file_name = input('Please input file name: ')
    email = input('Gmail: ')
    password = getpass.getpass('Password: ')

    # anrl
    # url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
    # crash
    # url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION'

    if 'errorType=ANR' in url:
        data_type = 0
    else:
        data_type = 1

    load_page_data(url, email, password, int(page_count))
