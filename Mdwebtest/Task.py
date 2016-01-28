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
import  time, re
import pdb
#from pywinauto import application
#from Funtion import waitelement
import Funtion
import Config

class Task:
    def __init__(self):
        self.driver = Config.driver
    
    # 通过链接进入任务
    '''
    def task_move(self):
        driver = self.driver
        url = driver.current_url
        print url
        driver.get(Config.base_url + "Apps/task/center")
        print Config.base_url + "Apps/task/center"
        driver.refresh()  #任务多次出现内容出不来的情况，刷新页面
        time.sleep(3)
    '''
    def task_move(self):
        driver = self.driver
        gourl = Config.base_url + "Apps/task/center"
        for i in range(0,10):
            if driver.current_url == gourl:
                time.sleep(3)
                break
            else:
                driver.get(gourl)
                time.sleep(1)
        time.sleep(1)
        
                    
    # 创建新项目
    def task_newpro(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath(u"//span[@tip=\"创建新项目\"]").click()  #点击创建新项目
            time.sleep(1)
            global titlename
            global projectid
            titlename1 = time.ctime()
            titlename2 = u"测试项目"
            titlename = titlename1 + titlename2        #建立项目名称
            driver.find_element_by_id("folderName").clear()
            driver.find_element_by_id("folderName").send_keys(titlename)  #输入项目名称
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[@class=\"text\" and text()=\"公开项目\"]").click()  #选择公开项目
            time.sleep(1)
            driver.find_element_by_link_text(u"选择分享范围").click()  #点击分享范围
            time.sleep(1)
            driver.find_element_by_css_selector(u"label[title=\"自动化测试\"]").click()   #群组名要多环境适用，选择分享范围
            time.sleep(1)
            driver.find_element_by_id("folderName").click()  #聚焦到项目名称，以防分享范围列表遮挡确认按钮
            time.sleep(1)
            driver.find_element_by_link_text(u"确定").click()  #点击确认
            time.sleep(2)
            for i in range(0,5):
                try:  #验证新建项目是否存在
                    driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]")
                    tnp = "PASS"
                    projectid = driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]/../..").get_attribute("data-id")
                except:
                    tnp = "FAIL"
                    time.sleep(1)
        except:
            tnp = "DONE"
        return tnp
        
    # 添加项目成员并设置管理员
    def task_setadmin(self):
        driver = self.driver
        member = Config.member
        try:
           # projectid = driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]/../..").get_attribute("data-id")
            #移动到新建的项目，使齿轮按钮显示
            chain = ActionChains(driver)
            me = driver.find_element_by_css_selector("[title=\"" + titlename + "\"]")
            chain.move_to_element(me).perform()
            driver.find_element_by_xpath("//li[@data-id=\"" + projectid + "\"]//span[contains(@class,\"folderIcon icon-setting-six sinSettings\")]").click() #点击齿轮按钮
            driver.find_element_by_xpath(u"//span[text()=\"项目设置\"]").click() #点击项目设置
            time.sleep(2)
            driver.find_element_by_xpath(u"//span[text()=\"添加成员\"]").click()  #点击添加成员
            Funtion.addmember(*member)  #添加member列表中的所有成员
            time.sleep(2)
            driver.find_element_by_css_selector("[class='downArrow']").click()  #点击第一个成员的角色设置
            time.sleep(1)
            driver.find_element_by_css_selector("[class='folderManager']").click() #改变角色为管理者
            time.sleep(1)
            facttext = driver.find_element_by_css_selector("span.pointer > label.text").text  #获取第一个成员的角色名
            driver.find_element_by_css_selector("[class='dialogCloseBtn icon-task-delete']").click()  #关闭成员设置层
            time.sleep(3)
            expres = u"管理者"  #预期目标为管理者
            if facttext == expres:  #比较获取角色是否为预期结果
                tsa = "PASS"
            else: 
                tsa = "FAIL"
        except:
            tsa = "DONE"
        return tsa
    #'''
    # 创建项目阶段(meihua)
    def task_newstep(self):
        driver = self.driver
        global stageid
        try:
            driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]").click()
            time.sleep(1)
            #<li class="commItem subMissionMode animatedFast" title="阶段视图" style="background-color: transparent;">阶段</li>
            #driver.find_element_by_css_selector("[class='icon-task-stage iconDisplySingle']").click() #点击阶段试图
            driver.find_element_by_css_selector(u"li[title=\"阶段视图\"]").click()
            time.sleep(1)
            try:
                driver.find_element_by_xpath(u"//span[text()=\"新建阶段\"]").click()  #点击新建阶段(meihua)
            except:
                driver.find_element_by_css_selecto("span.addIcon.ThemeBGColor3>i.icon-addnewcalendar").click() #sandbox
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").clear()
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").send_keys(u"测试阶段")
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").send_keys(Keys.ENTER)  #输入阶段名称
            time.sleep(1)
            try:  #验证新建阶段是否存在
                driver.find_element_by_xpath(u"//span[@class=\"listStageName overflow_ellipsis Hidden\" and text()=\"测试阶段\"]")
                tns = "PASS"
                #获取阶段id
                stageid = driver.find_element_by_xpath(u"//span[@class=\"listStageName overflow_ellipsis Hidden\" and text()=\"测试阶段\"]/../..").get_attribute("data-stageid")
            except:
                tns = "FAIL"
        except:
            tns = "DONE"
        return tns
    '''
    # 创建项目阶段(sandbox)
    def task_newstep(self):
        driver = self.driver
        global stageid
        try:
            driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]").click()
            time.sleep(1)
            #<li class="commItem subMissionMode animatedFast" title="阶段视图" style="background-color: transparent;">阶段</li>
            #driver.find_element_by_css_selector("[class='icon-task-stage iconDisplySingle']").click() #点击阶段试图
            driver.find_element_by_css_selector(u"li[title=\"阶段视图\"]").click()
            time.sleep(2)
            #driver.find_element_by_xpath(u"//span[text()=\"新建阶段\"]").click()  #点击新建阶段(meihua)
            driver.find_element_by_css_selector("span.addIcon.ThemeBGColor3>i.icon-addnewcalendar").click() #sandbox
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").clear()
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").send_keys(u"测试阶段")
            time.sleep(1)
            driver.find_element_by_xpath(u"//input[@class=\"txtAddNew boderRadAll_3\" and @placeholder=\"填写阶段名称\"]").send_keys(Keys.ENTER)  #输入阶段名称
            time.sleep(1)
            try:  #验证新建阶段是否存在
                driver.find_element_by_xpath(u"//span[@class=\"listStageName overflow_ellipsis Hidden\" and text()=\"测试阶段\"]")
                tns = "PASS"
                #获取阶段id
                stageid = driver.find_element_by_xpath(u"//span[@class=\"listStageName overflow_ellipsis Hidden\" and text()=\"测试阶段\"]/../..").get_attribute("data-stageid")
            except:
                tns = "FAIL"
        except:
            tns = "DONE"
        return tns
    '''    
    # 创建阶段任务
    def task_steptask(self):
        driver = self.driver
        try:
            #在新建的阶段下新建阶段任务
            driver.find_element_by_xpath("//li[@data-stageid=\"" + stageid + u"\"]//span[@class=\"btnBottomNew \" and text()=\" + 创建新任务 \"]").click()
            time.sleep(1)
            driver.find_element_by_css_selector("textarea.teaStageName.boxSizing").clear()
            time.sleep(1)
            driver.find_element_by_css_selector("textarea.teaStageName.boxSizing").send_keys(u"阶段任务")  #输入阶段任务名称
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[@class=\"btnStagCreateTask boderRadAll_3\" and text()=\"确认\"]").click()  #点击确认
            time.sleep(2)
            try:  #验证新增的阶段任务是否创建成功
                driver.find_element_by_css_selector(u"span.listStageTaskName.overflow_ellipsis[title=阶段任务]")
                tst = "PASS"
            except:
                tst = "FAIL"
        except:
            tst = "DONE"        
        return tst
        
    # 删除阶段
    def task_delstep(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//li[@data-stageid=\"" + stageid + "\"]//span[@class=\"Right icon-arrow-down-border Relative Hidden\"]").click()
            time.sleep(1)
            driver.find_element_by_css_selector("[class='delStage']").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[@class=\"btnEnter boderRadAll_3\" and text()=\" 删除  \"]").click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath(u"//span[@class=\"listStageName overflow_ellipsis Hidden\" and text()=\"测试阶段\"]")
                tds = "FAIL"
            except:
                tds = "PASS"
        except:
            tds = "DONE"        
        return tds
        #pass = self.close_alert_and_get_its_text()
        
        # 删除项目
    def task_delpro(self):
        driver = self.driver
        try:
            chain = ActionChains(driver)
            me = driver.find_element_by_css_selector("[title=\"" + titlename + "\"]")
            chain.move_to_element(me).perform()       
            driver.find_element_by_xpath("//li[@data-id=\"" + projectid + "\"]//span[contains(@class,\"folderIcon icon-setting-six sinSettings\")]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//li[@data-type=\"del\"]").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[text()=\"同时删除项目下的所有任务\"]").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//span[text()=\" 删除  \"]").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//span[@class=\"folderName overflow_ellipsis ThemeColor10\" and @title=\"" + titlename + "\"]")
                tdp = "FAIL"
            except:
                tdp = "PASS"
        #pass = self.close_alert_and_get_its_text()
        except:
            tdp = "DONE"
        return tdp
        
    # 新建任务（button改动）
    def task_newtask(self):
        driver = self.driver
        global taskname
        # dev class=createNewTaskBtn animatedFast
        # meihua class=ThemeBGColor3 creasteNewTask boderRadAll_3 animatedFast boxShadowOpticy1
        try:
            #driver.find_element_by_css_selector("[class=\"typeName responsibleText ThemeColor10\"]").click()
            driver.find_element_by_css_selector("span.typeName.responsibleText.ThemeColor10").click()
            time.sleep(1)
            driver.find_element_by_xpath("//span/i[@class=\"icon-addnewcalendar\"]").click()
            time.sleep(1)
            taskname = "This is a task test " + time.ctime()
            driver.find_element_by_css_selector("[class='txtSingleName']").send_keys(taskname)
            time.sleep(1)
            driver.find_element_by_css_selector("[class='txtSingleName']").send_keys(Keys.ENTER)
            time.sleep(1)
            # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=txtSingleName]]
            # ERROR: Caught exception [ERROR: Unsupported command [keyUp | class=txtSingleName | \13]]
            try:
                driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]")
                tnt = "PASS"
            except:
                tnt = "FAIL"
        except:
            tnt = "DONE"
        return tnt

        # 添加任务成员         
    def task_add(self):
        driver = self.driver
        member = Config.member
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(2)
            bcount = len(driver.find_elements_by_xpath("//div[@class='members']/span"))
            #print "task_add1:" + str(bcount)
            time.sleep(4)
            driver.find_element_by_id("addMembers").click()
            time.sleep(1)
            Funtion.addmember(*member)
            time.sleep(1)
            for i in range(0,10):
                acount = len(driver.find_elements_by_xpath("//div[@class='members']/span"))
                #print "task_add2:" + str(acount)
                if acount == bcount + len(member):
                    tar = "PASS"
                    break
                else:
                    tar = "FAIL"
                    time.sleep(2)
        except:
            tar = "DONE"
        return tar
        
        # 删除任务(需要重新建立任务)
    def task_deltask(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(1)
            driver.find_element_by_css_selector("[class='manipulationMore iconTip']").click()
            time.sleep(1)
            driver.find_element_by_xpath(u"//div[@id='slideTaskDetail']//li[text()=\"删除任务\"]").click()
            time.sleep(1)
            driver.find_element_by_css_selector("[class='btnEnter boderRadAll_3']").click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]")
                tdt = "FAIL"
            except:
                tdt = "PASS"
        except:
            tdt = "DONE"
        return tdt
        
        # 托付任务 
    def task_entrust(self):
        driver = self.driver
        member = Config.member
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(1)
            bcount = len(driver.find_elements_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])"))
            #print "task_entrust1:" + str(bcount)
            driver.find_element_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])[last()-1]").click()
            time.sleep(1)
            Funtion.addmember(member[0])
            time.sleep(1)
            acount = len(driver.find_elements_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])"))
            #print "task_entrust2:" + str(acount)
            #if acount == bcount -1:
            if acount < bcount:
                tet = "PASS"
            else:
                tet = "FAIL"
        except:
            tet = "DONE"
        return tet
        
        # 完成任务        
    def task_done(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(1)
            #driver.find_element_by_id("updateTaskStatus").click()
            driver.find_element_by_css_selector("span.markTask").click()
            time.sleep(3)
            for i in range(0,10):
                try:
                    driver.find_element_by_css_selector("span.markTask.completeHook")
                    tdr = "PASS"
                    break
                except:
                    tdr = "FAIL"
                    time.sleep(0.5)
        except:
            tdr = "DONE"
        return tdr
        
        # 退出任务
    def task_quittask(self):
        driver = self.driver
        try:
            bcount = len(driver.find_elements_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])"))
            #print "task_quittask1:" + str(bcount)
            chain = ActionChains(driver)
            me = driver.find_element_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])[last()]")
            chain.move_to_element(me).perform()
            time.sleep(2)
            driver.find_element_by_xpath(u"//span[text()=\"退出任务\"]").click()
            time.sleep(3)
            acount = len(driver.find_elements_by_xpath("(//img[contains(@src,'https://dn-mdpic.qbox.me/UserAvatar/default1.png?watermark/2/text/MTM=/font/5b6u6L2v6ZuF6buR/fontsize/600/fill/d2hpdGU=/dissolve/100/gravity/Center/dx/0/dy/0%7CimageView2/1/w/48/h/48/q/90')])"))
            #print "task_quittask2:" + str(acount)
            if acount == bcount -1:
                tqt = "PASS"
            else:
                tqt = "FAIL"
        except:
            tqt = "DONE"
        return tqt
        
    # 评论任务
    def task_discuss(self):
        driver = self.driver
        global discontent
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(2)
            discontent = u"This is discuss content" + time.ctime() 
            discontent2 = discontent + u"[可爱]"
            driver.find_element_by_css_selector("[class='txtComment']").clear()
            driver.find_element_by_css_selector("[class='txtComment']").send_keys(discontent2)  
            time.sleep(1)
            driver.find_element_by_css_selector("[class='talkSendBtn boderRadAll_3']").click()
            time.sleep(2)
            try:
               driver.find_elements_by_xpath("//div[contains(text(),'" + discontent + "')]")
               tdr = "PASS"
            except:
               tdr = "FAIL"
        except:
            tdr= "DONE"
        return tdr
    
    # 回复评论    
    def task_replydic(self):
        driver = self.driver       
        global replycontent
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(2)
            chain = ActionChains(driver)
            me = driver.find_element_by_css_selector("span.DateTask")
            chain.move_to_element(me).perform()
            driver.find_element_by_link_text(u"回复").click()
            time.sleep(1)
            replycontent = time.ctime() + u" 收到"
            replycontent2 = replycontent + u" @郭奕明 [衰]"
            driver.find_element_by_css_selector("[class='TextArea replyTxtArea boderRadAll_3']").send_keys(replycontent2)
            time.sleep(1)
            #Funtion.scrollbarmove("","100000") #slideTaskDetail
            driver.find_element_by_css_selector("div.taskContent").send_keys(Keys.DOWN)
            time.sleep(1)
            driver.find_element_by_css_selector("input.talkSendBtn.boderRadAll_3.ThemeBGColor3.Right").click()
            time.sleep(2)
            try:
                driver.find_elements_by_xpath("//div[contains(text(),'" + replycontent + "')]")
                trd = "PASS"
            except:
                trd = "FAIL"
        except:
            trd = "DONE"
        return trd
        
    # 删除任务
    def task_deltask(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]").click()
            time.sleep(1)
            driver.find_element_by_css_selector("li.manipulationMore.iconTip>i.icon-arrow-down-border").click()
            time.sleep(1)
            driver.find_element_by_css_selector("ul.Right.manipulation i.icon-task-new-delete").click()
            time.sleep(1)
            driver.find_element_by_css_selector("span.btnEnter.boderRadAll_3").click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//span[@title=\"" + taskname + "\"]")
                tdt = "FAIL"
            except:
                tdt = "PASS"
        except:
            tdt = "DONE"
        return tdt