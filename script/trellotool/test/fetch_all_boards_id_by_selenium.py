# -*- coding: utf-8 -*-
import getpass
import time
import csv

import simplejson as json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_list = []


def pre_handle_data(html, driver):
    soup = BeautifulSoup(html, 'lxml')
    boards_list = soup.findAll('li', class_='boards-page-board-section-list-item')
    for board in boards_list:
        a = board.find('a')
        if a is None:
            continue
        link = 'https://trello.com' + a.get('href')
        if link in link_list:
            continue
        link_list.append(link)

    for l in link_list:
        driver.get(l+'.json')
        da = json.loads(json.dumps(driver.page_source))
        print(len(da))
        print(da['name'])


def load_page(url, email, pw):
    driver = webdriver.Chrome()
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login')))
    account_element = driver.find_element_by_id('user')
    account_element.send_keys(email)
    password_element = driver.find_element_by_id('password')
    password_element.send_keys(pw)

    btn_login = driver.find_element_by_id('login')
    btn_login.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/a')))
    html = driver.page_source
    pre_handle_data(html, driver)

    driver.close()

if __name__ == '__main__':
    url = 'https://trello.com/login'
    email = ''
    pw = ''
    load_page(url, email, pw)

