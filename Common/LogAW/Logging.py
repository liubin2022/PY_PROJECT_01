#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2016年8月21日
@author: LiuBin
@note: excel operation
"""

import logging
import logging.config
from Common.System.SystemAW import SystemAW

sys_aw = SystemAW()
project_path = sys_aw.get_project_path('PY_PROJECT_01')
logging.config.fileConfig(project_path + '\Common\LogAW\LoggerConf.ini')
# logging.config.fileConfig('E:\project\PY_PROJECT_V1R1C00\PythonAW\LoggingAW\LoggerConf.ini')
logger = logging.getLogger("root")
