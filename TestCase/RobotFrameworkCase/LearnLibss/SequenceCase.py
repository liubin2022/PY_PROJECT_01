#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: excel operation
"""
import logging
from Libss.Sequence.dict.DictMethod import DictMethod


class SequenceCase:
    def __init__(self):
        self.dict_tmp = DictMethod()

    def dict_meth_case01(self):
        self.dict_tmp.sort_str('aaabbbcccddaaffeeeffbb')
        dic = {}  # 定义一个字
        dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
        print(dic)
        print(dic.values())
        print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
        exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
        print(dic.keys())  # exec 后，dic 的 key 多了一个

    def dict_meth_case02(self):
        try:
            self.dict_tmp.sort_str('aaaeeffbb')
            dic = {}  # 定义一个字
            dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
            print(dic)
            print(dic.values())
            print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
            exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
            print(dic.keys())  # exec 后，dic 的 key 多了一个
        except Exception as e:
            logging.Logger('webtc')
            print(e)

    def dict_meth_case03(self):
        try:
            self.dict_tmp.sort_str('bbderadsfutyutz')
            dic = {}  # 定义一个字
            dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
            print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
            exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
            print(dic.keys())  # exec 后，dic 的 key 多了一个
        except Exception as e:
            logging.Logger('webtc')
            print(e)


if __name__ == '__main__':
    aa = SequenceCase()
    aa.dict_meth_case01()
    aa.dict_meth_case02()
    aa.dict_meth_case03()
