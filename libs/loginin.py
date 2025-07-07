from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver


def login():
    wd = webdriver.Edge()
    wd.implicitly_wait(10)
    wd.get('http://127.0.0.1:8234/login.html')
    wd.find_element(By.ID,'username').send_keys('byhy')
    wd.find_element(By.ID,'password').send_keys('sdfsdf')
    wd.find_element(By.CSS_SELECTOR,'button[id="loginBtn"]').click()
    sleep(2)
    return wd