# *_*coding:utf-8 *_*
from PIL import Image
from pylab import *

im = array(Image.open('test1.jpg'))
imshow(im)
print 'Please click 3 points'
# 在windows上测试在此时无法显示图像, 自然无法输入坐标
x = ginput()
print 'you clicked : ', x
show()