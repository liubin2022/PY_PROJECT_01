#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: str
"""

if __name__ == '__main__':
    test01 = '<p id="para">Hi.What would you like to order?</p>'
    test01 = test01.split('>')[1].split('<')[0]
    print(test01)
    test02 = '<input type="radio" name="gender" id="male" value="male">'
    test02 = test02.split('=')[1].split(' ')[0]
    test03 = '<li>Black tea</li>'
    test04 = '<li>Green tea</li>'
    print(test03.split('li>')[1].split('<')[0])
    print(test04.split('li>')[1].split('<')[0])
