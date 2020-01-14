# -*- coding utf-8 -*-
# Author:longer
from selenium import webdriver
def browser():
    driver=webdriver.Chrome()
    return driver

if __name__ == '__main__':
    dr=browser()
    dr.get("http://psi.butterfly.mopaasapp.com")
    dr.quit()