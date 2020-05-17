# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git

# 导入需要使用的模块，pprint模块是为了格式化打印-
# 结果，一般情况下可不用
import csv

# 创建一个列表保存列名
title = ['input', 'output']
dataList = [] # 创建一个列表保存数据

# 读取所有文件
for i in range(5):
    with open('data' + str(i+1) + '.csv', 'r') as csvFile:
        csvFile.readline() # 跳过第一行
        reader = csv.reader(csvFile)
        for row in reader:
            dataList.append(row)

# 保存所有数据到data_all.csv文件
with open('data_all.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(title)
    writer.writerows(dataList)

