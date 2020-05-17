# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git

# 导入需要使用的模块，pprint模块是为了格式化打印-
# 结果，一般情况下可不用
import csv
import pprint

# 创建列表用来存储文件中的数据
dataList = []

# 打开data.csv文件并按行存入dataList
with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        dataList.append(row)

# 打印dataList
pp = pprint.PrettyPrinter()
pp.pprint(dataList)


