from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from libs.loginin import login
logging.basicConfig(level=logging.INFO)


name = '设备界面的增删改查'



def machine_add(model, description, types):

    # 检查参数
    if not all([model,description,types]):
        raise ValueError("model / description / types 中存在空值")

    wd = login()

    # 点击设备型号界面
    wd.find_element(By.CSS_SELECTOR,'a[href="#/devicemodel"]').click()

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
        assert lists[0].text == symbol.text
        assert lists[1].text == model
        assert lists[2].text == description
        logging.info("添加设备型号成功")
    except AssertionError:
        # 截图保存有利于查看Error
        wd.save_screenshot("error.png")
        logging.error("模型名称断言失败", exc_info=True)
        raise
    wd.quit()
    return f"添加成功: {model} - {description} - {types}"

def machine_change(modeltext, description):

    if not all([modeltext, description]):
        raise ValueError("modeltext / description 中存在空值")

    wd = login()

    # 点击设备型号界面
    wd.find_element(By.CSS_SELECTOR,'a[href="#/devicemodel"]').click()

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

    sleep(1)

    newmodeltext = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[2]/span[@class="field-value"]')
    newdescription = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]')

    try:
        assert modeltext == newmodeltext.text
        assert description == newdescription.text
    except AssertionError:
        # 截图保存有利于查看Error
        wd.save_screenshot("error.png")
        logging.error("模型名称断言失败", exc_info=True)
        raise
    wd.quit()
    return f"修改成功: {modeltext} - {description}"

def machine_delete():

    wd = login()

     # 点击设备型号界面
    wd.find_element(By.CSS_SELECTOR,'a[href="#/devicemodel"]').click()

    locator = (By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]')
    WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(locator))

    oldmodeltext = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]').text
    wd.find_element(By.CSS_SELECTOR,'.result-list-item-btn-bar>.btn-no-border').click()
    notice = wd.switch_to.alert.text
    wd.switch_to.alert.accept()

    WebDriverWait(wd,10,0.5).until(EC.visibility_of_element_located(locator))
    newmodeltext = wd.find_element(By.XPATH,'//div[@class="result-list-item-info"]/*[3]/span[@class="field-value"]').text

    try:
        assert notice == '确定要删除本记录吗？'
        assert oldmodeltext != newmodeltext
    except AssertionError:
        # 截图保存有利于查看Error
        wd.save_screenshot("error.png")
        logging.error("模型名称断言失败", exc_info=True)
        raise
    wd.quit()
    return f"删除成功: {oldmodeltext} - {newmodeltext}"



