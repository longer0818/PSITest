# -*- coding utf-8 -*-
# Author:longer
import unittest
from selenium import webdriver
from page.Login_Page import Login
from log.user_log import UserLog
import time
import os

class LoginTest(unittest.TestCase):
    '''登录功能'''
    @classmethod
    def setUpClass(cls):
        cls.log=UserLog()
        cls.logger=cls.log.get_log()

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://psi.butterfly.mopaasapp.com')
        #logger.debug("this a Chrome")
        self.logger.info("this a Chrome")


    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join('E:\longer\\test\PSI'+"/image/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def user_login_verify(self,username="",password=""):
        Login(self.driver).user_login(username,password)
    #@unittest.skip("test_login1")
    def test_login1(self):
        '''用户名为空'''
        self.user_login_verify(password="admin")
        user_error_hint=self.driver.find_element_by_xpath('//*[@id="divInfo"]').text
        self.assertEqual('没有输入登录名',user_error_hint)

    #@unittest.skip("test_login2")
    def test_login2(self):
        '''密码为空'''
        self.user_login_verify(username="admin")
        pawd_error_hint=self.driver.find_element_by_xpath('//*[@id="divInfo"]').text
        self.assertEqual('没有输入密码',pawd_error_hint)

    #@unittest.skip("test_login3")
    def test_login3(self):
        '''正确用户名、密码'''
        self.user_login_verify(username="admin",password="admin")
        title=self.driver.title
        self.assertEqual("首页 - PSI",title)

if __name__ == '__main__':
    unittest.main()