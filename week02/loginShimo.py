from selenium import webdriver
import time


browser = webdriver.Chrome('/usr/local/Cellar/python/3.7.7/bin/chromedriver')

try:
    browser.get('https://shimo.im/login?from=home')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('account@gmail.com')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('password')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    cookies = browser.get_cookies()
    print(cookies)

except Exception as e:
    print(e)
finally:
     browser.close()
