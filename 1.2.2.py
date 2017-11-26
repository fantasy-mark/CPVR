# *_*coding:utf-8 *_*
from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('test1.jpg').convert('L'))

# 新建一个图像
figure()
# 转化为灰度图
gray()
# 在原点左上角显示轮廓图像
contour(im, origin = 'image')
title('Convert to gray picture')
axis('equal')
axis('off')

figure()
title('Flatten the array, then total gary-value')
# 对数组进行一维化处理, 输出灰度直方图
hist(im.flatten(), 128)

show()
