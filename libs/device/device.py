import logging

from libs.loginin import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




name = '设备添加'

def testdevice(types,modeltypes,ruletypes,machinenumber,description):

    wd = login()
    # 进入设备界面
    wd.find_element(By.CSS_SELECTOR,'a[href="#/device"]').click()
    wd.find_element(By.CLASS_NAME,'btn').click()
    # 输入需要添加的数据
    selecttypes = Select(wd.find_element(By.ID,'device-type'))
    selecttypes.select_by_value(types)
    selectTypes = selecttypes.all_selected_options

    selectmodeltypes = Select(wd.find_element(By.ID,'device-model'))
    selectmodeltypes.select_by_value(modeltypes)
    selectmodelTypes = selectmodeltypes.all_selected_options

    selectruletypes = Select(wd.find_element(By.ID,'svc-rule-id'))
    selectruletypes.select_by_value(ruletypes)
    selectruleTypes = selectruletypes.all_selected_options

    wd.find_element(By.ID,'device-sn').send_keys(machinenumber)
    wd.find_element(By.ID,'device-desc').send_keys(description)
    wd.find_element(By.XPATH,'//div[@class="add-one-submit-btn-div"]/span').click()


    # 断言验证 显式验证
    # WebDriverWait(wd,10,0.5).until(lambda el:wd.find_elements(By.CSS_SELECTOR,'.result-list-item-info .field-value'))
    locator = (By.CSS_SELECTOR,'.result-list-item:nth-child(1) .field-value')
    WebDriverWait(wd,10,0.5).until(EC.visibility_of_all_elements_located(locator))

    fields = wd.find_elements(By.CSS_SELECTOR,'.result-list-item-info .field-value')

    try:
      assert fields[0].text == selectTypes[0].text
      assert fields[1].text == selectmodelTypes[0].text
      assert fields[2].text == machinenumber
      assert fields[4].text == selectruleTypes[0].text
      assert fields[5].text == description
    except AssertionError:
        wd.save_screenshot('error.png')
        logging.error("模型名称断言失败", exc_info=True)

    wd.quit()
    return f"添加成功: {types}-{modeltypes}-{ruletypes}-{machinenumber}-{description}"