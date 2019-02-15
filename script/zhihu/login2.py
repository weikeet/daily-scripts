from selenium import webdriver
from requests import Session
from time import sleep
req = Session()
req.headers.clear()
chromePath = r'/Users/zhengwei.zhang/Documents/MacPlugins/chrome/chromedriver'
wd = webdriver.Chrome(executable_path= chromePath)
zhihuLogInUrl = 'https://www.zhihu.com/signin'
wd.get(zhihuLogInUrl)

#wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
wd.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('username')
wd.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]').send_keys('password')
sleep(10)
wd.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').submit()
sleep(10)
cookies = wd.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])