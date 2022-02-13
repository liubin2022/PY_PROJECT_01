#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2016年8月21日
@author: LiuBin
@note: excel operation
"""


class Env():
    def __init__(self):
        self.LIST__FILE_NAME_01 = ['d:\\textopenpyxl.xlsx','d:\\textopenpyxl.xlsx']

if __name__ == '__main__':
    env = Env()
    print env.LIST__FILE_NAME_01[0]
