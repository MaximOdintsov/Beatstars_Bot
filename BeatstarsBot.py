import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from comments import list_comments

# from threading import Thread
# from selenium.webdriver.common.keys import Keys
# from database import username, password, username2, password2

from colorama import Fore, Back


class Beatstars_Bot:
    """Класс работы бота"""

    def __init__(self, log, pas):
        """Переменные для входа в аккаунт"""

        self.list_comment = None
        self.profile_urls = None
        self.profile_url = None
        self.sleep_1_cycle = None
        self.sleep_day_cycle = None
        self.number = None

        self.username = log
        self.password = pas
        self.browser = webdriver.Firefox()
        print(Fore.LIGHTMAGENTA_EX, 'БОТ НАЧАЛ СВОЮ РАБОТУ')

    def oauth_beatstars(self):
        """Открывает страницу авторизации в битстарс"""

        try:
            print(Fore.LIGHTMAGENTA_EX, 'БОТ НАЧАЛ АВТОРИЗАЦИЮ!')
            self.browser.get('https://oauth.beatstars.com/')
            print(Fore.LIGHTWHITE_EX, Back.BLACK, ' Открыл битстарс')
            time.sleep(random.randrange(5, 15))

            self.input_username()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть битстарс, запускаю авторизацию заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.oauth_beatstars()

    def input_username(self):
        """Вводит имя пользователя"""

        try:
            username_input = self.browser.find_element(By.XPATH,
                                                       '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/div[1]/bs-text-input/input')
            username_input.click()
            time.sleep(random.randrange(5, 10))
            username_input.send_keys(self.username)

            print(Fore.WHITE, 'Ввёл логин')
            time.sleep(random.randrange(1, 3))

            self.input_password()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось ввести имя пользователя, запускаю авторизацию заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.oauth_beatstars()

    def input_password(self):
        """Вводит пароль"""

        try:
            password_input = self.browser.find_element(By.XPATH,
                                                       '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/div[2]/bs-text-input/input')
            password_input.click()
            time.sleep(random.randrange(5, 10))
            password_input.send_keys(self.password)

            print(Fore.WHITE, 'Ввёл пароль')
            time.sleep(random.randrange(1, 3))

            self.login_button()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось ввести пароль, запускаю авторизацию заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.oauth_beatstars()

    def login_button(self):
        """Нажимает на кнопку 'Войти' """

        try:
            login_button = self.browser.find_element(By.XPATH,
                                                     '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/bs-square-button/button')
            login_button.click()
            print(Fore.LIGHTWHITE_EX, 'Нажал на кнопку "Войти"')
            time.sleep(random.randrange(55, 70))

            self.consent_to_cookies()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось нажать на кнопку "Войти", запускаю алгоритм заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.oauth_beatstars()

    def verification(self):
        try:
            print('Посмотри, пришло ли тебе письмо с кодом подтверждения на почту, если да, то вводи по 1 цифре в каждом сообщении')
        # вводит 1ю цифру кода подтверждения
            confirmation_code1 = self.browser.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/bs-dialog/div[2]/div/bs-code-input/form/div/input[3]')
            confirmation_code1.click()
            print(Fore.LIGHTBLUE_EX, 'Введите 1ю цифру: ')
            confirmation_code1.send_keys(input())

        # вводит 2ю цифру кода подтверждения
            confirmation_code2 = self.browser.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/bs-dialog/div[2]/div/bs-code-input/form/div/input[4]')
            confirmation_code2.click()
            print(Fore.LIGHTBLUE_EX, 'Введите 2ю цифру: ')
            confirmation_code2.send_keys(input())

        # вводит 3ю цифру кода подтверждения
            confirmation_code3 = self.browser.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/bs-dialog/div[2]/div/bs-code-input/form/div/input[5]')
            confirmation_code3.click()
            print(Fore.LIGHTBLUE_EX, 'Введите 3ю цифру: ')
            confirmation_code3.send_keys(input())

        # вводит 4ю цифру кода подтверждения
            confirmation_code4 = self.browser.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div/mat-dialog-container/ng-component/bs-dialog/div[2]/div/bs-code-input/form/div/input[6]')
            confirmation_code4.click()
            print(Fore.LIGHTBLUE_EX, 'Введите 4ю цифру: ')
            confirmation_code4.send_keys(input())

            time.sleep(random.randrange(5, 10))
            self.consent_to_cookies()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось ввести код верификации, открываю эту страницу заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.homepage()

    def consent_to_cookies(self):
        """Нажимает на кнопку 'Согласиться с куки' """

        try:
            cookie_consent = self.browser.find_element(By.XPATH,
                                                       '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
            cookie_consent.click()
            print(Fore.WHITE, 'Согласился с cookie')
            time.sleep(random.randrange(2, 4))
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось согласиться с куки, пробую ввести код верификации')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.verification()

    def homepage(self):
        """Открывает начальную страницу битстарс"""

        try:
            self.browser.get('https://beatstars.com/')
            print(Fore.WHITE, 'Открыл начальную страницу, т.к. не получилось согласиться с куки')
            time.sleep(random.randrange(5, 15))

            self.consent_to_cookies()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Снова не получилось согласиться с куки, запускаю алгоритм заново')
            print(ex)
            time.sleep(random.randrange(5, 10))
            self.oauth_beatstars()

    def open_feed(self):
        """Открывает фид"""

        try:
            self.browser.get('https://www.beatstars.com/feed')
            print(Fore.LIGHTMAGENTA_EX, ' Открыл фид!')
            time.sleep(random.randrange(10, 20))

            self.play_beat()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть фид, пробую заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def play_beat(self):
        """Нажимает на кнопку включения бита"""

        try:
            play_button = self.browser.find_element(By.XPATH,
                                                    '/html/body/mp-root/div/div/ng-component/mp-feed/div/section[2]/div[1]/mp-track-post/mp-feed-card/div/div[2]/div[1]/div[2]/div[1]/bs-button-play-item/button')
            play_button.click()
            print(Fore.GREEN, 'Включил бит')
            time.sleep(random.randrange(5, 10))

            self.open_beat()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось нажать на кнопку включения бита, запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def open_beat(self):
        """Открывает описание бита"""

        try:
            opening_beat = self.browser.find_element(By.XPATH,
                                                     '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a')
            opening_beat.click()

            print(Fore.GREEN, 'Открыл описание бита')
            time.sleep(random.randrange(10, 15))

            self.comments()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть описание бита, запускаю алгоритм заново')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def like(self):
        """Нажимает на кнопку лайка в описании бита"""

        try:
            like_button = self.browser.find_element(By.XPATH,
                                                    '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template')
            like_button.click()
            print(Fore.LIGHTGREEN_EX, 'Поставил', Fore.LIGHTBLUE_EX, 'лайк')
            time.sleep(random.randrange(3, 7))

            self.cycle_to_liked()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось поставить лайк, пишу комментарий.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.cycle_to_liked()

    def comment(self):
        """Определяет рандомный комментарий"""

        self.list_comment = random.choice(list_comments)

    def comments(self):
        """Печатает и отправляет комментарии"""

        try:
            self.comment()

            # нажимает на поле ввода и пишет рандомный комментарий
            input_comments = self.browser.find_element(By.XPATH,
                                                       '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[3]/div[2]/mp-comments-panel-box/mp-open-close-panel-template/div/article/div[2]/mp-create-new-comment-input/mp-musician-autocomplete-wrapper/mp-autocomplete-dropdown-template/div/div[2]/mp-compose-new-message-input/form/div[2]/input')
            time.sleep(random.randrange(5, 10))
            input_comments.send_keys(self.list_comment)
            print(Fore.LIGHTGREEN_EX, "Ввёл", Fore.LIGHTBLUE_EX, "комментарий:\n", Fore.LIGHTYELLOW_EX,
                  self.list_comment)

            # нажимает на кнопку отправки комментария
            comment_button = self.browser.find_element(By.XPATH,
                                                       '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[3]/div[2]/mp-comments-panel-box/mp-open-close-panel-template/div/article/div[2]/mp-create-new-comment-input/mp-musician-autocomplete-wrapper/mp-autocomplete-dropdown-template/div/div[2]/mp-compose-new-message-input/form/bs-square-button')
            comment_button.click()
            print(Fore.LIGHTBLUE_EX, 'Отправил этот комментарий!')
            time.sleep(random.randrange(5, 15))

            self.open_profile()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось отправить комментарий, открываю профиль')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_profile()

    def open_profile(self):
        """Открывает профиль"""

        try:
            go_to_the_profile = self.browser.find_element(By.XPATH,
                                                          '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[2]/mp-caption-figure-template[2]/a')
            go_to_the_profile.click()
            print(Fore.GREEN, u'Открыл профиль, сейчас посмотрим, что тут у нас😑')
            time.sleep(random.randrange(15, 25))

            self.subscription()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть профиль, запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def subscription(self):
        """Подписывается на пользователя"""

        try:
            follow_button = self.browser.find_element(By.XPATH,
                                                      '/html/body/mp-root/div/div/ng-component/ng-component/mp-wrapper-member-profile-content/main/bs-container-grid/mp-profile-header/mp-profile-visitor-actions/div/mp-button-follow-text-template/mp-button-item-action-text-template')
            follow_button.click()
            print(Fore.LIGHTGREEN_EX, 'Оформил', Fore.LIGHTBLUE_EX, 'подписку')
            time.sleep(random.randrange(5, 15))

            self.back()
            self.open_liked()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Подписаться не получилось, нажимаю кнопку "Назад".')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.back()

    def back(self):
        """Нажимает на кнопку 'Назад' в браузере"""

        try:
            self.browser.back()
            print(Fore.GREEN, 'Нажал на кнопку "Назад"')
            time.sleep(random.randrange(10, 15))

        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось нажать на кнопку "Назад", запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def close_menu(self):
        """Закрывает меню с лайнкувшими"""

        try:
            self.browser.find_element(By.CSS_SELECTOR, '.close-button').click()
            print('Закрыл меню с лайкнувшими')
            time.sleep(random.randrange(2, 4))
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось закрыть меню, запускаю алгоритм подписки на лайкнувших.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.cycle_to_liked()

    def open_liked(self):
        """Открывает меню с лайкнувшими"""
        try:
            likes = self.browser.find_element(By.XPATH,
                                              '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-like-action-template/mp-button-item-action-icon-template/span')
            likes.click()
            print(Fore.GREEN, 'Открыл меню с лайкнувшими!')
            time.sleep(random.randrange(7, 15))

            self.parsing()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть меню лайкнувших, запускаю цикл заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def parsing(self):
        """Парсит ссылки на тех, кто лайкнул бит"""

        try:

            # ищет элементы только в окне с теми, кто лайкнул бит
            window_with_liked = self.browser.find_element(By.CLASS_NAME, 'body-container')

            # ищет элементы с тегом "а"
            elements = window_with_liked.find_elements(By.TAG_NAME, 'a')

            # собирает ссылки на элементы только 'href'
            self.profile_urls = [item.get_attribute('href') for item in elements]
            print(Fore.LIGHTCYAN_EX, 'Спарсил ссылки на профили: ', Fore.LIGHTYELLOW_EX, self.profile_urls)

            self.close_menu()
            self.like()
        except Exception as ex:
            print(Fore.LIGHTRED_EX,
                  'Не получилось спарсить пользователей, которые лайкнули бит, запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def cycle_to_liked(self):
        """Запускает цикл подписки на лайкнувших"""

        try:
            for self.profile_url in self.profile_urls[0:random.randrange(5, 15)]:
                self.browser.get(self.profile_url)
                time.sleep(random.randrange(10, 15))

                self.subscription_to_liked()
        except Exception as ex:
            print(Fore.LIGHTRED_EX,
                  'Не получилось запустить цикл подписки на пользователей, которые лайкнули бит, запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def subscription_to_liked(self):
        """Подписывается на лайкнувших"""

        try:

            follow_button = self.browser.find_element(By.XPATH,
                                                      '/html/body/mp-root/div/div/ng-component/ng-component/mp-wrapper-member-profile-content/main/bs-container-grid/mp-profile-header/mp-profile-visitor-actions/div/mp-button-follow-text-template/mp-button-item-action-text-template')
            follow_button.click()
            print(Fore.LIGHTGREEN_EX, 'Оформил', Fore.LIGHTBLUE_EX, 'подписку', Fore.LIGHTGREEN_EX, 'на:',
                  Fore.LIGHTYELLOW_EX, self.profile_url)

            time.sleep(random.randrange(30, 45))
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось подписаться на "', self.profile_url, '", подписываюсь на следующего пользователя.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            time.sleep(10)

    def close_beatstars(self):
        """Открывает страницу гугл, якобы для закрытия битстарса"""

        self.browser.get('https://google.com/')
        print(Fore.LIGHTYELLOW_EX, 'Бот закрыл битстарс')

    def sleep(self):
        """Рандомизирует переменные сна"""

        self.sleep_1_cycle = random.randrange(3500, 5500)
        self.sleep_day_cycle = random.randrange(27000, 40000)

    def repost_beat(self):
        """Делает репост моих битов"""
        try:
            self.browser.get('https://www.beatstars.com/flipsidebeats/tracks')
            time.sleep(random.randrange(30, 40))

            self.browser.find_element(By.XPATH,
                                      '/html/body/mp-root/div/div/ng-component/ng-component/mp-search-v3/div/div/section/mp-search-results/mp-list-card-track/div/mp-list-card-template/div/mp-card-figure-track[1]/mp-card-figure-template/figure/div/div[2]/div[2]/mp-button-play-track-on-algolia-v3/bs-vb-button-play-item').click()
            time.sleep(random.randrange(3, 5))

            for i in range(0, random.randrange(3, 10)):
                # открывает описание бита
                self.browser.find_element(By.XPATH,
                                          '//*[@id="player-container"]/div/div[1]/div[1]/bs-playable-item-info/div[2]/div[1]/a').click()
                print(Fore.GREEN, 'Открыл описание бита')
                time.sleep(random.randrange(15, 20))

                # нажимает на кнопку репоста (2 раза)
                self.browser.find_element(By.XPATH,
                                          '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[1]/section/mp-member-content-item-header-template/div[4]/mp-button-repost-icon-template/mp-button-item-action-icon-template/button').click()
                time.sleep(random.randrange(2, 4))
                print(Fore.LIGHTBLUE_EX, 'Сделал репост')

                # переключает на следующий бит
                self.browser.find_element(By.XPATH,
                                          '/html/body/mp-root/mp-player-wrapper/bs-player/div/div/div[2]/bs-player-next/button').click()
                print(Fore.CYAN, 'Переключился на следующий бит')
                time.sleep(random.randrange(5, 10))
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось сделать репост')
            print(Fore.RED, 'Описание ошибки: ', ex)
            time.sleep(10)

    def start_bot(self):
        """Запускает бота в цикл"""

        start_bot = True
        self.oauth_beatstars()

        while start_bot:
            """Бесконечный цикл"""

            self.sleep()

            for main_cycle in range(0, 1):
                """Выполняется 1 раз в день, засыпает на 8-12 часов"""

                self.sleep()
                self.repost_beat()

                for self.number in range(0, random.randrange(4, 6)):

                    """Выполняется 3, 7 раз в день, каждый раз засыпает на 1-1,5 часа"""

                    self.sleep()

                    for i in range(0, random.randrange(10, 16)):
                        """Сам цикл, выполняется 4-7 раз за 1 цикл"""

                        print(Fore.LIGHTMAGENTA_EX, 'Цикл №', i + 1, 'начал свою работу!')
                        self.open_feed()
                        print(Fore.LIGHTMAGENTA_EX, 'Цикл №', i + 1, 'успешно завершён! Продолжаем..')
                        time.sleep(random.randrange(5, 15))

                    self.close_beatstars()
                    print(Fore.LIGHTMAGENTA_EX, 'Циклы завершены. Боту нужно немного отдохнуть...'
                                                'Он продолжит работу через', Fore.LIGHTRED_EX, self.sleep_1_cycle, Fore.LIGHTMAGENTA_EX, 'секунд!')
                    time.sleep(self.sleep_1_cycle)

                self.repost_beat()
                print(Fore.LIGHTYELLOW_EX, 'Бот провёл', self.number, 'циклов за день!')
            print(Fore.LIGHTMAGENTA_EX, 'Боту тоже нужен сон!'
                  'Он проснётся через', Fore.LIGHTRED_EX, self.sleep_day_cycle, Fore.LIGHTMAGENTA_EX, 'секунд')
            time.sleep(self.sleep_day_cycle)


print(Fore.LIGHTYELLOW_EX, 'Введите логин: ')
username = input()

print(Fore.LIGHTYELLOW_EX, 'Введите пароль: ')
password = input()

BS_bot = Beatstars_Bot(username, password)
BS_bot.start_bot()

# запускает многопоточность
#
#
# второй класс
# login_browser_2 = Authorization(username2, password2)
#
# функция первого класса
# def login_browser1():
#     login_browser_1.start()
#
# функция второго класса
# def login_browser2():
#     login_browser_2.start()

# запускает многопоточность
# th = Thread(target = login_browser1, args = ())
# th.start()
# th2 = Thread(target = login_browser2, args = ())
# th2.start()
