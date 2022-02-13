#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: dict
"""

from robot.libraries.BuiltIn import BuiltIn


class aaa:
    builtIn_aw = BuiltIn()

    def __init__(self):
        self.builtin_aw = BuiltIn()

    def should_be_equal(self, first, second):
        self.builtin_aw.should_be_equal(self, first, second)


if __name__ == '__main__':
    test = 'aaabbbcccddaaffeeeffbb'
    d = {}
    for i in test:
        count = str(test.count(i))
        d.update({i: count})
    print(d)
    aa = ''
    bb = ''
    for j in d:
        aa = j + d[j]
        bb = bb + aa
    print(bb)
    dic = {}  # 定义一个字
    dic['b'] = 3  # 在 dic 中加一条元素，key 为 b
    print(dic.keys(), dic.values(), dic.items())  # 先将 dic 的 key 打印出来，有一个元素 b
    exec("a = 4", dic)  # 在 exec 执行的语句后面跟一个作用域 dic
    print(dic.keys())  # exec 后，dic 的 key 多了一个
    # 创建字典key
    aa = {}.fromkeys(['name', 'age'])
    print(aa)
