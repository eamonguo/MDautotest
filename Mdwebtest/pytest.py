# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
#from selenium.webdriver.common.action_chains import ActionChains
# import win32api
# import win32con
import time, re
#import pdb
#from pywinauto import application
import Login
import Post
import Chat
from Funtion import resultjudge
import Config
import Task
import Date
import sys


driver = Config.driver
#test_file = Config.test_file
test_file = Config.nowtime    
#sys.stdout = open(nowtime,'w')
   
time1 = time.time()
print ("Testing environment: " + Config.base_url)
print "Test start time: " + time.ctime()
#��¼
resultjudge("Login", "login", Config.login)

#chat
#�½�����-������Ϣ-������Ƭ-���ճ̿�-��ɢ����
print "Chat==> create chat -- send message -- send attachment -- task card -- date card -- drop chat"
#test_file.write("Chat==> create chat -- send message -- task card -- date card -- drop chat\n")
Chat.Chat().chat_move()
resultjudge("Chat", "chat_newchat", Config.chat_newchat)
resultjudge("Chat", "chat_send", Config.chat_send)
resultjudge("Chat", "chat_attachment", Config.chat_attachment)
resultjudge("Chat", "chat_task", Config.chat_task)
resultjudge("Chat", "chat_date", Config.chat_date)
resultjudge("Chat", "chat_dischat", Config.chat_dischat)

#�½�����-����תȺ��-��ɢȺ��
print "Chat==> create chat -- chat to group -- drop group"
#test_file.write("Chat==> create chat -- chat to group -- drop group\n")
Chat.Chat().chat_move()
resultjudge("Chat", "chat_newchat", Config.chat_newchat)
resultjudge("Chat", "chat_turngroup", Config.chat_turngroup)
resultjudge("Chat", "chat_disgroup", Config.chat_disgroup)


#�½�Ⱥ��-������Ϣ-����̬��Ƭ-��ͶƱ-�ر�Ⱥ��
print "Chat==> create group -- send message -- post card -- vote card -- close group"
#test_file.write("Chat==> create group -- send message -- post card -- vote card -- close group\n")
Chat.Chat().chat_move()
resultjudge("Chat", "chat_newgroup", Config.chat_newgroup)
resultjudge("Chat", "chat_send", Config.chat_send)
resultjudge("Chat", "chat_post", Config.chat_post)
resultjudge("Chat", "chat_vote", Config.chat_vote)
resultjudge("Chat", "chat_clsgroup", Config.chat_clsgroup)

#��̬
#����̬-�ظ���̬-ɾ����̬
print "Post==> send post-- reply post -- delete post"
#test_file.write("Post==> send post-- reply post -- delete post\n")
Post.Post().post_move()
resultjudge("Post","post_send", Config.post_send)
resultjudge("Post","post_reply", Config.post_reply)
resultjudge("Post", "post_del", Config.post_del)


#����
#�½���Ŀ-���ù���Ա-�½���Ŀ�׶�-�½��׶�����-ɾ���׶�-ɾ����Ŀ(�޸�)
print "Task==> create project -- set admin -- create step -- create step task -- delete step -- delete project"
#test_file.write("Chat==> creategroup -- sendmessage -- postcard -- votecard -- closegroup\n")
Task.Task().task_move()
resultjudge("Task", "task_newpro", Config.task_newpro)
resultjudge("Task", "task_setadmin", Config.task_setadmin)
resultjudge("Task", "task_newstep", Config.task_newstep)
resultjudge("Task", "task_steptask", Config.task_steptask)
resultjudge("Task", "task_delstep", Config.task_delstep)
resultjudge("Task", "task_delpro", Config.task_delpro)

#�½�����-��������Ա-�и�����-�������-�˳�����
print "Task==> create task -- entrust task -- task done -- quit task"
#test_file.write("Task==> create task -- entrust task -- task done -- quit task")
Task.Task().task_move()
resultjudge("Task", "task_newtask", Config.task_newtask)
resultjudge("Task", "task_add", Config.task_add)

resultjudge("Task", "task_entrust", Config.task_entrust)
resultjudge("Task", "task_done", Config.task_done)
resultjudge("Task", "task_quittask", Config.task_quittask)

#�½�����-��������-�ظ���������-ɾ������
print "Task==> create task -- discuss task -- reply task -- delete task"
#test_file.write("Task==> create task -- discuss task -- reply task -- delete task\n")
Task.Task().task_move()
resultjudge("Task", "task_newtask", Config.task_newtask)
resultjudge("Task", "task_discuss", Config.task_discuss)
resultjudge("Task", "task_replydic", Config.task_replydic)
resultjudge("Task", "task_deltask", Config.task_deltask)


#�ճ�
#�½��ճ�-ɾ���ճ�
print "Date==> create date -- delete date"
#test_file.write("Date==> create date -- delete date\n")
Date.Date().date_move()
resultjudge("Date", "date_newdate", Config.date_newdate)
resultjudge("Date", "date_deldate", Config.date_deldate)

time2 = time.time()
print "Test end time: " + time.ctime()
costtime = str(round((time2 - time1), 2))
print ("Test Cost Time: " + costtime + "s")
#test_file.write("Test Cost Time: " + costtime + "s")
#test_file.close

print "End"
driver.quit()
