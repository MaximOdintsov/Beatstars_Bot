import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from database import login, password


browser = webdriver.Chrome()
browser.get('https://oauth.beatstars.com/')
time.sleep(15)

# auth_button = browser.find_element(By.XPATH, '/html/body/oauth-root/ng-component/section/div[2]/div[2]/div/div/button[4]').click()
# time.sleep(100)

# login_input = browser.find_element_by_css_selector()
# login_input.clear()
# login_input.send_keys('flipsidebeats')
# time.sleep(10)

login_input = browser.find_element(By.ID, "input-username")
login_input.send_keys('login')
time.sleep(10)

# '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/div[1]/bs-text-input/input'
# //*[@id="input-username"]

# password_input = browser.find_element(By.NAME, '/html/body/oauth-root/ng-component/section/div[2]/div[2]/form/div[2]/bs-text-input/input')
# password_input.clear()
# password_input.send_keys(password)
# time.sleep(10)


# listen_button = browser.find_element(By.XPATH, '/html/body/mp-root/div/div/ng-component/mp-feed/div/section[2]/div[1]/mp-track-post/mp-feed-card/div/div[2]/div[1]/div[2]/div[1]/bs-button-play-item/button').click()
# time.sleep(10)
#
# next_listen_button = browser.find_element(By.XPATH, '/html/body/mp-root/mp-player-wrapper/bs-player/div/div/div[2]/bs-player-next/button').click()
# time.sleep(100)



browser.close()
browser.quit()