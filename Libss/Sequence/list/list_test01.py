#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: dict
"""

if __name__ == '__main__':
    aa = ['a', 'b', 'e', 'c', 'd']
    bb = ['1', '3', '5', '4', '2']
    cc = ['aaaa', 'bbb', 'ee', 'c', 'dddddddd']
    print(sorted(aa))
    print(sorted(bb))
    cc.sort(key=len)
    bb.sort(reverse=True)
    print(cc)
    print(bb)
    x = 2
    y = 2
    print()
