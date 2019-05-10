#!/usr/bin/python3
#-*-coding:UTF-8-*-
#!@Author:lumm   
#!@Time:2019/4/1

from selenium import webdriver
import unittest,time

class BaiduTest(unittest.TestCase):#继承unittest.testCase各种断言方法

    def setUp(self):
        self.driver=webdriver.Chrome(r"E:\WorkSpace\python\PycharmProjects\applianxi\chromedriver.exe")
        self.driver.implicitly_wait(30) #隐性等待30s
        self.base_url='https://www.baidu.com'
        print('测试开始')

    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title,u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()
        print('测试完成')
if __name__ == '__main__':
    unittest.main()

