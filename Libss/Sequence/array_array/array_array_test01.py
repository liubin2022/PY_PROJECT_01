#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: array.array
"""

if __name__ == '__main__':
    a = ('a', 'b', ['A', 'B', 'C'])
    print a
    a[2][0] = 'x'
    a[2][1] = 'y'
    print a
    bytes = 'aaaadfddeeff'
    print bytes.count('a', 'd')