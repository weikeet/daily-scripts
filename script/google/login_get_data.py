# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup, Comment, sys

def login(login_url, login_name, login_passwd):
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(5)

    #account = driver.find_element_by_xpath('//*[@id="identifierId"]')
    account = driver.find_element_by_id('identifierId')
    account.send_keys(login_name)

    identifier_next = driver.find_element_by_id('identifierNext')
    identifier_next.click()
    time.sleep(5)

    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(login_passwd)

    password_next = driver.find_element_by_id('passwordNext')
    password_next.click()
    time.sleep(15)

    jd_cookies = driver.get_cookies()
    html = driver.page_source
    #file = open("titles.html", "w")
    #file.write(html)
    #print(html)

    soup = BeautifulSoup(html,'lxml')
    print('OK')
    file = open("tttt.html", "w")
    file.write(str(soup))

    # for element in soup(text=lambda text: isinstance(text, Comment)):
    #     element.extract()
    #
    # trs = soup.findAll('tr')
    #
    # csv = open('csv2file.csv', "w")
    # csv.write('信息' + ',' + '位置' + ',' + '报告' + ',' + '受影响用户数量' + ',' + '详细错误信息' + '\n')
    #
    # for tr in trs:
    #     # div = tr.find('div', 'LTMPNY-od-a')
    #     # errors = div.findAll('p')
    #     # errorDescription
    #     # errorDescription = errors[0].get_text()
    #     # errorLocation
    #     # errorLocation = errors[1].get_text()
    #
    #     pv = tr.findAll('p')
    #
    #     errorDescription = ''
    #     errorLocation = ''
    #     reportsTotal = ''
    #     numAffected = ''
    #     for p in pv:
    #         if p.get('data-type') == 'errorDescription':
    #             errorDescription = p.get_text()
    #         elif p.get('data-type') == 'errorLocation':
    #             errorLocation = p.get_text()
    #         elif p.get('data-type') == 'reportsTotal':
    #             reportsTotal = p.get_text()
    #         elif p.get('data-type') == 'numAffected':
    #             numAffected = p.get_text()
    #
    #     print(errorDescription)
    #     print(errorLocation)
    #     print(reportsTotal)
    #     print(numAffected)
    #
    #     # link
    #     href = 'https://play.google.com/apps/publish/?account=8505122062204140606' + \
    #            tr.find('a').get('href')
    #     print(href)
    #
    #     row = errorDescription.replace('\n', '').replace(
    #         ',', '.') + ',' + errorLocation + ',' + reportsTotal + ',' + numAffected + ',' + href
    #     print(row)
    #     csv.write(row + '\n')

    driver.close()
    return jd_cookies

if __name__ == '__main__':
    url = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.mobile.security.antivirus.applock.wifi&appid=4972898036482753524&appVersion=PRODUCTION&errorType=ANR'
    name = input('Name:\n')
    password = input('PW:\n')
    cookies = login(url, name, password)
    #print(cookies)