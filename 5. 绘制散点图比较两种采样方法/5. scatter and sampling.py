# -*- coding: utf-8 -*-
# @Author: AlvinPy
# @github: https://github.com/AlvinPy/PythonTutorials.git
# @码云：https://gitee.com/alvinfeng/PythonTutorials.git\

# 导入所需模块
import matplotlib.pyplot as plt
import numpy as np
import lhsmdu

# 分别采用numpy里的随机数算法和lhs算法生成(-1, 1)之间的随机数
x1 = np.random.rand(20) * 2 - 1
x2 = np.array(lhsmdu.sample(1, 20)) * 2 - 1
y1 = 2 * x1
y2 = 2 * x2

# 画第一个子图
plt.subplot(2, 1, 1)  # (2, 1, 1)表示图有2行1列， 现在画第1个
plt.scatter(x1, y1, alpha=0.6)  # alpha是透明度
plt.title('numpy.random.rand')
plt.xlim([-1, 1])
plt.ylim([-2, 2])

plt.subplot(2, 1, 2)  # 画第二个
plt.scatter(x2, y2, alpha=0.6)
plt.title('lhsmdu')
plt.xlim([-1, 1])
plt.ylim([-2, 2])

plt.subplots_adjust(hspace=0.4, wspace=0)  # 设置两图间隔
plt.show()


