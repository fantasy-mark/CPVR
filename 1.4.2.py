# *_*coding:utf-8 *_*
from PIL import Image
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('test1.jpg').convert('L'))
gray()
imshow(im)

sigma = 5   # 标准差

# Sobel导数滤波器
imx = zeros(im.shape)
# filters.sobel(im, 1, imx)
filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
figure()
imshow(imx)

imy = zeros(im.shape)
# filters.sobel(im, 1, imy)
filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)
figure()
imshow(imy)

magnitude = sqrt(imx**2 + imy**2)
figure()
imshow(magnitude)

show()