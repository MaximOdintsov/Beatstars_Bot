import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from comments import list

from threading import Thread

from database import username, password, username2, password2

from colorama import Fore, Back, Style

browser = webdriver.Firefox()
browser.get('https://beatstars.com/feed')
time.sleep(15)


cookie_consent = browser.find_element(By.XPATH, '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
cookie_consent.click()
print(Fore.WHITE, 'Согласился с cookie')
time.sleep(random.randrange(2, 4))


play_button = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-feed/div/section[2]/div[1]/mp-track-post/mp-feed-card/div/div[2]/div[1]/div[2]/div[1]/bs-button-play-item/button')
play_button.click()
print(Fore.GREEN, 'Включил бит')
time.sleep(random.randrange(2, 5))


opening_beat = browser.find_element(By.XPATH, '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a')
opening_beat.click()
print(Fore.GREEN, 'Открыл описание бита')
time.sleep(random.randrange(10, 15))


likes = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template/mp-button-item-action-icon-template/span')
likes.click()
print(Fore.GREEN, 'Открыл меню с лайкнувшими!')
time.sleep(random.randrange(7, 15))


window_with_liked = browser.find_element(By.CLASS_NAME, 'body-container')
# ищет элементы с тегом "а"
elements = window_with_liked.find_elements(By.TAG_NAME, 'a')
# собирает ссылки на элементы только 'href'
profile_urls = [item.get_attribute('href') for item in elements]
print(Fore.LIGHTCYAN_EX, 'Спарсил ссылки на профили: ', Fore.LIGHTYELLOW_EX, profile_urls)
time.sleep(10)

browser.find_element(By.CSS_SELECTOR, '.close-button').click()
print('Закрыл меню с лайкнувшими')
time.sleep(20)


browser.close()
