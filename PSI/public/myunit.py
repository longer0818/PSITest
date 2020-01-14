# -*- coding utf-8 -*-
# Author:longer
from public.driver import browser
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()