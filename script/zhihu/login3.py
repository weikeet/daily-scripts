from selenium import webdriver

chromePath = r'/Users/zhengwei.zhang/Documents/MacPlugins/chrome/chromedriver'
driver = webdriver.Chrome(executable_path= chromePath)
driver.maximize_window()
driver.get('https://www.zhihu.com/')

elem = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/button[1]').click()
driver.find_element_by_xpath('/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys('username')
driver.find_element_by_xpath('/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('password')
driver.find_element_by_xpath('/html/body/div[5]/div/span/div/div[2]/div/div/div/div[2]/div[1]/form/button').click()
print(driver.page_source)