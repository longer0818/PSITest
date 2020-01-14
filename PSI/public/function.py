# -*- coding utf-8 -*-
# Author:longer
from selenium import webdriver
import os

def insert_img(driver,file_name):
    print(os.path.dirname(__file__))
    base_dir=os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    base_dir=str(base_dir)
    print(base_dir)
    #base_dir=base_dir.replace('\\','/')
    print(base_dir)
    base=base_dir.split('/test_case')[0]
    print(base)
    file_path=base+"/report/image/"+file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://psi.butterfly.mopaasapp.com")
    insert_img(driver,'login1.jpg')
    driver.quit()