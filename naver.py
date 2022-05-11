from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get('https://www.ustockplus.com/')
browser.set_window_size(1650, 950)

HOME = browser.find_element_by_css_selector('#__next > div > header > div > div > div.css-1f7bmty.e11a8xfx11 > a > span > img')
SEARCH = browser.find_element_by_css_selector('#__next > div > header > div > div > div.css-1f7bmty.e11a8xfx11 > div.css-13uayra.e11a8xfx8 > div > div > input')

browser.implicitly_wait(10)

def homeClick():
    HOME.click()
    time.sleep(2)

def searchClear():
    SEARCH.clear()
    time.sleep(2)

homeClick()

SEARCH.send_keys('두나무')
time.sleep(2)

homeClick()
searchClear()

SEARCH.send_keys(';sldfksd;fk;fsd;lkf')
time.sleep(2)

homeClick()
searchClear()