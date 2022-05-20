import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://beatstars.com')

time.sleep(100)

browser.close()
browser.quit()