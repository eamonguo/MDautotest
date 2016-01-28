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
        
    # ��¼
    def login(self):
        driver = self.driver
        name1 = Config.loginname               #��ȡ��¼��
        password = Config.password             #��ȡ����
        base_url = Config.base_url             #��ȡ����
        driver.get(base_url + "/login.htm")
        driver.maximize_window()                #��������
        time.sleep(1)
        try:
            driver.find_element_by_id("txtMobilePhone").clear()         #����ֻ�������
            driver.find_element_by_id("txtMobilePhone").send_keys(name1)
            driver.find_element_by_css_selector("span.passwordNotice").click()
            driver.find_element_by_id("txtPassword").clear()
            driver.find_element_by_id("txtPassword").send_keys(password)  #��������
            driver.find_element_by_id("btnLogin").click()                 #�����¼
            time.sleep(3)
            netname = driver.find_element_by_css_selector("span.overflow_ellipsis.Left").text    #��ȡ��������
            driver.find_element_by_css_selector("span.overflow_ellipsis.Left").click()            #ѡ������
            time.sleep(10)
            netresult = driver.find_element_by_css_selector("[class=\"companyName\"]").text       #��ȡ��¼�ɹ���������
            if netname == netresult:                  #�жϵ�¼�����Ƿ���ȷ
                loginresult = "PASS"
            else:
                loginresult = "FAIL"
        except:
            loginresult = "DONE"  
        return loginresult
