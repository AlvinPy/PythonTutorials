# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git\

# 导入所需模块
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)  # 离散x
y1 = 2 * x  # 一次函数
y2 = x ** 2  # 二次函数
y3 = 1. / 3 * x ** 3  # 三次函数

# 使用matplotlib画图，将三条曲线放在一张图中显示
plt.plot(x, y1, color='blue', label='y1')
plt.plot(x, y2, color='red', label='y2')
plt.plot(x, y3, color='black', label='y3')
plt.title('Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

