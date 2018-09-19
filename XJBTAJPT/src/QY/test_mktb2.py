#coding=utf-8

'''
Created on 2018年9月19日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os

class mktb2(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.88.116.46:88"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #煤矿企业填报企业证照用例
    def test_mktb2(self):
        u"""煤矿企业填报企业证照用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='rightNavContent']/li[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='username']").send_keys("13100000006")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("13100000006")
        driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        time.sleep(5)
                
        try:
        #寻找是否存在该元素id
            driver.find_element_by_xpath("//*[@id='navbar-container']/div[1]/a/img")
        except:
        #如果没有找到上面的元素就截取当前页面。
            driver.get_screenshot_as_file("E:\\selenium_use_case\\error_png\\XJBT_mktb.png")
        
        driver.find_element_by_xpath("//*[@id='no_1005001']").click()
        time.sleep(3)
        
        js = "window.scrollTo(0,1000)" 
        driver.execute_script(js)
        
        driver.find_element_by_xpath("//*[@id='enterprise-license-form']/div[2]/div[1]/div[1]/div[4]/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-license-form']/div[2]/div[1]/div[1]/div[4]/input").send_keys("煤矿")
        
        #选择有效期开始日期
        driver.find_element_by_xpath("//*[@id='org-base-s']").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[8]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[1]").click()
        time.sleep(2)
        driver.switch_to.default_content()
        
        driver.find_element_by_xpath("//*[@id='enterprise-license-form']/div[2]/div[1]/div[3]/div[2]/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-license-form']/div[2]/div[1]/div[3]/div[2]/input").send_keys("兵团")
        
        #选择发放日期
        driver.find_element_by_xpath("//*[@id='enterprise-license-form']/div[2]/div[1]/div[3]/div[4]/input").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[8]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[1]").click()
        time.sleep(2)
        driver.switch_to.default_content()
        
        driver.find_element_by_xpath("//*[@id='yyzz']").click()
        time.sleep(2)
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(mktb2("test_mktb2"))
    results = unittest.TextTestRunner().run(suite)    