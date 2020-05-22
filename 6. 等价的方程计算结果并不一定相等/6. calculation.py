# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git\

import csv
import numpy as np

# 创建csv文件用来保存结果，首先写入各列名称
with open('data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x[0]', 'x[1]', 'y1', 'y2', 'y1 == y2?'])

# 执行10次
for i in range(10):
    x = np.random.rand(2)  # 生成（0,1）之间两个随机数
    y1 = x[0] ** 2 + 2 * x[0] * x[1] + x[1] ** 2  # y1 = x1^2 + 2x1x2 + x2^2
    y2 = (x[0] + x[1]) ** 2  # y2 = (x1 + x2)^2
    # 将结果存入data.csv，'a'表示以追加方式写入
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([x[0], x[1], y1, y2, y1 == y2])

