#coding=utf-8

'''
Created on 2018年9月17日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os

class fmtb(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.88.116.46:88"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #非煤企业填报用例
    def test_fmtb(self):
        u"""非煤企业填报用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//*[@id='rightNavContent']/li[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='username']").send_keys("13100000002")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("13100000002")
        driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        time.sleep(2)
                
        try:
        #寻找是否存在该元素id
            driver.find_element_by_xpath("//*[@id='navbar-container']/div[1]/a/img")
        except:
        #如果没有找到上面的元素就截取当前页面。
            driver.get_screenshot_as_file("E:\\selenium_use_case\\error_png\\XJBT_fmtb.png")
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fmtb("test_fmtb"))
    results = unittest.TextTestRunner().run(suite)    