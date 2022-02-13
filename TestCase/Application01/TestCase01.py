#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: excel operation
"""


class TestCase01(object):
    def __init__(self):
        pass

    def aaa(self):
        dic = {}  # 定义一个字
        dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
        print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
        exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
        print(dic.keys())  # exec 后，dic 的 key 多了一个


if __name__ == '__main__':
    dic = {}  # 定义一个字
    dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
    print(dic.keys())  # 先将 dic 的 key 打印出来，有一个元素 b
    exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
    print(dic.keys())  # exec 后，dic 的 key 多了一个
