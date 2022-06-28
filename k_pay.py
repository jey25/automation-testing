from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#main
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get('https://www.kakaopay.com/')
browser.set_window_size(1650, 950)

browser.implicitly_wait(10)

browser.find_element_by_css_selector('#__next > div.css-1okryao.e17yt6xy6 > header > div.css-1mjuj2d.e1ur28bq3 > a').click()
time.sleep(0.5)

browser.find_element_by_css_selector('#__next > div.css-1okryao.e17yt6xy6 > header > div.css-ezcqgw.e1ur28bq1 > div:nth-child(1) > a').click()
time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="__next"]/header/div[2]/div[2]/a').click()
browser.find_element_by_css_selector('#__next > div.css-1qmh5wl.evcs03d0 > div:nth-child(1) > section > div.css-1ysqers.e1256prn4 > div.css-1al2v5r.e1sz0hhq1 > a:nth-child(3) > p').click()