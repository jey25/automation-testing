from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get('https://stockplus.com/m')

browser.implicitly_wait(10)

browser.find_element_by_css_selector('body > div:nth-child(1) > div > div:nth-child(1) > header > div.topDef.new-topDef > h1 > a').click()
time.sleep(2)

browser.find_element_by_css_selector('.btnMy').click()
time.sleep(2)

browser.find_element_by_css_selector('.btnPrev').click()
time.sleep(2)

search = browser.find_element_by_css_selector('input.maintxt')
search.click()

search.send_keys('삼성전자')
search.send_keys(Keys.ENTER)