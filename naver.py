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


browser.find_element_by_css_selector('#press_list > li:nth-child(1) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(2) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(3) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(4) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(5) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(6) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(7) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(8) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(9) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')


browser.find_element_by_css_selector('#press_paging > li:nth-child(4) > a').click()


browser.find_element_by_css_selector('#press_list > li:nth-child(1) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(2) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(3) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(4) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(5) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(6) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(7) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(8) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(9) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')


browser.find_element_by_css_selector('#press_paging > li:nth-child(5) > a').click()

browser.find_element_by_css_selector('#press_list > li:nth-child(1) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(2) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(3) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(4) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(5) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(6) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(7) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(8) > a > span.left').click()
browser.get('https://whale.naver.com/ko/whats_new/press/')

browser.find_element_by_css_selector('#press_list > li:nth-child(9) > a > span.left').click()