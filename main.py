import pyautogui
import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from database import username, password

from colorama import init
from colorama import Fore, Back, Style


browser = webdriver.Chrome()

# ЛОГИНИМСЯ


def login():
    try:
        print(Fore.BLUE, Back.BLACK)
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

        # соглашаемся с куки
        cookie_consent = browser.find_element(By.XPATH, '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
        cookie_consent.click()
        print('Согласился с cookie')
        time.sleep(random.randrange(2, 4))
        print('Ну что, послушаем немного музыки?')
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# открываем вкладку "Топ Чарты"


def top_charts():
    try:
        print(Fore.CYAN, 'Открываю Топ чарты')
        time.sleep(1)
        browser.get('https://www.beatstars.com/top-charts')
        time.sleep(random.randrange(3, 5))

        # функция
        playing_promo_beats()
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# нажимаем на КНОПКУ включения бита (рекламного)


def playing_promo_beats():
    try:
        print('Включаю музыку для тебя...')
        time.sleep(1)
        play_promo_beat = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-internal-page-tracks-wrapper/bs-container-grid[3]/mp-wrapper-list-holder-section/section/mp-list-card-track/div/mp-list-card-template/div/mp-card-figure-track[1]/mp-card-figure-template/figure/div/div[2]/div[2]/mp-button-play-track-on-search')
        play_promo_beat.click()
        time.sleep(random.randrange(15, 20))
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# открываем описание бита


def open_beat():
    try:
        opening_beat = browser.find_element(By.XPATH, '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a')
        opening_beat.click()
        print(Fore.GREEN, 'Открыл описание бита')
        time.sleep(random.randrange(4, 10))

        # функция
        like()
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# ставим лайк


def like():
    try:
        like_the_beat = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template')
        like_the_beat.click()
        print('Поставил лайк, перехожу в профиль!')
        time.sleep(random.randrange(5, 10))

        # функция
        open_profile()
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# переходим в профиль и подписываемся (нужно будет разделить функции)


def open_profile():
    try:
        go_to_the_profile = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[2]/mp-caption-figure-template[2]/a')
        go_to_the_profile.click()
        print('Тааак-с, посмотрим, что тут у нас...')
        time.sleep(random.randrange(7, 12))

        # функция
        following()
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()

# подписываемся на профиль


def following():
    try:
        time.sleep(random.randrange(1))
        follow = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/ng-component/mp-wrapper-member-profile-content/main/bs-container-grid/mp-profile-header/mp-profile-visitor-actions/div/mp-button-follow-text-template/mp-button-item-action-text-template')
        follow.click()
        print('Подписался на этого пользователя!')
        time.sleep(random.randrange(5, 15))
    except:
        print(Fore.RED, 'Произошла какая-то неведомая херня, подписаться не удалось :(')
        next_beat()
        time.sleep(random.randrange(2,4))

# переходим на следующий бит


def next_beat():
    try:
        print(Fore.YELLOW, 'Переключаюсь на следующий бит...')
        time.sleep(1)
        next_button = browser.find_element(By.XPATH, '/html/body/mp-root/mp-player-wrapper/bs-player/div/div/div[2]/bs-player-next/button')
        next_button.click()
        print('Переключился!')
        time.sleep(random.randrange(7,14))
    except Exception as ex:
        print(Fore.RED, ex)
        browser.close()
        browser.quit()


login()

ad_beats = True
error = False

while ad_beats:
    if error == False:
        top_charts()
        open_beat()
        next_beat()
        open_beat()

    else:
        error = True
        browser.close()
        browser.quit()


print(Fore.RED)

# закрываем браузер
browser.close()
browser.quit()