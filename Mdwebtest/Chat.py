# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
# import win32api
# import win32con
import time, re
#import pdb
#from pywinauto import application
import Login
import Post
#from Funtion import addmember
import Funtion
import Config

class Chat:
    def __init__(self):
        self.driver = Config.driver
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # 进入chat链接-解决www或www2自动跳转meihua的问题

    def chat_move(self):
        driver = self.driver
        driver.get(Config.base_url + "chat")
        time.sleep(3)
          
    # 新建聊天 
    def chat_newchat(self):
        try:
            global cid
            global cit
            global ciw
            cid = ""             #初始化
            cit = ""
            ciw = ""
            driver = self.driver
            loginname = Config.loginname
            member = Config.member           #获取添加成员列表
            allmember = Config.allmember     #获取需要验证的群组名变量
            driver.find_element_by_css_selector("[class=\"icon-folder-addTask ThemeColor8\"]").click()   #点击+
            time.sleep(1)
            driver.find_element_by_id("btnNewDisGroup").click()             #点击新建聊天
            time.sleep(2)
            Funtion.addmember(*member)          #添加成员数组内的全部成员
            time.sleep(4)
            for i in range(0,3):
                try:  #验证创建的聊天是否存在-通过聊天名
                    driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + allmember + "  \"]")
                    cnc = "PASS"
                    time.sleep(1)
                    #点击该聊天
                    driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + allmember + "  \"]").click()  
                    time.sleep(1)  
                    #保存该聊天的id
                    cid = driver.find_element_by_css_selector("[class=\"ThemeHoverBGColor7 ThemeBorderColor7 active ThemeBGColor8\"],[data-type=\"2\"],[data-push=\"true\"]").get_attribute("id")
                    cit = cid.replace('st','chat')
                    ciw = cid.replace('st','sw')
                    #print ciw
                    break
                except:
                    cnc = "FAIL"
                    time.sleep(1)
        except:
            cnc = "DONE"
        return cnc
        
    # 发送消息
    def chat_send(self):
        try:
            driver = self.driver
            #driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + member + "  \"]").click()  
            ms = time.ctime()    #获取当前时间
            driver.find_element_by_id(cit).clear()
            driver.find_element_by_id(cit).send_keys(ms)    #在聊天窗口内输入当前时间
            time.sleep(1)
            driver.find_element_by_id(cit).send_keys(Keys.ENTER)    #在聊天窗口内输入回车
            time.sleep(2)
            for i in range(0,10):
                try:
                    driver.find_element_by_xpath("//div[contains(text(),'" + ms + "')]") 
                    csr = "PASS"
                    break
                except:
                    csr = "FAIL"
                    time.sleep(1)
        except:
            csr = "DONE"
        return csr
    
    # 解散聊天
    def chat_dischat(self):
        driver = self.driver
        try:
            dcr = ""   #初始化
            driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i").click()   #点击齿轮
            time.sleep(2)
            driver.find_element_by_css_selector("div.userGroupDeleteDIV").click()    #点击解散聊天
            driver.find_element_by_css_selector("[class=\"btn btnLink btnConfirm ThemeBGColor3\"]").click()   #点击确认
            time.sleep(0.5)
            """
            try:   #获取alert信息
                alert=driver.switch_to_alert()
                print (alert.text)
                alert.dismiss()
            except:
                time.sleep(1)
                print 2
            
            #xxx = self.close_alert_and_get_its_text()
            #print xxx
            """
            try:  #验证之前创建的聊天是否存在
                time.sleep(2)
                driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i")
                #driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + member + "  \"]")
                dcr = "FAIL"
            except:
                dcr = "PASS"
        except:
            if dcr == "":
                dcr = "DONE"
        return dcr
        
    # 聊天转群
    def chat_turngroup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i").click()   #点击新建的聊天
            time.sleep(2)
            #driver.find_element_by_css_selector("div.userGroupDeleteDIV").click()
            #driver.find_element_by_css_selector("[class=\"discussionGroupConversionClick\"]").click
            driver.find_element_by_link_text(u"转换为长期群组>").click()  #点击转群组
            time.sleep(1)
            driver.find_element_by_css_selector("[class=\"btn btnLink btnConfirm ThemeBGColor3\"]").click()  #点击确认
            time.sleep(4)
            try:  #验证群组图标是否存在
                driver.find_element_by_xpath("/html/body/form/div/div/div/div/div[@id=\"" + ciw + u"\"]/div[1]/div[1]/div[1]/a[@data-titletip=\"查看群组动态\"]")
                ctr = "PASS"
            except:
                ctr = "FAIL"
        except:
            ctr = "DONE"   
        return ctr
        
    # 解散群组
    def chat_disgroup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i").click()  #点击新建的群组
            driver.find_element_by_css_selector(".icon-chat-gear").click()   #点击齿轮
            time.sleep(2)
            driver.find_element_by_css_selector("[class*=\"groupSettingsTop Hand\"]").click()   #进入群设置
            time.sleep(3)
            driver.find_element_by_css_selector("div.groupSettingBottomDel").click()   #点击解散群组
            time.sleep(3)
            driver.find_element_by_css_selector("[class=\"btn btnLink btnConfirm ThemeBGColor3\"]").click()  #点击确定
            try:  #验证群组是否存在
                time.sleep(2)
                driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i")
                #driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + member + "  \"]")
                cdg = "FAIL"
            except:
                cdg = "PASS"
        except:
            cdg = "DONE"
        return cdg
    
    # 发送日程卡片    
    def chat_date(self):
        driver = self.driver
        try:        
            driver.find_element_by_id(cit).click()
            time.sleep(1)
            driver.find_element_by_css_selector("div#" + ciw + " i.icon-create-network").click()
            chain = ActionChains(driver)  
            me = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[2]/div[@id='" + ciw + "']/div[1]/div[3]/div/div[1]/div/div/ul/li[2]")      
            chain.move_to_element(me).perform()
            time.sleep(2)
            driver.find_element_by_css_selector("div#" + ciw + " li.menuItem.btnNewSchedule").click()
            time.sleep(3)
            datename = time.ctime()
            member = Config.member
            Funtion.datedata(datename,*member)
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//div[@class=\"cardContent\"][text()=\"" + datename + "\"]")            
                cdr = "PASS"
            except:
                cdr = "FAIL"
        except:
            cdr = "DONE"
        return cdr
    
    # 发送附件    
    def chat_attachment(self):
        driver = self.driver
        factfilename = Config.uploadfilename
        path = Config.pathway
        try:
            driver.find_element_by_id(cit).click()
            time.sleep(1)
            driver.find_element_by_css_selector("i.icon-chat-clip").click()
            time.sleep(1)
            Funtion.upload(path)
            time.sleep(4)
            try:
                filename = driver.find_element_by_css_selector("div.fileName").text
                driver.find_element_by_css_selector("div.fileName").click()
                time.sleep(2)
                driver.find_element_by_css_selector("div.btnClose").click()
                if factfilename == filename:
                    car = "PASS"
                else:
                    car = "FAIL"
            except:
                car = "FAIL"
        except:
            car = "DONE"
        return car
        
    # 发送任务卡片
    def chat_task(self):
        driver = self.driver
        try:
            driver.find_element_by_id(cit).click()
            tasktitle = time.ctime()
            time.sleep(1)
            driver.find_element_by_css_selector("div#" + ciw + " i.icon-create-network").click()
            chain = ActionChains(driver)  
            me = driver.find_element_by_xpath(" /html/body/form/div[5]/div/div/div[2]/div[@id='" + ciw + "']/div[1]/div[3]/div/div[1]/div/div/ul/li[1]")     
            chain.move_to_element(me).perform()
            time.sleep(2)
            driver.find_element_by_css_selector("div#" + ciw + " li.menuItem.btnNewTask").click()  
            time.sleep(3)
            driver.find_element_by_id("txtTaskName").click()
            driver.find_element_by_id("txtTaskName").clear()
            driver.find_element_by_id("txtTaskName").send_keys(tasktitle)
            time.sleep(1)
            driver.find_element_by_link_text(u"创建").click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//div[@class=\"cardContent\"][text()=\"" + tasktitle + "\"]")            
                ctr = "PASS"
            except:
                ctr = "FAIL"  
        except:
        	  ctr = "DONE"
        return ctr
    '''
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    '''
    
    # 创建群组
    def chat_newgroup(self):
        driver = self.driver
        groupname = time.ctime()
        global cid
        global cit
        global ciw
        cid = ""
        cit = ""
        ciw = ""
        try:
            driver.find_element_by_css_selector("[class=\"icon-folder-addTask ThemeColor8\"]").click()   #点击+
            time.sleep(1)
            driver.find_element_by_id("btnNewGroup").click()             #点击新建聊天
            time.sleep(2)
            driver.find_element_by_css_selector("input.TextBoxNew.Gray_8.txtGroupName").clear()
            driver.find_element_by_css_selector("input.TextBoxNew.Gray_8.txtGroupName").send_keys(groupname)
            time.sleep(1)
            driver.find_element_by_css_selector(u"input[value=\"创建\"]").click()
            time.sleep(3)
            for i in range(0,5):
                try:
                    driver.find_element_by_xpath(u"//div[text()=\"暂不添加群成员\"]")
                    driver.find_element_by_xpath(u"//div[text()=\"暂不添加群成员\"]").find_element_by_xpath("..").click()
                    time.sleep(2)
                    driver.find_element_by_xpath(u"//div[text()=\"暂不添加群成员\"]").click()
                except:
                    break
                    
            for i in range(0,5):
                try:  #验证创建的聊天是否存在-通过聊天名
                    driver.find_element_by_xpath("//span[contains(text(),'" + groupname + "')]")
                    driver.find_element_by_xpath("//span[contains(text(),'" + groupname + "')]").click
                    time.sleep(1)
                    cid = driver.find_element_by_xpath("//span[contains(text(),'" + groupname + "')]/../../../../div/ul/li").get_attribute("id")
                    cit = cid.replace('st','chat')
                    ciw = cid.replace('st','sw')
                    #driver.find_element_by_css_selector("span.sessionName:contains(\"" + groupname + "\")+a>i.icon-task-participate")
                    cng = "PASS"
                    #print ciw
                    break
                except:
                    cng = "FAIL"
                    time.sleep(2)
        except:
            cng = "DONE"
        return cng
    
    # 发动态卡片
    def chat_post(self):
        driver = self.driver
        try:
            driver.find_element_by_id(cit).click()
            posttitle = time.ctime()
            time.sleep(1)
            driver.find_element_by_css_selector("div#" + ciw + " i.icon-create-network").click()
            time.sleep(1)
            driver.find_element_by_css_selector("li.menuItem.btnNewPost").click()
            time.sleep(3)
            driver.find_element_by_id("MDUpdater_textarea_Updater").clear()
            driver.find_element_by_id("MDUpdater_textarea_Updater").send_keys(posttitle)
            time.sleep(1)
            driver.find_element_by_css_selector("a.updaterFor.TxtMiddle").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[text()=\"自动化测试\"]").click()
            time.sleep(1)
            driver.find_element_by_id("MDUpdater_textarea_Updater").click()
            time.sleep(1)
            driver.find_element_by_id("MDUpdater_button_Share").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//div[contains(text(),'" + posttitle + "')]")  
                cpr = "PASS"
            except:
                cpr = "FAIL"
        except:
            cpr = "DONE"
        return cpr
    
    # 发投票卡片
    def chat_vote(self):
        driver = self.driver
        votetitle = time.ctime()
        try:
            driver.find_element_by_css_selector("div#" + ciw + " i.icon-create-network").click()
            time.sleep(1)
            driver.find_element_by_css_selector("li.menuItem.btnNewVote").click()
            time.sleep(3)
            driver.find_element_by_id("MDUpdater_textarea_Updater").clear()
            driver.find_element_by_id("MDUpdater_textarea_Updater").send_keys(votetitle)
            driver.find_element_by_xpath(u"(//input[@value='请输入投票项'])[1]").clear()
            driver.find_element_by_xpath(u"(//input[@value='请输入投票项'])[1]").send_keys("111")
            driver.find_element_by_xpath(u"(//input[@value='请输入投票项'])[2]").clear()
            driver.find_element_by_xpath(u"(//input[@value='请输入投票项'])[2]").send_keys("222")
            driver.find_element_by_css_selector("a.updaterFor.TxtMiddle").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[text()=\"自动化测试\"]").click()
            time.sleep(1)
            driver.find_element_by_id("MDUpdater_textarea_Updater").click()
            time.sleep(1)
            driver.find_element_by_id("MDUpdater_button_Share").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//div[contains(text(),'" + votetitle + "')]")
                cvr = "PASS"
            except:
                cvr = "FAIL"
        except:
            cvr = "DONE"
        return cvr
        
    # 关闭群组    
    def chat_clsgroup(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i").click()  #点击新建的群组
            driver.find_element_by_css_selector(".icon-chat-gear").click()   #点击齿轮
            time.sleep(2)
            driver.find_element_by_css_selector("[class*=\"groupSettingsTop Hand\"]").click()   #进入群设置
            time.sleep(3)
            driver.find_element_by_css_selector("div.groupSettingBottomClo").click()   #点击解散群组
            time.sleep(3)
            driver.find_element_by_css_selector("[class=\"btn btnLink btnConfirm ThemeBGColor3\"]").click()  #点击确定
            try:  #验证群组是否存在
                time.sleep(2)
                driver.find_element_by_xpath("//div[@id='" + ciw + "']/div/div/div[2]/span[2]/i")
                #driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[1]/div[3]/div[1]/div[1]/div[1]/ul/li/div/div/div[1]/span[text()=\"  " + loginname + "," + member + "  \"]")
                ccg = "FAIL"
            except:
                ccg = "PASS"
        except:
            ccg = "DONE"
        return ccg