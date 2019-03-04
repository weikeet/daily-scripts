# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup, Comment, sys

reload(sys)
sys.setdefaultencoding('utf-8')

csv = open('csvfile.csv', "w")
csv.write('信息' + ',' + '位置' + ',' + '报告' + ',' + '受影响用户数量' + ',' + '错误信息链接' + '\n')


def get_detail_error(html):
    soup = BeautifulSoup(html, 'lxml')
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    div_detail = soup.find('div', class_='CVP2USC-Dc-b')
    div_detail_item = div_detail.findAll('div', class_='CVP2USC-Vp-d CVP2USC-xd-b')

    div_error_title = div_detail_item[0].find('div', class_='gwt-HTML')
    print(' '.join(div_error_title.string.replace('\n', ' ').replace(',', '.').split()))
    div_error_infos = div_detail_item[0].findAll('div', class_='gwt-Label CVP2USC-dq-b')

    allInfo = ''
    for div_error_info in div_error_infos:
        s1 = div_error_info.string.replace('\n', ' ').replace(',', '.')
        s2 = ' '.join(s1.split())
        print(s2)


def get_table_data(session_table, driver):
    trs = session_table.findAll('tr')
    ttt = 0;
    for tr in trs:
        # div = tr.find('div', 'LTMPNY-od-a')
        # errors = div.findAll('p')
        # errorDescription
        # errorDescription = errors[0].get_text()
        # errorLocation
        # errorLocation = errors[1].get_text()

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
        time.sleep(10)
        detail_html = driver.page_source
        soup = BeautifulSoup(detail_html, 'lxml')
        file11 = open("error13.html", "w")
        file11.write(str(soup))
        driver.back()
        time.sleep(5)

    row = errorDescription.replace('\n', ' ').replace(',', '.') + ',' \
          + errorLocation.replace('\n', ' ').replace(',', '.') + ',' \
          + reportsTotal.replace('\n', ' ').replace(',', '.') + ',' \
          + numAffected.replace('\n', ' ').replace(',', '.') + ',' \
          + href
    print(row)
    csv.write(row + '\n')


def pre_handle_data(html, driver):
    soup = BeautifulSoup(html, 'lxml')
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    session_tables = soup.findAll('section')
    for session_table in session_tables:
        if session_table.get('role') == 'article':
            get_table_data(session_table, driver)


def login(login_url, login_name, login_passwd):
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
    time.sleep(15)

    html = driver.page_source
    # soup = BeautifulSoup(html,'lxml')
    pre_handle_data(html, driver)
    print('OK0')
    # file = open("AnrPage0.html", "w")
    # file.write(str(soup))

    next_page_button = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/section/div/div/div/span[2]/div/button[2]')
    next_page_button.click()
    time.sleep(15)

    html = driver.page_source
    # soup = BeautifulSoup(html, 'lxml')
    pre_handle_data(html, driver)
    print('OK1')
    # file = open("AnrPage1.html", "w")
    # file.write(str(soup))

    play_cookies = driver.get_cookies()
    driver.close()
    return play_cookies


if __name__ == '__main__':
    url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
    name = input('Name:\n')
    password = input('PW:\n')
    cookies = login(url, name, password)
    # print(cookies)
