
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)
driver.set_window_size(1650, 950)

driver.get(
    'https://csonline.nexon.com/Main/Index')

driver.find_element(By.CSS_SELECTOR, "#GNB_BannerBtToday").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "body > div.gnbWrapper.gnbSizeL > div.gnbBar > h1 > a").click()

driver.find_element(By.CSS_SELECTOR, "#GNB_BannerBtClose").click()

driver.get(
    'https://csonline.nexon.com/Main/Index')



driver.find_element(By.CSS_SELECTOR, "#header > ul > li.active > a").click()
driver.find_element(By.CSS_SELECTOR, "#header > ul > li.active > ul > li.active > a").click()
driver.find_element(By.CSS_SELECTOR, "#container > div > div > ul > li.active > a").click()
