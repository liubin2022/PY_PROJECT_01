#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: youdao.com
"""
import platform
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestYoudao(unittest.TestCase):
    def setUp(self):
        if platform.system() == 'Windows':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.FirefoxProfile()
        self.driver.implicitly_wait(3)
        self.base_url = "https://www.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element(By.ID, 'translateContent').clear()
        driver.find_element(By.ID, 'translateContent').send_keys(u"你好")
        driver.find_element(By.XPATH, '//button').click()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("hello", page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
