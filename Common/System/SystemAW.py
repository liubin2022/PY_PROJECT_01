#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2016年8月21日
@author: LiuBin
@note: excel operation
"""
import logging
import os
import platform
import sys

sys.path.append('..')


class SystemAW:
    def __init__(self):
        self.separator = ''

    def get_separator(self):
        if 'Windows' in platform.system():
            self.separator = '\\'
        else:
            self.separator = '/'
        return self.separator

    @staticmethod
    def get_system_type():
        if platform.system() == 'Windows':
            return 'Windows'
        elif platform.system() == 'Linux':
            return 'Linux'
        else:
            return 'other system'

    def get_project_path(self, project_dir_name):
        project_path = ''
        current_path = os.getcwd()
        separator = self.get_separator()
        current_path_list = current_path.split(separator)
        count = len(current_path_list)
        for index in range(0, count):
            project_path = project_path + separator + current_path_list[index]
            if current_path_list[index] == project_dir_name:
                return project_path.split(separator, 1)[1]
        return None

    @staticmethod
    def should_be_equal(str1, str2):
        assert str1 == str2

    @staticmethod
    def should_contain(str1, str2):
        assert str2 in str1


if __name__ == '__main__':
    common_aw = SystemAW()
    project_dir = common_aw.get_project_path('PY_PROJECT_01')
    print(project_dir)
