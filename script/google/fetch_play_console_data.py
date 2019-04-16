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
    gwtHtmlDivs = soup.findAll('div', class_='gwt-HTML')
    if gwtHtmlDivs is None or len(gwtHtmlDivs) < 2:
        print('get_detail_anr gwtHtmlDivs is none or gwtHtmlDivs.length < 2')
        return ''

    print(gwtHtmlDivs[1])
    detailErrorInfo = ' '.join(str(gwtHtmlDivs[1].string).replace('\n', ' ').split()) + '\n'

    gwtHtmlDiv1P = gwtHtmlDivs[1].parent
    div_error_infos = gwtHtmlDiv1P.findAll('div', class_='gwt-Label')
    if div_error_infos is None:
        print('get_detail_anr div_error_infos is none')
        return detailErrorInfo

    for div_error_info in div_error_infos:
        s1 = div_error_info.string.replace('\n', ' ')
        s2 = ' '.join(s1.split())
        detailErrorInfo = detailErrorInfo + s2 + '\n'
    return detailErrorInfo


def get_detail_crash(html):
    soup = BeautifulSoup(html, 'lxml')
    gwtHtmlDivs = soup.findAll('div', class_='gwt-HTML')
    if gwtHtmlDivs is None or len(gwtHtmlDivs) < 1:
        print('get_detail_crash gwtHtmlDivs is none or gwtHtmlDivs.length < 1')
        return ''

    detailErrorInfo = ''
    for gwtHtmlDiv in gwtHtmlDivs:
        if gwtHtmlDiv.string is not None:
            detailErrorInfo = detailErrorInfo + ' '.join(gwtHtmlDiv.string.replace('\n', ' ').split()) + '\n'
        else:
            strong = gwtHtmlDiv.find('strong')
            if strong is not None:
                detailErrorInfo = detailErrorInfo + ' '.join(strong.string.replace('\n', ' ').split()) + '\n'

        gwtHtmlDivP = gwtHtmlDiv.parent
        div_error_infos = gwtHtmlDivP.findAll('div', class_='gwt-Label')
        if div_error_infos is None:
            continue

        for div_error_info in div_error_infos:
            if div_error_info is None:
                continue
            s1 = div_error_info.string.replace('\n', ' ')
            s2 = ' '.join(s1.split())
            detailErrorInfo = detailErrorInfo + s2 + '\n'

    return detailErrorInfo


def longest_common_prefix(strs):
    if not strs: return ''
    ss = list(map(set, zip(*strs)))
    res = ''
    for x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res


def calc_similar(key, dataKey):
    commonStr = longest_common_prefix([key, dataKey])
    commonLen = len(commonStr)

    if commonLen == 0:
        return False

    if len(key) <= len(dataKey):
        minLen = len(key)
    else:
        minLen = len(dataKey)

    if minLen <= 10 and minLen == commonLen:
        print('1 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 20 and commonLen / minLen >= 0.95:
        print('2 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 30 and commonLen / minLen >= 0.9:
        print('3 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 40 and commonLen / minLen >= 0.85:
        print('4 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen > 40 and commonLen / minLen >= 0.80:
        print('x key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    return False


def get_table_data(session_table):
    trs = session_table.findAll('tr')
    if trs is None:
        print('get_table_data: table.tr tag is none')
        return

    for tr in trs:
        # link
        a = tr.find('a')
        if a is None:
            print('get_table_data: a tag is none')
            continue

        pv = tr.findAll('p')
        if pv is None:
            print('get_table_data: p tag is none')
            continue

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
            data[key] = [errorLocation, errorDescription, reportsTotal, numAffected, hrefList, '']
        else:
            hrefList = []
            similar = False
            originErrorLocation = errorLocation
            originErrorDesc = errorDescription
            originReports = reportsTotal
            originAffected = numAffected
            extraInfo = ''
            for dataKey in data.keys():
                if calc_similar(key, dataKey):
                    similar = True
                    value = data[dataKey]
                    errorLocation = value[0]
                    errorDescription = value[1]
                    reportsTotal = reportsTotal + value[2]
                    numAffected = numAffected + value[3]
                    hrefList = value[4]
                    hrefList.insert(len(hrefList), href)
                    extraInfo = value[5]
                    break
            if similar:
                extraInfo = extraInfo + '\n' + originErrorLocation + ', ' + originErrorDesc + ', ' + str(originReports) + ', ' + str(originAffected) + ', ' + href
            else:
                hrefList = [href]
            data[key] = [errorLocation, errorDescription, reportsTotal, numAffected, hrefList, extraInfo]


def pre_handle_data(html):
    soup = BeautifulSoup(html, 'lxml')
    session_tables = soup.findAll('section')
    if session_tables is None:
        print('pre_handle_data section tag is none')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table)


def write_data2file():
    with open(file_name + '.csv', 'w') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['位置', '描述信息', '报告', '影响数量', '详细错误信息', '详细错误链接', '备注'])
        for value in data.values():
            links = ''
            if value[4] is None:
                print('write_data2file links is none')
                continue
            for link in value[4]:
                links = links + link + '\n'
            myWriter.writerow([value[0], value[1], str(value[2]), str(value[3]), value[6], links, value[5]])


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

    print('开始时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')))
    html = driver.page_source
    pre_handle_data(html)
    print('第1页数据加载完成')

    curr_page = 1
    while curr_page < page_count:
        next_page_button = driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')
        next_page_button.click()

        print('start wait next page: ' + str(time.time()))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/table/tbody[1]/tr[1]/td[5]/div/button')))
        print('end wait next page: ' + str(time.time()))

        html = driver.page_source
        pre_handle_data(html)

        curr_page = curr_page + 1
        print('第' + str(curr_page) + '页数据加载完成')

    print('开始加载每项数据的详细错误信息')
    for v in data.values():
        curr_page_url = v[4][0]
        print('当前页面: ' + curr_page_url)
        driver.get(curr_page_url)

        if data_type == 0:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[3]/div/button')))
        else:
            # next page
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/section/div[5]/div/section/div[1]/div[2]/span[2]/div/button[2]')))

        detail_html = driver.page_source
        if data_type == 0:
            detailErrorInfo = get_detail_anr(detail_html)
        else:
            detailErrorInfo = get_detail_crash(detail_html)
        v.insert(len(v), detailErrorInfo)
    print('每项数据的详细错误信息加载完成')

    driver.close()

    write_data2file()
    print('结束时间: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    url = input('Please input anr/crash url: ')
    email = input('Email: ')
    password = getpass.getpass('Password: ')
    page_count = input('Please input page count: ')

    if url is None or url == '':
        url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'

    if 'errorType=ANR' in url:
        data_type = 0
        file_name = 'data_anr_' + page_count + 'page_' + time.strftime("%Y%m%d_%H.%M.%S", time.localtime())
    else:
        data_type = 1
        file_name = 'data_crash_' + page_count + 'page_' + time.strftime("%Y%m%d_%H.%M.%S", time.localtime())

    load_page_data(url, email, password, int(page_count))
