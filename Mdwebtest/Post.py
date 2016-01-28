# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con
import  time, re
import pdb
from pywinauto import application
#from Funtion import waitelement
from Funtion import upload
import Config
from Funtion import scrollbarmove

class Post:
    #messagenow = "null"
    def __init__(self,):
        self.driver = Config.driver
        
    # 通过链接进入动态
    def post_move(self):
        driver = self.driver
        driver.get(Config.base_url + "/feed")
        time.sleep(3)
    
    # 发送动态
    def post_send(self):
            driver = self.driver
        #driver.find_element_by_link_text(u"动态").click()

        #try:
            time.sleep(2)
            #编辑发送内容
            global messagenow
            messagenow = time.ctime()
#            print messagenow
            textarea = messagenow + u" @沈婕 "
            driver.find_element_by_id("textarea_Updater").clear()
            driver.find_element_by_id("textarea_Updater").send_keys(textarea) #输入发送内容
            #driver.find_element_by_id("textarea_Updater").click()
            time.sleep(2)
            
            
            
            # 文件上传开始
            for i in range(0,10):
                displayed = driver.find_element_by_xpath(u"//span[text()=\"本地文件\"]").is_displayed()
                if displayed == False:
                    driver.find_element_by_css_selector("a[data-targetdiv=\"#Attachment_updater\"]").click()
                    break
                else: 
                    time.sleep(3)
            
            for i in range(0,10):
                try:
                    time.sleep(2)
                    app = application.Application()
                    window = app.window_(class_name = "#32770")
                    break
                except:
                    driver.find_element_by_xpath(u"//span[text()=\"本地文件\"]").click()
                    time.sleep(3)
            
            '''
            a = driver.switch_to_alert() #获取对话框对象
            #a.send_keys('key') #alert/confirm对话框不能用
            b = a.text
            print b #得到文本值
            a.accept() #点击“确认”
#            a.dismiss() #点击“取消” 

            time.sleep(2)
            upid = driver.find_element_by_xpath("/html/body/div/input[@type=\"file\"]").get_attribute("id")
            print upid
            #driver.find_element_by_xpath("/html/body/div/input[@type=\"file\"]").click()         
            #displayed = driver.find_element_by_id(upid).is_displayed()
            displayed = driver.find_element_by_xpath("/html/body/div/input[@type=\"file\"]").is_displayed()
            print displayed
            #driver.find_element_by_id(upid).click()
            chain = ActionChains(driver)
            me = driver.find_element_by_link_text(u"动态")
            chain.move_to_element(me).perform()
            driver.find_element_by_xpath("/html/body/div/input[@type=\"file\"]").click()   
            #print upid
            '''
            upload(Config.pathway)
            time.sleep(1)
            for i in range(0,10):
                try:
                    driver.find_element_by_xpath("//span[text()='" + Config.uploadfilename + "']")
                    posup = "PASS"
                    break
                except:
                    posup = "FAIL"
                    time.sleep(2)
            print "pos_upload:" + posup
                    
            # 文件上传完成

            driver.find_element_by_css_selector("[class=\"icon-arrow-down-border Font14 Hand TxtMiddle\"]").click() #点击分享范围
            time.sleep(1)
            #js="var q=document.documentElement.scrollTop=300"
            #driver.execute_script(js)
            scrollbarmove("","300")
            driver.find_element_by_css_selector(u"label[title=\"我自己\"]").click()  #选择分享范围
            #js="var q=document.documentElement.scrollTop=0"
            scrollbarmove("","0")
            #driver.execute_script(js)
            time.sleep(3)                       
            driver.find_element_by_id("button_Share").click()  #点击分享
            time.sleep(3)
            try:  #验证动态是否发送成功
                #driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]")
                driver.find_element_by_xpath("//div[@class=\"postContentBody\"]/div[contains(text(),\"" + messagenow + "\")]")
                tst="PASS"
            except:
                tst="FAIL"
        #except:
            #tst = "DONE"
            return tst
    
    # 回复动态
    def post_reply(self):
        driver = self.driver
        try:
            time.sleep(2)
            #获取动态data-reactid
            idaa = driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]").get_attribute("data-reactid")    
            idab = idaa[0:54]
            idbb = idab + "1.4.2.0.0.0.0.0"
            messagenow1 = time.ctime() #回复动态的内容
            #页面移动到回复动态的地方-解决无法点击的问题
            chain = ActionChains(driver)
            me = driver.find_element_by_css_selector("[data-reactid=\"" + idbb + "\"]")
            chain.move_to_element(me).perform()
            driver.find_element_by_css_selector("[data-reactid=\"" + idbb + "\"]").send_keys(messagenow1) #输入回复动态内容
            idbc = idab + "1.4.2.0.1.0.3"
            driver.find_element_by_css_selector("[data-reactid=\"" + idbc + "\"]").click()  #点击回复
            time.sleep(2)
            for i in range(0,10):
                try:  #验证回复是否成功
                    driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[2]/div[1]/div[1]/div/ul/li[1]/div[2]/div/ul/li/div/div/div/span[contains(text(),\"" + messagenow1 + "\")]")
                    rtt="PASS"
                    break
                except:
                    rtt="FAIL"
                    time.sleep(1)
        except:
                rtt="DONE"
        return rtt
    
    # 删除动态
    def post_del(self):
        try:
            driver = self.driver
            idaa = driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]").get_attribute("data-reactid")    
            idab = idaa[0:54]
            idac = idab + "1.1.1.0.0"
            chain = ActionChains(driver)
            me = driver.find_element_by_id("textarea_Updater")
            chain.move_to_element(me).perform()
            driver.find_element_by_css_selector("[data-reactid=\"" + idac + "\"]").click()  #点击箭头
            idad = idab + "1.1.1.0.1.1.$=15:0.0.0.1"
            time.sleep(1)
            driver.find_element_by_css_selector("[data-reactid=\"" + idad + "\"]").find_element_by_xpath("..").click()
            time.sleep(1)
            driver.find_element_by_css_selector("[data-reactid=\"" + idad + "\"]").click()  #点击删除动态
            time.sleep(1)
            driver.find_element_by_id("easyDialogBoxeasyDialogYesBtn").find_element_by_xpath("..").click()  #点击上层聚焦
#            time.sleep(30)
            #driver.find_element_by_xpath(u"/html/body/div/div/div/div/button[text()='确定']").click()
            driver.find_element_by_id("easyDialogBoxeasyDialogYesBtn").click()   #确认删除
            #element = driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]")
            #waitresult = waitelement(element, 50 ,False)    for i inif EC.alert_is_present:


            time.sleep(2)
            for i in range(0,50):  #循环50次验证动态是否存在
                try:
                    driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]")
                    waitresult = True
                except:
                    waitresult = False
                    break
                time.sleep(1)
            
            if waitresult == True:
                pdr = "FAIL"
            else:
                pdr = "PASS"            
        except:
            pdr = "DONE"       
        return pdr