# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git\

# 导入系统功能模块
import os

# 需要创建的文件夹数量
number = 5

# 逐个创建文件夹并复制相应的数据文件
for i in range(number):
    os.system('mkdir data' + str(i+1))
    os.system('copy .\\TotalData\\data' + str(i+1) + '.csv .\\data' + str(i+1))
