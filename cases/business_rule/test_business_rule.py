from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from libs.business_rule import business_rule_update, business_rule

import pytest


@pytest.fixture(scope="class")
def browser():
    """初始化浏览器、登录系统并跳转界面"""
    wd = webdriver.Edge()
    wd.implicitly_wait(10)
    wd.get('http://127.0.0.1:8234/login.html')
    wd.find_element(By.ID,'username').send_keys('byhy')
    wd.find_element(By.ID,'password').send_keys('sdfsdf')
    wd.find_element(By.CSS_SELECTOR,'button[id="loginBtn"]').click()
    sleep(1)

    yield wd

    wd.quit()




class TestBusinessRule:

    name = '业务规则'

    @pytest.mark.parametrize('ruleName,minConsume,estimateConsume,measurement,measurePrice,description,types',[
        ('全国-电瓶车充电费率1','0.1','2','千瓦时','1','','1')
    ],scope='function')
    def test_business_rule1(self,ruleName,minConsume,estimateConsume,
                            measurement,measurePrice,description,types,browser):

        business_rule_update.business.test_service_rule_type1(ruleName, minConsume, estimateConsume,
                                              measurement, measurePrice, description, types, browser)


    @pytest.mark.parametrize('ruleName,minConsume,estimateConsume,description,types',[
        ('南京-洗车机费率1','2','10','','2')
    ],scope='function')
    def test_business_rule2(self,ruleName,minConsume,
                            estimateConsume,description,types,browser):


        business_rule_update.business.test_service_rule_type2(
            ruleName,minConsume,estimateConsume,description,types,browser)


    @pytest.mark.parametrize('ruleName,businesscode,measurement,measurePrice,description,types',[
            ('南京-存储柜费率1','业务码100L','小时','2','','3')
        ],scope='function')
    def test_business_rule3(self,ruleName,businesscode,measurement,
                            measurePrice,description,types,browser):

        business_rule_update.business.test_service_rule_type3(
            ruleName,businesscode,measurement,measurePrice,description,types,browser)






