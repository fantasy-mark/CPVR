# *_*coding:utf-8 *_*
import numpy as np
import matplotlib.pyplot as plt

# pyplot用于绘制函数曲线图
x = np.arange(-1, 3, 0.1)
y = 2 ** x

plt.plot(x, y)
plt.yticks([1], [r'1'])
ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# plt.plot(0, 1)

plt.show()
