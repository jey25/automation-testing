from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#main
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get('https://www.naver.com/')
browser.set_window_size(1650, 950)

browser.implicitly_wait(10)

#naver whale banner
browser.find_element_by_xpath('//*[@id="NM_TOP_BANNER"]/div/a[1]').click()
time.sleep(0.5)

# browser.find_element_by_css_selector('body > div > main > section.download > div > a').click()
# browser.find_element_by_css_selector('body > div > main > section.slides > div > button > svg').click()
# time.sleep(2)

#naver whale
browser.find_element_by_css_selector('body > div > header > a').click()
time.sleep(0.5)

browser.find_element_by_css_selector('#ccWrap > header > div > h1 > a').click()
time.sleep(0.5)

browser.find_element_by_css_selector('#ko_main').click()
time.sleep(0.5)

browser.find_element_by_css_selector('body').click()
time.sleep(0.5)

browser.get('https://whale.naver.com/ko/details/omnitasking/')

browser.find_element_by_css_selector('#ccWrap > section.whywhale_top > div > ul > li.current > div > a').click()
browser.find_element_by_css_selector('#ccWrap > section.whywhale_top > div > ul > li:nth-child(2) > div > a').click()
browser.find_element_by_css_selector('#ccWrap > section.whywhale_top > div > ul > li:nth-child(3) > div > a').click()
time.sleep(0.5)

browser.find_element_by_css_selector('#ko_guide').click()
time.sleep(1)

browser.find_element_by_css_selector('#update_list1 > li.pc.clearfix > div.left.text_area > a').click()
browser.get('https://whale.naver.com/ko/whats_new/')

browser.find_element_by_css_selector('#update_list1 > li.Android.clearfix > div.left.text_area > a').click()
browser.get('https://whale.naver.com/ko/whats_new/')

browser.find_element_by_css_selector('#update_list1 > li.iOS.clearfix > div.left.text_area > a').click()
browser.get('https://whale.naver.com/ko/whats_new/')



browser.find_element_by_css_selector('#ccContent > article.WhatsNew_contents.Whale_News > div > div > p > a').click()

i = 2
while i < 36:
    browser.get(f"https://whale.naver.com/ko/whats_new/press/{i}.html")
    browser.get('https://whale.naver.com/ko/whats_new/press/')
    i += 1

browser.find_element_by_xpath('//*[@id="s_year"]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[2]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[3]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[5]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[6]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[7]').click()
browser.find_element_by_xpath('//*[@id="s_year"]').click()
browser.find_element_by_xpath('//*[@id="s_year"]/option[1]').click()

browser.find_element_by_xpath('//*[@id="search_str"]').click()
browser.find_element_by_xpath('//*[@id="search_str"]').send_keys('네이버')
browser.find_element_by_xpath('//*[@id="ccContent"]/article[3]/div[1]/div[1]/form/fieldset/div/p[2]/button').click()
time.sleep(2)

browser.find_element_by_xpath('//*[@id="search_str"]').click()
browser.find_element_by_xpath('//*[@id="search_str"]').clear()
browser.find_element_by_xpath('//*[@id="search_str"]').send_keys('asdasd')
browser.find_element_by_xpath('//*[@id="ccContent"]/article[3]/div[1]/div[1]/form/fieldset/div/p[2]/button').click()

browser.get('https://help.whale.naver.com/desktop/')