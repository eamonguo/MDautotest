# -*- coding: utf-8 -*-
from selenium import webdriver
import time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Firefox()
'''
iedriver = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
driver = webdriver.Ie(iedriver)

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
'''
loginname = "13700000001"
password = "qwe123456"
member = [u"沈婕",u"张丁菱"];
#member = ["111","beck"]
#member = [u"沈婕"]
allmember = ""
for i in range (0,len(member)):
    if i < len(member) - 1:
        allmember = allmember + member[i] + ","
    else:
        allmember = allmember + member[i]

base_url = "https://www2.mingdao.com/"
ISOTIMEFORMAT = '%Y-%m-%d-%X'
nowtime = time.strftime( ISOTIMEFORMAT, time.localtime() )
nowtime = nowtime.replace(":","")
nowtime = "C:\\test" + nowtime + ".txt"
#test_file = open(nowtime,'w') 
uploadfilename = "1.txt"
pathway = "D:\\" + uploadfilename

#登录
login = 1

#chat
chat_newchat = 1
chat_newgroup = 1
chat_turngroup = 1
chat_send = 1
chat_attachment = 1
chat_task = 1
chat_vote = 1
chat_post = 1
chat_date = 1
chat_disgroup = 1
chat_dischat = 1
chat_setadmin = 1
chat_remove = 1
chat_quitgroup = 1
chat_clsgroup = 1

#动态
post_send = 1
post_reply = 1
post_del = 1

#任务
task_newtask = 1
task_discuss = 1
task_replydic = 1
task_add = 1
task_entrust = 1
task_quittask = 1
task_deltask = 1
task_newpro = 1
task_setadmin = 1
task_newstep = 1
task_steptask = 1
task_delstep = 1
task_delpro = 1
task_done = 1

#日程
date_newdate = 1
date_deldate = 1

'''
        devjocelyn = "f441c155-5f1d-4848-9a02-7d5f59243342"
        devellie = "3f7fafa1-ffc7-4fac-9af2-18897158747f"
        deveamon = "140e9a2b-0d55-4a8f-a599-17f901650760"
        devrita = "bc3464d8-0367-48b9-8c86-fe275373c471"
        sbjocelyn = "63f15bab-9a51-4989-849f-71bcd9fa532b"
        sbellie = "a380faf3-67a8-4bea-b057-1dbe3c02f054"
        sbeamon = "1d57ea7e-6a5d-49c5-946b-fb845a05d814"
        sbrita = "b8b65e6b-4540-4f9e-80b3-09c33b692f5d"
        mhjocelyn = "b58d39a3-b7c5-4cb0-81aa-f7155bb07089"
        mhellie = "2ca1ab5a-5659-4250-afc8-686baee3e8ac"
        mheamon = "2020ac33-7911-4ebe-a070-0ac789229979"
        mhrita = "d4801998-baf4-4efb-8fcd-ca4aa1762cb6"
        mh137 = "d9b1aabc-8e75-4eb7-b2f3-6dc716715032"
'''
