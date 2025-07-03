import pytest
from libs.loginin import login
from selenium.webdriver.common.by import By




@pytest.fixture(scope="class")
def browser_add(login):
    """初始化浏览器、登录系统并跳转界面"""
    wd = login()

    wd.find_element(By.XPATH,'//ul[@class="side-menu"]//li[@class="menu-item"]//a[@href="#/svcrule"]').click()
    wd.find_element(By.XPATH,'//div[@class="add-one-area"]/span').click()

    yield wd

    wd.quit()