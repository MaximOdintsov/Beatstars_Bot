import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from database import username, password

from colorama import Fore, Back, Style

profile_urls = None

browser = webdriver.Firefox()


def authorization():
    try:
        # открываем страницу авторизации в битстарс
        browser.get('https://oauth.beatstars.com/')
        print(Fore.BLUE, Back.BLACK, 'Открыл битстарс')
        time.sleep(random.randrange(2, 5))


        # вводим username
        username_input = browser.find_element(By.ID, 'input-username')
        username_input.click()
        time.sleep(random.randrange(4, 9))

        # вводим пароль (набирается с клавиатуры)
        pyautogui.typewrite(username)
        print('Ввёл логин')
        time.sleep(random.randrange(1, 3))


        # вводим password
        password_input = browser.find_element(By.ID, 'input-password')
        password_input.click()
        time.sleep(random.randrange(5, 10))

        # вводим пароль (набирается с клавиатуры)
        pyautogui.typewrite(password)
        print('Ввёл пароль')
        time.sleep(random.randrange(2, 4))


        # нажимаем на кнопку "Login"
        login_button = browser.find_element(By.XPATH, '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/bs-square-button/button')
        login_button.click()
        print('Вошёл в аккаунт')
        time.sleep(random.randrange(60, 75))


        # соглашаемся с куки
        cookie_consent = browser.find_element(By.XPATH, '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
        cookie_consent.click()
        print('Согласился с cookie')
        time.sleep(random.randrange(4, 8))
        print('Ну что, послушаем немного музыки?')

    except Exception as ex:
        print(Fore.RED, 'Произошла какя-то ошибка, закрываю браузер.')
        print(ex)
        browser.close()
        browser.quit()


def open_feed():
    browser.get('https://www.beatstars.com/feed')
    time.sleep(random.randrange(20, 25))


def play_beat():
    try:
        WebDriverWait(browser, timeout=random.randrange(10, 20)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.feed:nth-child(2) > mp-track-post:nth-child(1) > mp-feed-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > bs-button-play-item:nth-child(1) > button:nth-child(1)"))).click()
        print('Включил бит')
        time.sleep(random.randrange(15, 20))
    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгорит заново.')
        print(ex)
        open_feed()


def open_beat():
    try:
        opening_beat = browser.find_element(By.XPATH, '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a')
        opening_beat.click()
        print(Fore.GREEN, 'Открыл описание бита')
        time.sleep(random.randrange(10, 15))
    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгорит заново')
        print(ex)
        open_feed()

def like():
    try:
        like_button = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template')
        like_button.click()
        print('Поставил лайк')
        time.sleep(random.randrange(5, 10))
    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгоритм заново.')
        print(ex)


def liked():
    try:
        global profile_urls

        likes = browser.find_element(By.XPATH,
                                     '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template/mp-button-item-action-icon-template/span')
        likes.click()
        print('Ищу тех, кто поставил лайк!')
        time.sleep(random.randrange(7, 14))

        # ищет элементы только в окне с теми, кто лайкнул бит
        window_with_liked = browser.find_element(By.CLASS_NAME, 'body-container')

        # ищет элементы с тегом "а"
        elements = window_with_liked.find_elements(By.TAG_NAME, 'a')

        # собирает ссылки на элементы только 'href'
        profile_urls = [item.get_attribute('href') for item in elements]
        print('Спарсил ссылки на профили: ', profile_urls)

        for url in profile_urls:
            browser.get(url)
            time.sleep(random.randrange(10, 15))
            subscription()

    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгоритм заново.')
        print(ex)
        open_feed()


def open_profile():
    try:
        go_to_the_profile = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[2]/mp-caption-figure-template[2]/a')
        go_to_the_profile.click()
        print('Тааак-с, посмотрим, что тут у нас...')
        time.sleep(random.randrange(15, 25))
    except Exception as ex:
        print(Fore.RED, 'произошла какая-то ошибки, запускаю алгоритм заново.')
        print(ex)
        browser.close()
        browser.quit()


def subscription():
    try:

        follow_button = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/ng-component/mp-wrapper-member-profile-content/main/bs-container-grid/mp-profile-header/mp-profile-visitor-actions/div/mp-button-follow-text-template/mp-button-item-action-text-template')
        follow_button.click()
        print('Подписался на этого пользователя!')
        time.sleep(random.randrange(30, 45))
    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгоритм заново.')
        print(ex)
        open_feed()


def back():
    try:
        back_button = browser.back()
        time.sleep(random.randrange(2, 4))
    except Exception as ex:
        print(Fore.RED, 'Произошла какая-то ошибка, запускаю алгоритм заново.')
        print(ex)
        open_feed()


# def next_beat():
#     print(Fore.YELLOW, 'Переключаюсь на следующий бит...')
#     time.sleep(1)
#     next_button = browser.find_element(By.XPATH, '/html/body/mp-root/mp-player-wrapper/bs-player/div/div/div[2]/bs-player-next/button')
#     next_button.click()
#     print('Переключился!')
#     time.sleep(random.randrange(7, 14))


listen_beats = True

authorization()

while listen_beats:
    if listen_beats == True:
        open_feed()
        play_beat()
        open_beat()
        like()
        open_profile()
        subscription()
        back()
        liked()
    else:
        listen_beats = False
        browser.close()
        browser.quit()
        print(Fore.RED, 'Что-то пошло не так, скрипт окончил свою работу.')
