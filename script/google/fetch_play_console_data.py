# -*- coding: utf-8 -*-
import getpass
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_anr_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    # anr
    div_detail = soup.find('div', class_='CVP2USC-Dc-b')
    div_detail_item = div_detail.findAll('div', class_='CVP2USC-Vp-d CVP2USC-xd-b')
    div_error_title = div_detail_item[0].find('div', class_='gwt-HTML')
    div_error_infos = div_detail_item[0].findAll('div', class_='gwt-Label CVP2USC-dq-b')

    allInfo = ' '.join(div_error_title.string.replace('\n', ' ').replace(',', '.').split()) + '\n'
    for div_error_info in div_error_infos:
        s1 = div_error_info.string.replace('\n', ' ').replace(',', '.')
        s2 = ' '.join(s1.split())
        allInfo = allInfo + s2 + '\n'
    return allInfo


def get_crash_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    # crash
    div_detail = soup.find('div', class_='CVP2USC-Vp-d')
    div_error_title = div_detail.find('div', class_='gwt-HTML')
    div_error_infos = div_detail.findAll('div', class_='gwt-Label CVP2USC-dq-b')

    allInfo = ''
    if div_error_title.string is None:
        strong = div_error_title.find('strong')
        allInfo = ' '.join(strong.string.replace('\n', ' ').replace(',', '.').split()) + '\n'
    else:
        allInfo = ' '.join(div_error_title.string.replace('\n', ' ').replace(',', '.').split()) + '\n'
    for div_error_info in div_error_infos:
        s1 = div_error_info.string.replace('\n', ' ').replace(',', '.')
        s2 = ' '.join(s1.split())
        allInfo = allInfo + s2 + '\n'
    return allInfo


def get_table_data(session_table, driver, my_writer):
    trs = session_table.findAll('tr')
    for tr in trs:
        pv = tr.findAll('p')
        errorDescription = ''
        errorLocation = ''
        reportsTotal = ''
        numAffected = ''
        for p in pv:
            if p.get('data-type') == 'errorDescription':
                errorDescription = p.get_text()
            elif p.get('data-type') == 'errorLocation':
                errorLocation = p.get_text()
            elif p.get('data-type') == 'reportsTotal':
                reportsTotal = p.get_text()
            elif p.get('data-type') == 'numAffected':
                numAffected = p.get_text()
        print(errorDescription + ' ---- ' + errorLocation + ' ---- ' + reportsTotal + ' ---- ' + numAffected)

        # link
        aaa = tr.find('a')
        if aaa is None:
            continue
        href = 'https://play.google.com/apps/publish/?account=8505122062204140606' + aaa.get('href')
        print(href)

        driver.get(href)
        time.sleep(5)
        detail_html = driver.page_source

        errorInfo = get_anr_detail(detail_html)

        driver.back()
        time.sleep(3)

        my_writer.writerow(
            [errorDescription.replace('\n', ' '), errorLocation.replace('\n', ' '), reportsTotal.replace('\n', ' '),
             numAffected.replace('\n', ' '), errorInfo, href])


def pre_handle_data(html, driver, myWriter):
    soup = BeautifulSoup(html, 'lxml')
    session_tables = soup.findAll('section')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table, driver, myWriter)


def load_page_data(login_url, login_name, login_passwd, page_count):
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)

    # account_element = driver.find_element_by_xpath('//*[@id="identifierId"]')
    account_element = driver.find_element_by_id('identifierId')
    account_element.send_keys(login_name)

    identifier_next = driver.find_element_by_id('identifierNext')
    identifier_next.click()
    time.sleep(5)

    password_element = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_element.send_keys(login_passwd)

    password_next = driver.find_element_by_id('passwordNext')
    password_next.click()
    time.sleep(10)

    with open('playAnr2file1.csv', 'wb') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['信息', '位置', '报告', '受影响用户数量', '错误信息', '详细错误链接'])

        html = driver.page_source
        pre_handle_data(html, driver, myWriter)
        print('加载第1页数据完成')

        curr_page = 1
        while curr_page < page_count:
            next_page_button = driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')
            next_page_button.click()
            time.sleep(8)

            html = driver.page_source
            pre_handle_data(html, driver, myWriter)

            curr_page = curr_page + 1
            print('加载第' + str(curr_page) + '页数据完成')

    # play_cookies = driver.get_cookies()
    driver.close()


if __name__ == '__main__':
    # anr
    url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
    # crash
    # url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION'
    name = input('Google account email: ')
    password = getpass.getpass('Password: ')
    load_page_data(url, name, password, 2)
