# *_*coding:utf-8 *_*
from PIL import Image
from numpy import *
from pylab import *
import pca

imlist = ['z1.jpg', 'z2.jpg', 'z3.jpg', 'z4.jpg', 'z5.jpg', 'z6.jpg', 'z7.jpg', 'z8.jpg']

im = array(Image.open(imlist[0]))   # 打开一副图像, 获取其大小
m, n = im.shape[0:2]                # 获取图像的大小
imnbr = len(imlist)                 # 获取图像的数目

# 创建矩阵, 图像数据所有一维化处理
immatrix = array([array(Image.open(im).convert('L')).flatten()
                  for im in imlist], 'f')

# 执行PCA操作
V, S, immean = pca.pca(immatrix)

# 显示一些图像(均值图像和前7各模式)
figure()
gray()
subplot(2, 4, 1)
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))

show()