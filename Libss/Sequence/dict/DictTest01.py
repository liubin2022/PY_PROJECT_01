#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2022年1月24日
@author: LiuBin
@note: dict
"""

from robot.libraries.BuiltIn import BuiltIn
from Common.Excel.OperateExcel import OperateExcel


class DictTest02:
    builtIn_aw = BuiltIn()
    excel_aw = OperateExcel()


    def __init__(self):
        self.builtin_aw = BuiltIn()

    def should_be_equal(self, first, second):
        self.builtin_aw.should_be_equal(self, first, second)


if __name__ == '__main__':
    builtin_aw = BuiltIn()
    # 步骤
    res01 = {
        "ready.test": "准备测试",
        "exec.test": "测试执行",
        "start.exec":"开始执行",
        "end.test": "测试结束"
    }

    # execl
    res02 =[["准备测试","aa","bb"],
            ["测试执行","aa","bb"],
            ["开始执行","aa","bb"],
            ["测试结束","aa","bb"]]

    # 步骤
    test = [{
                "opt": "ready.test",
                "startTime": "aa",
                "endTime": "bb"
            },
            {
                "opt": "exec.test",
                "startTime": "aa",
                "endTime": "bb",
                "testing": {"opt": "start.exec", "startTime": "aa", "endTime": "bb"}
            },
            {
                "opt": "end.test",
                "startTime": "aa",
                "endTime": "bb"
            }]
    test1 = {}
    d = {}
    ja = 3
    x = 0
    for i in test:
        # print(i)

        y =0
        for j in i:
            # print(j)

            # if j == "testing":
            #     print(j)
            #     print(j["opt"])
            #     print(j["startTime"])
            #     print(j["endTime"])
            if j == "opt":
                if  j == "testing":
                    print(i[j]["opt"])
                # print(res01[i[j]])
                builtin_aw.should_be_equal(res01[i[j]], res02[x][y])
            y +=1
        x += 1



