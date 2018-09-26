#coding=utf-8

'''
Created on 2018年9月17日
@author: Jerry
'''

import re, os, math
import unittest, doctest
import HTMLTestRunner
from XJBT import allcase_list

alltestnames = allcase_list.caselist()

suite = unittest.TestSuite()

if __name__ == '__main__':
# 这里我们可以使用defaultTestLoader.loadTestsFromNames(),
# 但如果不提供一个良好的错误消息时，它无法加载测试
# 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
            #循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print ('ERROR: Skipping tests from "%s".' % test)
            try:
                __import__(test)
            except ImportError:
                print ('Could not import the test module.')
            else:
                print ('Could not load the test suite.')
            from traceback import print_exc
            print_exc()
    print ('Running the tests...')
    
filename = 'D:\\XJBT_Result_20180926.html'
fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'新疆兵团安监平台自动化测试报告',
    description=u'用例执行情况：')

runner.run(suite)