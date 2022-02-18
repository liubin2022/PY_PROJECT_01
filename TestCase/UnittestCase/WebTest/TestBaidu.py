#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: baidu.com
"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://www.baidu.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element(By.XPATH, '//input[@id="kw"]').clear()
        driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys(u"你好")
        driver.find_element(By.ID, 'su').click()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("你好，是一个汉语词语", page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
