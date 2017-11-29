# *_*coding:utf-8 *_*
from imtools import *

im = array(Image.open('test1.jpg').convert('L'))
imshow(im)

figure()                # create new draw paper
hist(im.flatten(), 128)

figure()
im2, cdf = histeq(im)
imshow(im2)

figure()
hist(im2.flatten(), 128)

show()      # figure1 figure3 对比可见图像3层次更加分明, figure2 figure4 对比可见直方图4 更均衡
