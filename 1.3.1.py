# *_*coding:utf-8 *_*
from PIL import Image
from pylab import *

im = array(Image.open('test1.jpg'))
print im.shape, im.dtype

im = array(Image.open('test1.jpg').convert('L'))
print im.shape, im.dtype

# 灰度变化
im2 = 255 - im                  # 反相
im3 = (100.0/255) * im + 100    # 色度变换到100...200
im4 = 255.0 * (im/255.0) ** 2   # 对色度平方

imshow(im)
figure()
imshow(im2)
figure()
imshow(im3)
figure()
imshow(im4)
show()