from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from libs.loginin import login
logging.basicConfig(level=logging.INFO)

@pytest.fixture(scope="module")
def setup_browser():
    """初始化浏览器并登录系统"""
    wd = login()
    # 点击设备型号界面
    wd.find_element(By.CSS_SELECTOR,'a[href="#/devicemodel"]').click()
    yield wd
    wd.quit()

@pytest.fixture()
class machine(setup_browser()):

    name = '设备界面的增删改查'

    def machine_add(self,model, description, types):
        # 检查参数
        if not all([model,description,types]):
            raise ValueError("model / description / types 中存在空值")

        wd = setup_browser()

        addbutton = WebDriverWait(wd,10,0.5).until(
            lambda el:wd.find_element(By.CSS_SELECTOR,'.add-one-area>.btn'))
        # 找到添加按钮，选择并输入元素
        addbutton.click()

        select = Select(wd.find_element(By.ID,'device-type'))
        select.select_by_visible_text(types)
        symbols = select.all_selected_options

        wd.find_element(By.ID,'device-model').send_keys(model)
        wd.find_element(By.ID,'device-model-desc').send_keys(description)
        # 提交
        wd.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div>.btn').click()

        locator = (By.CSS_SELECTOR,'.result-list .field-value')
        WebDriverWait(wd,10,0.5).until(EC.visibility_of_all_elements_located(locator))
        # 断言比对
        lists = wd.find_elements(By.CSS_SELECTOR,'.result-list .field-value')

        symbol = symbols[0]

        try:
            assert lists[0].text == symbol.text,\
                f"提交值{lists[0].text}与添加值{symbol.text}不匹配"
            assert lists[1].text == model,\
                f"提交值{lists[1].text}与添加值{model}不匹配"
            assert lists[2].text == description,\
                f"提交值{lists[2].text}与添加值{description}不匹配"
            logging.info("添加设备型号成功")
            return f"添加成功: {model} - {description} - {types}"
        except AssertionError:
            # 截图保存有利于查看Error
            wd.save_screenshot("error.png")
            logging.error("模型名称断言失败", exc_info=True)
            raise


    def machine_change(self,modeltext, description):

        if not all([modeltext, description]):
            raise ValueError("modeltext / description 中存在空值")

        wd = setup_browser()

        locator = (By.XPATH,'//div[@class="result-list-item-btn-bar"]/*[2]')
        WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(locator))

        # 修改设备型号
        wd.find_element(By.XPATH,'//div[@class="result-list-item-btn-bar"]/*[2]').click()
        finds = wd.find_elements(By.XPATH,'//div[@class="result-list"]//input[@class="input-xl"]')
        finds[0].clear()
        finds[0].send_keys(modeltext)
        finds[1].clear()
        finds[1].send_keys(description)

        wd.find_element(By.CSS_SELECTOR,'.result-list-item-btn-bar .btn-no-border:nth-child(1)').click()

        WebDriverWait(wd,10,0.5).until(wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[2]/span[@class="field-value"]'))

        newmodeltext = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[2]/span[@class="field-value"]')
        newdescription = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]')

        try:
            assert modeltext == newmodeltext.text,\
                f"断言失败，修改值{modeltext}与提交值{newmodeltext.text}不符"
            assert description == newdescription.text,\
                f"断言失败，修改值{description}与提交值{newdescription.text}不符"
            return f"修改成功: {modeltext} - {description}"
        except AssertionError:
            # 截图保存有利于查看Error
            wd.save_screenshot("error.png")
            logging.error("模型名称断言失败", exc_info=True)
            raise


    def machine_delete(self):

        wd = setup_browser()

        locator = (By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]')
        WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(locator))

        modeltextpath = '//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]'

        oldmodeltext = wd.find_element(By.XPATH,modeltextpath).text
        wd.find_element(By.CSS_SELECTOR,'.result-list-item-btn-bar>.btn-no-border').click()

        WebDriverWait(wd,10,0.5).until(wd.switch_to.alert.text)

        notice = wd.switch_to.alert.text
        wd.switch_to.alert.accept()

        WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(locator))
        newmodeltext = wd.find_element(By.XPATH,modeltextpath).text

        try:
            assert notice == '确定要删除本记录吗？',\
            f"断言错误，{notice}不符"
            assert oldmodeltext != newmodeltext,\
            f"断言错误，{oldmodeltext}与{newmodeltext}相符，重新删除"
            return f"删除成功: {oldmodeltext} - {newmodeltext}"
        except AssertionError:
            # 截图保存有利于查看Error
            wd.save_screenshot("error.png")
            logging.error("模型名称断言失败", exc_info=True)
            raise



