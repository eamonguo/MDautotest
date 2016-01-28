# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
#from selenium.webdriver.common.action_chains import ActionChains
# import win32api
# import win32con
import time, re
#import pdb
#from pywinauto import application
import Config

class Login:
    def __init__(self):
        self.driver = Config.driver
        
    # 登录
    def login(self):
        driver = self.driver
        name1 = Config.loginname               #获取登录名
        password = Config.password             #获取密码
        base_url = Config.base_url             #获取链接
        driver.get(base_url + "/login.htm")
        driver.maximize_window()                #浏览器最大化
        time.sleep(1)
        try:
            driver.find_element_by_id("txtMobilePhone").clear()         #清空手机号输入
            driver.find_element_by_id("txtMobilePhone").send_keys(name1)
            driver.find_element_by_css_selector("span.passwordNotice").click()
            driver.find_element_by_id("txtPassword").clear()
            driver.find_element_by_id("txtPassword").send_keys(password)  #输入密码
            driver.find_element_by_id("btnLogin").click()                 #点击登录
            time.sleep(3)
            netname = driver.find_element_by_css_selector("span.overflow_ellipsis.Left").text    #获取网络名称
            driver.find_element_by_css_selector("span.overflow_ellipsis.Left").click()            #选择网络
            time.sleep(10)
            netresult = driver.find_element_by_css_selector("[class=\"companyName\"]").text       #获取登录成功的网络名
            if netname == netresult:                  #判断登录网络是否正确
                loginresult = "PASS"
            else:
                loginresult = "FAIL"
        except:
            loginresult = "DONE"  
        return loginresult
