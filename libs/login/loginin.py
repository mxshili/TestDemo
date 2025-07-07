from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




class login:

    def loginin(self,username = 'byhy',password = 'sdfsdf'):

        wd = webdriver.Edge()
        wd.implicitly_wait(10)

        wd.get('http://127.0.0.1:8234/login.html')
        if username == 'byhy' and password == 'sdfsdf':
            return None

        if username is not None:
            wd.find_element(By.ID,'username').send_keys(username)

        if password is not None:
            wd.find_element(By.ID,'password').send_keys(password)

        wd.find_element(By.CSS_SELECTOR,'button[id="loginBtn"]').click()


        WebDriverWait(wd,10,1).until(lambda el:wd.switch_to.alert.text)

        alerttext = wd.switch_to.alert.text

        return alerttext