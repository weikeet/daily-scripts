# -*- coding: utf-8 -*-
import getpass
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

d = {}
file_name = ''
data_type = 0


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


def get_table_data(session_table, driver):
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
        print(errorLocation + ' -- ' + errorDescription + ' -- ' + str(reportsTotal) + ' -- ' + str(numAffected) + ' -- ' + href)

        driver.get(href)
        time.sleep(8)

        detail_html = driver.page_source
        if data_type == 0:
            detailErrorInfo = get_detail_anr(detail_html)
        else:
            detailErrorInfo = get_detail_crash(detail_html)

        if errorLocation in d:
            value = d[errorLocation]
            reportsTotal = reportsTotal + value[0]
            numAffected = numAffected + value[1]
            errorDescription = value[2]
            detailErrorInfo = value[3]
            href = href + ', ' + value[4]
        d[errorLocation] = [reportsTotal, numAffected, errorDescription, detailErrorInfo, href]

        driver.back()
        time.sleep(4)


def pre_handle_data(html, driver):
    soup = BeautifulSoup(html, 'lxml')
    session_tables = soup.findAll('section')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table, driver)


def write_data2file():
    for k, v in d.items():
        print(k + ' =-= ' + str(v))

    with open(file_name + '.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['位置', '信息', '报告', '受影响用户数量', '错误信息', '详细错误链接'])
        for k,v in d.items():
            myWriter.writerow([k, v[2], str(v[0]), str(v[1]), v[3], v[4]])


def load_page_data(target_url, email, pw, page_count):
    driver = webdriver.Chrome()
    driver.get(target_url)
    time.sleep(4)

    # account_element = driver.find_element_by_xpath('//*[@id="identifierId"]')
    account_element = driver.find_element_by_id('identifierId')
    account_element.send_keys(email)
    identifier_next = driver.find_element_by_id('identifierNext')
    identifier_next.click()
    time.sleep(4)

    # password_element = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_element = driver.find_element_by_id('password')
    password_element.send_keys(pw)
    password_next = driver.find_element_by_id('passwordNext')
    password_next.click()
    time.sleep(10)

    print('Start time:')
    print(time.time())

    html = driver.page_source
    pre_handle_data(html, driver)
    print('加载第1页数据完成')

    curr_page = 1
    while curr_page < page_count:
        next_page_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')
        next_page_button.click()
        time.sleep(8)

        html = driver.page_source
        pre_handle_data(html, driver)

        curr_page = curr_page + 1
        print('加载第' + str(curr_page) + '页数据完成')

    driver.close()

    write_data2file()
    print('End time: ' + str(time.time()))


if __name__ == '__main__':
    data_type = input('Please input fetch data type(0: anr, 1: crash): ')
    # url = input('Please input anr/crash url: ')
    page_count = input('Please input fetch page count: ')
    file_name = input('Please input file name: ')
    # anr
    url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
    # crash
    # url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION'
    name = input('Please input google email: ')
    password = getpass.getpass('Password: ')
    load_page_data(url, name, password, int(page_count))
