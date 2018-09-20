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

class fmtb1(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.88.116.46:88"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #非煤企业填报企业信息用例
    def test_fmtb1(self):
        u"""非煤企业填报企业信息用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='rightNavContent']/li[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='username']").send_keys("13100000002")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("13100000002")
        driver.find_element_by_xpath("//*[@id='loginBtn']").click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
                
        try:
        #寻找是否存在该元素id
            driver.find_element_by_xpath("//*[@id='navbar-container']/div[1]/a/img")
        except:
        #如果没有找到上面的元素就截取当前页面。
            driver.get_screenshot_as_file("E:\\selenium_use_case\\error_png\\XJBT_fmtb.png")
        
        driver.find_element_by_xpath("//*[@id='no_1005001']").click()
        time.sleep(3)
        
        #填写企业信息
        driver.find_element_by_xpath("//*[@id='fullname']").clear()
        driver.find_element_by_xpath("//*[@id='fullname']").send_keys("新疆天山采矿场")
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[1]/div[2]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[1]/div[2]/div/input").send_keys("天山采矿")
        
        #选择核发对象
        driver.find_element_by_xpath("//*[@id='select2-legalpersontype-container']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//*[@class='select2-results__option select2-results__option--highlighted']").click()
        driver.implicitly_wait(30)
        
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[3]/div[2]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[3]/div[2]/div/input").send_keys("李大勇")
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[4]/div[1]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[4]/div[1]/div/input").send_keys("88585858")
        
        #选择国民经济分类
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[5]/div[2]/div/span/span/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/ul/li/div/span[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/ul/li/ul/li/div/span[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/ul/li/ul/li/ul/li/div/span[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[6]/div/ul/li/ul/li/ul/li/ul/li/div/span[6]").click()
        time.sleep(1)
        
        #选择企业经济类型
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[6]/div[1]/div/span/span/a").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("/html/body/div[7]/div/ul/li/div/span[1]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("/html/body/div[7]/div/ul/li/ul/li/div/span[4]").click()
        time.sleep(1)
        
        #选择行政隶属关系
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[6]/div[2]/div/span/span[1]/span/span[2]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("html/body/span/span/span[2]/ul/li[1]").click()
        driver.implicitly_wait(30)
        
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[7]/div[1]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[7]/div[1]/div/input").send_keys("1234@qq.com")
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[7]/div[2]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[7]/div[2]/div/input").send_keys("830000")
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[8]/div[1]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[8]/div[1]/div/input").send_keys("2000")
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[8]/div[2]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[8]/div[2]/div/input").send_keys("12345678.12")
        
        #选择企业状态
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[9]/div[1]/div/span/span[1]/span/span[2]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("html/body/span/span/span[2]/ul/li[2]").click()
        time.sleep(1)
        
        #选取企业地址
        driver.find_element_by_xpath("//*[@id='showMap']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='suggestId']").send_keys("乌鲁木齐站")
        driver.find_element_by_xpath("//*[@id='searchMapButton']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='MapClose']").click()
        time.sleep(2)
        
        #选择成立日期
        driver.find_element_by_xpath("//*[@id='enterprise-complete-form']/div[12]/div[2]/div/input").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[9]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        time.sleep(2)
        
        driver.switch_to.default_content()
        js = "window.scrollTo(0,500)" 
        driver.execute_script(js)
        driver.find_element_by_xpath("//*[@id='e_edit']").click()
        time.sleep(2)
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fmtb1("test_fmtb1"))
    results = unittest.TextTestRunner().run(suite)    