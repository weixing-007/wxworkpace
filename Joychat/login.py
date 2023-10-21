# !/usr/bin/env python
# -*-coding:utf-8 -*-


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

desire = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "vivo",
    "noReset": True,
    "appPackage": "com.foreverht.workplus.hcbmpre",
    "automationName": "UiAutomator2",
    "appActivity": "com.foreveross.atwork.modules.main.activity.SplashActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire)

# 用户登录账号
# userlog = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/et_login_username_EditText")
# password = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/et_login_password")
# # password = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/password_input_layout")
# loginButton = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/login_login_button")
# switch = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/switch_account")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(switch))

# driver.find_element(*switch).click()
# # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(userlog))
# driver.find_element(*userlog).send_keys("uf101538")
# driver.find_element(*password).send_keys("yxxy7684")
# sleep(1)
# driver.find_element(*loginButton).click()
# sleep(6)
# print("登录成功")
# driver.quit()

# passw = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/password_input_layout")
# sub = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/login_button")
#
# switch = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/switch_account")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(switch))
#
# driver.find_element(*switch).click()
# sleep(3)
# driver.quit


btnlogin = (MobileBy.ID, "com.foreverht.workplus.hcbmpre:id/login_login_button_did")
didlog = (MobileBy.XPATH, "//*[contains(@text,'WebEAM登录')]")
didname = (MobileBy.XPATH, "//*[contains(@text,'请输入账号')]")
diduser = (MobileBy.ID, "new_username")
didpass = (MobileBy.ID, "new_SMSpassword")
didcode = (MobileBy.ID, "new_SMScode")
didsmslogin = (MobileBy.ID, "new_smsLogin")

#new_username/new_SMSpassword/new_SMScode/new_smsLogin
#new_sendsms  验证码
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(btnlogin))
driver.find_element(*btnlogin).click()
sleep(6)

try:
    log = driver.find_element(*didlog).text
except:
    print("哦吼！没有找到哦")
    sleep(2)
    driver.quit()
else:
    print("找到了:{}".format(log))

    # driver.find_element(*diduser).click()
    # driver.find_element(*diduser).send_keys("uf101538")
    # driver.find_element(*didpass).send_keys("12345678")
    # driver.find_element(*didcode).send_keys("123456")
    driver.find_element(*didsmslogin).click()





