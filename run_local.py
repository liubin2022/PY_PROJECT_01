#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: array.array
"""


import sys
import os

#sys.argv[0]=run_local.py

#sys.argv[1]=aa

#pybot -i "sys.argv[0]" -d result Suites

#print 'Argument List:', str(sys.argv[1])

#os.system("pybot -t %s -d result Suites>>ping_result" % sys.argv[1])

#robot --outputdir /tmp/xcloud/result/ /tmp/xcloud/PY_PROJECT_01/Suite/TestCase01/TC_001.robot
#robot -t testcast0001 -d /tmp/xcloud/result/ /tmp/xcloud/PY_PROJECT_01/Suite


# os.system("robot %s %s -d results %s" % (sys.argv[1], sys.argv[2], sys.argv[3]))
# run_local.py -t testcase001 Suite


def main(args):
    print(args)
    print(' '.join(args))
    log_dir = 'results'
    os.system('robot --outputdir "%s" %s' % (log_dir, ' '.join(args)))


if __name__ == '__main__':
    main(sys.argv[1:])
