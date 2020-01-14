# -*- coding utf-8 -*-
# Author:longer
from selenium.webdriver.common.by import By
from public.base import Page
from time import sleep

class Login(Page):
    url='/'
    login_username_loc=(By.ID,"editLoginName")
    login_password_loc=(By.ID,"editPassword")
    login_button_loc=(By.ID,"buttonOK")
    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
    #定义统一登录入口
    def user_login(self,username="username",password="passwrd"):
     #获取用户名密码
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)