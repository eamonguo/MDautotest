# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con
import win32gui
import time, re
import pdb
from pywinauto import application
import Login
import Post
import Config
import Chat
import Task
import Date

#test_file = Config.test_file
'''
def waitelement(element, times, result):
    for i in range (0,times):
        try:
            driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/div[2]/div[1]/div[1]/div[3]/ul/li[1]/div[2]/div[1]/div/div/div/div[contains(text(),\"" + messagenow + "\")]")
            item = True
            if result != False:
                break
        except:
            item = False
            if result == False:
                break
        time.sleep(1)
        print i
    print item
    return item  
''' 


def addmember(*member):
    driver = Config.driver
    for i in range (0,len(member)):
        driver.find_element_by_css_selector("input.txt.txtKeyword").clear()
        driver.find_element_by_css_selector("input.txt.txtKeyword").send_keys(member[i])
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div/font[text()=\"" + member[i] + "\"]").click()
        time.sleep(2)
    driver.find_element_by_xpath(u"//input[@value='确认邀请' or @value='添加' or @value='设为负责人']").click()

def datedata(titlename,*member):
    driver = Config.driver
    driver.find_element_by_id("txtCalendarName").clear()
    driver.find_element_by_id("txtCalendarName").send_keys(titlename)
    driver.find_element_by_xpath(u"//span[@class=\"textboxlist-bit-editable-addtag ThemeColor3\" and text()=\"+ 添加参与人员\"]").click()
    # 添加人员（2个人）
    for i in range (0,len(member)):
        #print member[i]
        driver.find_element_by_xpath("//input[@class=\"textboxlist-bit-editable-input\"]").send_keys(member[i])
        time.sleep(2)
        driver.find_element_by_xpath("//input[@class=\"textboxlist-bit-editable-input\"]").send_keys(Keys.ENTER)
    #driver.find_element_by_xpath("//input[@class=\"textboxlist-bit-editable-input\"]").send_keys(u"张丁菱")
    #driver.find_element_by_xpath("//input[@class=\"textboxlist-bit-editable-input\"]").send_keys(Keys.ENTER)
    # 分享至动态
    # 点小三角    xpath=//span[@id="chToFeedCalendar"]
    # //div[@id='CreateCalendarView']/div/i
    driver.find_element_by_link_text(u"创 建").click()
    
def scrollbarmove(elementid,movevalue):
    driver = Config.driver
    if elementid != "":
        js="var q=document.getElementById('" + elementid + "').scrollTop=" + movevalue
    else: 
        js="var q=document.documentElement.scrollTop=" + movevalue
    driver.execute_script(js)
    time.sleep(2)
    
def upload(path):
    filename1 = u"文件上传"
    filename2 = u"打开(&O)"
    filename3 = u"取消"
    app = application.Application()
    window = app.window_(class_name = "#32770")
    #window.print_control_identifiers()
    #filename1 = '文件上传'.decode('gb2312')
    #filename2 ="打开(&O)".decode('gb2312')
    hwnd=win32gui.FindWindow(None,filename1) 
    time.sleep(1) 
    win32gui.EnableWindow(hwnd,True)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(2)
    window["Edit"].TypeKeys(path)
    #window["Edit"].TypeKeys("d:\1.txt")
    time.sleep(2)
    #window["ScrollBar2"].Click()
    #window.SetFocus()
    time.sleep(2)     
    window[filename2].Click()
    try:
        window[filename2]
        window[filename2].Click()
    except:
        #window[filename3].Click()
        upclick = 0
        
def resultjudge(cls, fun, switch):
    lcount = 0
    if switch == 1:
        for i in range(0,3):
            if cls == "Login" :
                a = Login.Login()
            elif cls == "Post" :
                a = Post.Post()
            elif cls == "Chat" :
                a = Chat.Chat()
            elif cls == "Task" :
                a = Task.Task()
            elif cls == "Date" :
                a = Date.Date()
            
                       
            global aa
            #登录
            if fun == "login":
                aa = a.login()
            #动态    
            elif fun == "post_send":
                aa = a.post_send()
            elif fun == "post_reply":
                aa = a.post_reply()
            elif fun == "post_del":
                aa = a.post_del()
            #chat
            elif fun == "chat_newchat":
                aa = a.chat_newchat()
            elif fun == "chat_newgroup":
                aa = a.chat_newgroup()
            elif fun == "chat_turngroup":
                aa = a.chat_turngroup()
            elif fun == "chat_send":
                aa = a.chat_send()
            elif fun == "chat_attachment":
                aa = a.chat_attachment()
            elif fun == "chat_task":
                aa = a.chat_task()
            elif fun == "chat_vote":
                aa = a.chat_vote()
            elif fun == "chat_post":
                aa = a.chat_post()
            elif fun == "chat_date":
                aa = a.chat_date()
            elif fun == "chat_disgroup" :
                aa = a.chat_disgroup()   
            elif fun == "chat_dischat" :
                aa = a.chat_dischat()
            elif fun == "chat_setadmin" :
                aa = a.chat_setadmin()
            elif fun == "chat_remove" :
                aa = a.chat_remove()
            elif fun == "chat_quitgroup" :
                aa = a.chat_quitgroup()
            elif fun == "chat_clsgroup" :
                aa = a.chat_clsgroup()
            #任务
            elif fun == "task_newtask" :
                aa = a.task_newtask()
            elif fun == "task_discuss" :                    
                aa = a.task_discuss()
            elif fun == "task_replydic" :
                aa = a.task_replydic()
            elif fun == "task_add" :
                aa = a.task_add()
            elif fun == "task_entrust" :                    
                aa = a.task_entrust()
            elif fun == "task_quittask" :
                aa = a.task_quittask()
            elif fun == "task_deltask" :
                aa = a.task_deltask()
            elif fun == "task_newpro" :                    
                aa = a.task_newpro()
            elif fun == "task_setadmin" :
                aa = a.task_setadmin()
            elif fun == "task_newstep" :
                aa = a.task_newstep()
            elif fun == "task_steptask" :                    
                aa = a.task_steptask()
            elif fun == "task_delstep" :
                aa = a.task_delstep()  
            elif fun == "task_delpro" :
                aa = a.task_delpro()
            elif fun == "task_done" :
                aa = a.task_done()                
            #日程
            elif fun == "date_newdate" :
                aa = a.date_newdate()
            elif fun == "date_deldate" :
                aa = a.date_deldate()         
            #print aa
            
            if aa == "PASS":
                break
            else: 
                lcount = lcount + 1
    else:
        aa = "UNDO"
    print (fun + " Result: " + aa)
    #test_file.write(fun + " Result: " + aa + "\n")
    if lcount == 1 or lcount == 2:
        print (fun + " FAIL Time: " + str(lcount))
        #test_file.write(fun + " FAIL Time: " + str(lcount)+"\n")
    elif lcount == 3:
        print fun + " " + aa + " 3 Time," + fun + " Test End"
        #test_file.write(" FAIL 3 Time," + fun + " Test End\n")