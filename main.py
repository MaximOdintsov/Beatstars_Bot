import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from comments import list

from threading import Thread

from database import username, password, username2, password2

from colorama import Fore, Back, Style

list_comments = None

url = None


class Beatstars_Bot():
    """Класс работы бота"""

    def __init__(self, username, password):
        """Переменные для входа в аккаунт"""

        self.username = username
        self.password = password
        self.browser = webdriver.Firefox()
        print(Fore.LIGHTMAGENTA_EX, 'БОТ НАЧАЛ АВТОРИЗАЦИЮ')
        # АВТОРИЗАЦИЯ

    def oauth_beatstars(self):
        """Открывает страницу авторизации в битстарс"""

        try:
            self.browser.get('https://oauth.beatstars.com/')
            print(Fore.LIGHTWHITE_EX, Back.BLACK, 'Открыл битстарс')
            time.sleep(random.randrange(5, 15))

            self.input_username()
        except:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть битстарс, запускаю авторизацию заново')
            time.sleep(10)
            self.oauth_beatstars()

    def input_username(self):
        """Вводит имя пользователя"""

        try:
            username_input = self.browser.find_element(By.ID, 'input-username')
            username_input.click()
            time.sleep(random.randrange(5, 10))
            # вводим юзернейм с клавиатуры (в будущем заменить на код из JS)
            pyautogui.typewrite(username)
            print(Fore.WHITE, ' Ввёл логин')
            time.sleep(random.randrange(1, 3))

            self.input_password()
        except:
            print(Fore.LIGHTRED_EX, 'Не получилось ввести имя пользователя, запускаю авторизацию заново')
            time.sleep(10)
            self.oauth_beatstars()

    def input_password(self):
        """Вводит пароль"""

        try:
            password_input = self.browser.find_element(By.ID, 'input-password')
            password_input.click()
            time.sleep(random.randrange(5, 10))
            # вводим пароль с клавиатуры (в будущем заменить на код из JS)
            pyautogui.typewrite(password)
            print(Fore.WHITE, ' Ввёл пароль')
            time.sleep(random.randrange(1, 3))

            self.login_button()
        except:
            print(Fore.LIGHTRED_EX, 'Не получилось ввести пароль, запускаю авторизацию заново')
            time.sleep(10)
            self.oauth_beatstars()

    def login_button(self):
        """Нажимает на кнопку 'Войти' """

        try:
            login_button = self.browser.find_element(By.XPATH,
                                                     '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/bs-square-button/button')
            login_button.click()
            print(Fore.LIGHTWHITE_EX, ' Вошёл в аккаунт')
            time.sleep(random.randrange(40, 45))

            self.consent_to_cookies()
        except:
            print(Fore.LIGHTRED_EX, 'Не получилось нажать на кнопку "Войти", запускаю алгоритм заново')
            time.sleep(10)
            self.oauth_beatstars()

    def consent_to_cookies(self):
        """Нажимает на кнопку 'Согласиться с куки' """

        try:
            cookie_consent = self.browser.find_element(By.XPATH,
                                                       '/html/body/mp-root/mp-snackbar-info-messages/div/mp-cookies-snackbar/mp-snackbar-info-message-template/div/button')
            cookie_consent.click()
            print(Fore.WHITE, ' Согласился с cookie')
            time.sleep(random.randrange(2, 4))
        except:
            print(Fore.LIGHTRED_EX, 'Не получилось согласиться с куки, открываю эту страницу заново')
            time.sleep(10)
            self.homepage()

    def homepage(self):
        """Открывает начальную страницу битстарс"""

        try:
            self.browser.get('https://beatstars.com/')
            print(Fore.WHITE, 'Открыл начальную страницу, т.к. не получилось согласиться с куки')
            time.sleep(random.randrange(5, 15))

            self.consent_to_cookies()
        except:
            print(Fore.LIGHTRED_EX, 'Снова не получилось согласиться с куки, запускаю алгоритм заново')
            self.close_beatstars()
            time.sleep(10)
            self.oauth_beatstars()
            # ОСНОВНАЯ РАБОТА БОТА

    def open_feed(self):
        """Открывает фид"""

        try:
            self.browser.get('https://www.beatstars.com/feed')
            print(Fore.LIGHTMAGENTA_EX, ' БОТ НАЧАЛ РАБОТУ!')
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

            self.like()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось открыть описание бита, запускаю алгорит заново')
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

            self.comments()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось поставить лайк, пишу комментарий.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.comments()

    def comment(self):
        """Определяет рандомный комментарий"""

        global list_comments

        list_comments = random.choice(list)

    def comments(self):
        """Печатает и отправляет комментарии"""

        try:
            self.comment()

            # нажимает на поле ввода и вписывает рандомный комментарий
            input_comments = self.browser.find_element(By.XPATH,
                                                       '/html/body/mp-root/div/div/ng-component/mp-wrapper-member-track-content/mp-member-content-item-template/bs-container-grid/div[3]/div[2]/mp-comments-panel-box/mp-open-close-panel-template/div/article/div[2]/mp-create-new-comment-input/mp-musician-autocomplete-wrapper/mp-autocomplete-dropdown-template/div/div[2]/mp-compose-new-message-input/form/div[2]/input')
            time.sleep(random.randrange(5, 10))
            input_comments.send_keys(list_comments)
            print(Fore.LIGHTGREEN_EX, "Ввёл", Fore.LIGHTBLUE_EX, " комментарий:\n", Fore.LIGHTYELLOW_EX, list_comments)

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
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Подписаться не получилось, нажимаю кнопку "Назад".')
            print(Fore.RED, 'Описание ошибки: ', ex)

            # хз, оставить или нет
            self.back()

    def back(self):
        """Нажимает на кнопку 'Назад' в браузере"""

        try:
            self.browser.back()
            time.sleep(random.randrange(10, 15))
            print(Fore.GREEN, 'Нажал на кнопку "Назад"')

            self.open_liked()
        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось нажать на кнопку "Назад", запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

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

            self.cycle_to_liked()

        except Exception as ex:
            print(Fore.LIGHTRED_EX,
                  'Не получилось спарсить пользователей, которые лайкнули бит, запускаю алгоритм заново.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            self.open_feed()

    def cycle_to_liked(self):
        """Запускает цикл подписки на лайкнувших"""

        global url

        try:
            for url in self.profile_urls:
                self.browser.get(url)
                time.sleep(random.randrange(10, 15))
                # func
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
            print(Fore.LIGHTGREEN_EX, 'Оформил', Fore.LIGHTBLUE_EX, 'подписочку', Fore.LIGHTGREEN_EX, 'на:',
                  Fore.LIGHTYELLOW_EX, url)

            time.sleep(random.randrange(30, 45))

        except Exception as ex:
            print(Fore.LIGHTRED_EX, 'Не получилось подписаться на "', url,
                  '", подписываюсь на следующего пользователя.')
            print(Fore.RED, 'Описание ошибки: ', ex)
            time.sleep(10)

    def close_beatstars(self):
        """Открывает страницу гугл, якобы для закрытия битстарса"""

        self.browser.get('https://google.com/')
        print(Fore.LIGHTYELLOW_EX, 'Бот закрыл битстарс')

    def sleep(self):
        """Рандомизирует переменные сна"""

        # global sleep_1_cycle
        # global sleep_day_cycle

        self.sleep_1_cycle = random.randrange(3500, 5500)
        self.sleep_day_cycle = random.randrange(30000, 45000)

    def start_bot(self):
        """Запускает бота в цикл"""

        start_bot = True

        self.oauth_beatstars()

        while start_bot:
            """Бесконечный цикл"""

            self.sleep()

            for o in range(1, 2):
                """Выполняется 1 раз в день, засыпает на 8-12 часов"""

                self.sleep()

                for number in range(1, random.randrange(4, 8)):
                    """Выполняется 4, 6 раз в день, каждый раз засыпает на 1-1,5 часа"""

                    self.sleep()

                    for i in range(1, random.randrange(5, 8)):
                        """Сам цикл, выполняется 3-7 раз за 1 цикл"""

                        self.open_feed()
                        print(Fore.LIGHTMAGENTA_EX, 'Цикл №', i, 'успешно завершён! Продолжаем..')
                        time.sleep(random.randrange(5, 20))

                    self.close_beatstars()
                    print(Fore.LIGHTMAGENTA_EX, 'Цикл №', number, 'завершён. Бот продолжит работу через',
                          Fore.LIGHTRED_EX, self.sleep_1_cycle, Fore.LIGHTMAGENTA_EX, 'секунд!')
                    time.sleep(self.sleep_1_cycle)

            self.close_beatstars()
            print(Fore.LIGHTMAGENTA_EX, 'Бот полностью завершил свою работу. Он проснется через', Fore.LIGHTRED_EX,
                  self.sleep_day_cycle, Fore.LIGHTMAGENTA_EX, 'секунд')
            time.sleep(self.sleep_day_cycle)


BS_bot = Beatstars_Bot(username, password)
BS_bot.start_bot()