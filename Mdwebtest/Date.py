# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re
import Funtion
import Config

class Date:
    def __init__(self):
        self.driver = Config.driver
        
    def date_move(self):
        driver = self.driver
        driver.get(Config.base_url + "/apps/calendar/home")
        time.sleep(3)
        #driver.find_element_by_link_text(u"日程").click()

    # 新建日程        
    def date_newdate(self):
        driver = self.driver
        member = Config.member
        global datename
        try:
            driver.find_element_by_xpath(u"//button[@type='button' and text()=\"列表\"]").click()
            time.sleep(2)
            driver.find_element_by_xpath(u"//div[@id=\"addNewClaendar\" and text()=\"新日程\"]").click()
            datename = u"新建一个" + time.ctime()
            time.sleep(3)
            Funtion.datedata(datename,*member)
            time.sleep(3)
            try:
                driver.find_element_by_css_selector("[class='icon-task-status-complete']")
                dnd = "PASS"
                #driver.find_element_by_css_selector("span.dialogCloseBtn.icon-task-delete").find_element_by_xpath("..").click()
                for i in range(0,10):
                    try:
                        driver.find_element_by_css_selector("[class='icon-task-status-complete']")
                        driver.find_element_by_css_selector("span.dialogCloseBtn.icon-task-delete").click()
                        time.sleep(0.5)
                    except:
                        break
            except:
                dnd = "FAIL"
        except:
        	  dnd = "DONE"
        time.sleep(1)
        return dnd
         
    # 删除日程        
    def date_deldate(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//div[text()=\"" + datename + "\"]").click()
            time.sleep(2)
            driver.find_element_by_xpath("//div[@id='editBoxMain']/div/div/div[@class='right editOpertion pointer']/span").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//li[@class=\"deleteCalendar\" and text()=\"删除日程\"]").click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//div[text()=\"" + datename + "\"]")
                ddd = "FAIL"
            except:
                ddd = "PASS"
        except:
        	  ddd = "DONE"
        return ddd