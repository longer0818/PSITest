# -*- coding utf-8 -*-
# Author:longer
from case.Login_TestCase import LoginTest
import unittest
def login_ex():
    suite=unittest.TestSuite()
    suite.addTest(LoginTest('test_login1'))
    suite.addTest(LoginTest('test_login2'))
    suite.addTest(LoginTest('test_login3'))
    unittest.TextTestRunner().run(suite)

#login_ex()