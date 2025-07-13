import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from cases.business_rule.test_business_rule import browser
from libs.loginin import login
logging.basicConfig(level=logging.INFO)
import pytest



class business:

    name = '业务规则添加'

    def test_service_rule_type1(ruleName, minConsume, estimateConsume, measurement,
                                measurePrice, description, types, browser):
            # 选择类型
            wd = browser
            wd.find_element(By.XPATH,'//ul[@class="side-menu"]//li[@class="menu-item"]//a[@href="#/svcrule"]').click()
            wd.find_element(By.XPATH,'//div[@class="add-one-area"]/span').click()
            Select(wd.find_element(By.ID,'rule_type_id')).select_by_value(types)
            select = Select(wd.find_element(By.ID,'rule_type_id')).all_selected_options

            inputs = wd.find_elements(By.XPATH,'//div[@class="add-one-area"]//input')
            inputs[0].send_keys(ruleName)
            inputs[1].send_keys(minConsume)
            inputs[2].send_keys(estimateConsume)
            inputs[3].send_keys(measurement)
            inputs[4].send_keys(measurePrice)
            inputs[5].send_keys(description)


            wd.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div .btn').click()

            WebDriverWait(wd,10,0.5).until(lambda el:wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value'))

            newinputs = wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value')
            subnewinputs = wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .sub-field-value')

            length = len(subnewinputs[0].text)
            selecttext = subnewinputs[0].text[3:length-1]
            selecttextprice = subnewinputs[1].text

            try:
                assert newinputs[0].text == ruleName
                assert newinputs[1].text == select[0].text
                assert selecttext == measurement
                assert selecttextprice[3:] == measurePrice
                assert newinputs[3].text == minConsume
                assert newinputs[4].text == estimateConsume
                assert newinputs[5].text == description
            except AssertionError:
                wd.save_screenshot("error.png")
                logging.error("模型名称断言失败", exc_info=True)
                raise

            return f"添加成功: {ruleName}-{minConsume}-{estimateConsume}-{measurement}-{measurePrice}-{description}-{types}"

    def test_service_rule_type2(ruleName, minConsume, estimateConsume, description, types, browser):

            wd = browser
            # 选择类型
            wd.find_element(By.XPATH,'//ul[@class="side-menu"]//li[@class="menu-item"]//a[@href="#/svcrule"]').click()
            wd.find_element(By.XPATH,'//div[@class="add-one-area"]/span').click()
            Select(wd.find_element(By.ID,'rule_type_id')).select_by_value(types)
            select_options = Select(wd.find_element(By.ID,'rule_type_id')).all_selected_options

            # 输入数据
            inputs = wd.find_elements(By.XPATH,'//div[@class="add-one-area"]//input')
            inputs[0].send_keys(ruleName)
            inputs[1].send_keys(minConsume)
            inputs[2].send_keys(estimateConsume)
            inputs[3].send_keys(description)

            wd.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div .btn').click()

            sleep(1)

            newinputs = wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value')

            try:
                assert newinputs[0].text == ruleName
                assert newinputs[1].text == select_options[0].text
                assert newinputs[3].text == minConsume
                assert newinputs[4].text == estimateConsume
                assert newinputs[5].text == description
            except AssertionError:
                wd.save_screenshot('error.png')
                logging.error('模型断言失败',exc_info=True)

            return f"添加成功: {ruleName}-{minConsume}-{estimateConsume}-{description}-{types}"


    def test_service_rule_type3(ruleName,businesscode,measurement,measurePrice,description,types,browser):


            wd = browser

            wd.find_element(By.XPATH,'//ul[@class="side-menu"]//li[@class="menu-item"]//a[@href="#/svcrule"]').click()
            wd.find_element(By.XPATH,'//div[@class="add-one-area"]/span').click()
            # 选择类型
            Select(wd.find_element(By.ID,'rule_type_id')).select_by_value(types)
            select_options = Select(wd.find_element(By.ID,'rule_type_id')).all_selected_options

    # 选择类型
            inputs = wd.find_elements(By.XPATH,'//div[@class="add-one-area"]//input')
            inputs[0].send_keys(ruleName)
            inputs[1].send_keys(businesscode)
            inputs[2].send_keys(measurement)
            inputs[3].send_keys(measurePrice)
            inputs[4].send_keys(description)

            # 点击确定提交
            wd.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div .btn').click()

            # 显示等待
            try:
                WebDriverWait(wd,10,0.5).until(lambda el:wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value'))
            except TimeoutError:
                wd.quit()

            newinputs = wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value')
            subnewinputs = wd.find_elements(By.CSS_SELECTOR,'.result-list-item:nth-child(1) .sub-field-value')

            length1 = len(subnewinputs[1].text)

            try:
                assert newinputs[0].text == ruleName
                assert newinputs[1].text == select_options[0].text
                assert newinputs[3].text == description
                assert subnewinputs[0].text[4:] == businesscode
                assert subnewinputs[1].text[3:length1-1] == measurement
                assert subnewinputs[2].text[3:] == measurePrice
            except AssertionError:
                wd.save_screenshot('error.jpg')
                logging.error("模型名称断言失败", exc_info=True)

            return f"添加成功: {ruleName}-{businesscode}-{measurement}-{measurePrice}-{description}-{types}"
