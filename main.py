import pyautogui
import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from database import username, password

browser = webdriver.Chrome()

# логинимся
def login():
    # открываем страницу авторизации в битстарс
    browser.get('https://oauth.beatstars.com/')
    print('Открыл битстарс')
    time.sleep(random.randrange(2, 5))

    # вводим username
    username_input = browser.find_element(By.ID, 'input-username')
    username_input.click()
    time.sleep(random.randrange(4, 9))
    pyautogui.typewrite(username)
    print('Ввёл логин')
    time.sleep(random.randrange(1, 3))

    # вводим password
    password_input = browser.find_element(By.ID, 'input-password')
    password_input.click()
    time.sleep(random.randrange(5, 10))
    pyautogui.typewrite(password)
    print('Ввёл пароль')
    time.sleep(random.randrange(2, 4))

    # нажимаем на кнопку "Login"
    button_login = browser.find_element(By.XPATH, '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/bs-square-button/button')
    button_login.click()
    print('Вошёл в аккаунт')
    time.sleep(random.randrange(10, 15))

# Соглашаемся на использование файлов cookie
def cookie():
    cookie_consent = browser.find_element(By.XPATH, '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
    cookie_consent.click()
    print('Согласился с cookie')
    time.sleep(random.randrange(2, 4))


# открываем вкладку "Топ Чарты"
def top_charts():
    print('Открываю Топ чарты')
    time.sleep(1)
    browser.get('https://www.beatstars.com/top-charts')
    print('Ну что, насладимся прекрасной музыкой?')
    time.sleep(random.randrange(3, 5))


# нажимаем на кнопку включения бита
def turn_beats():
    print('Включаю музыку для тебя...')
    time.sleep(1)
    turn_ad_beat = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-internal-page-tracks-wrapper/bs-container-grid[3]/mp-wrapper-list-holder-section/section/mp-list-card-track/div/mp-list-card-template/div/mp-card-figure-track[1]/mp-card-figure-template/figure/div/div[2]/div[2]/mp-button-play-track-on-search')
    turn_ad_beat.click()
    time.sleep(random.randrange(10, 15))


# открываем бит
def open_beat():
    opening_beat = browser.find_element(By.XPATH, '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a')
    opening_beat.click()
    print('Открыл описание бита')
    time.sleep(random.randrange(4, 10))


# ставим лайк
def like():
    like_the_beat = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template')
    like_the_beat.click()
    print('Поставил лайк, перехожу в профиль!')
    time.sleep(random.randrange(5, 10))


# переходим в профиль и подписываемся (нужно будет разделить функции)
def following_in_beat():
    go_to_the_profile = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[2]/mp-caption-figure-template[2]/a')
    go_to_the_profile.click()
    print('Тааак-с, посмотрим, что тут у нас...')
    time.sleep(random.randrange(7, 12))

    time.sleep(random.randrange(1))
    follow = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/ng-component/mp-wrapper-member-profile-content/main/bs-container-grid/mp-profile-header/mp-profile-visitor-actions/div/mp-button-follow-text-template/mp-button-item-action-text-template')
    follow.click()
    print('Подписался на этого пользователя!')
    time.sleep(random.randrange(5, 15))


# переходим на следующий бит
def next_beat():
    print('Переключаюсь на следующий бит...')
    time.sleep(1)
    next_button = browser.find_element(By.XPATH, '/html/body/mp-root/mp-player-wrapper/bs-player/div/div/div[2]/bs-player-next/button')
    next_button.click()
    print('Переключился на другой бит')
    time.sleep(random.randrange(5, 10))

login()
cookie()
top_charts()


turn_beats()
open_beat()
like()
following_in_beat()
next_beat()
open_beat()
like()
following_in_beat()
next_beat()
open_beat()
like()
following_in_beat()
next_beat()
open_beat()
like()
following_in_beat()
next_beat()
open_beat()
like()
following_in_beat()
next_beat()

# закрываем браузер
browser.close()
browser.quit()