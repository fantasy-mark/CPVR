# *_*coding:utf-8 *_*
from pylab import *
from numpy import *
from numpy import random
from scipy.ndimage import filters
import rof

# 使用噪声创建合成图像
im = zeros((500, 500))
gray()

im[100:400, 100:400] = 128
im[200:300, 200:300] = 255
im = im + 30 * random.standard_normal((500, 500))
title('raw picture')
imshow(im)

U, T = rof.denoise(im, im)
G = filters.gaussian_filter(im, 10)

figure()
title('Gaussian filter')
imshow(G)

figure()
title('ROF denoise')
imshow(U)

show()

# 保存生成结果
# from scipy.misc import imsave
# imsave('synth_rof.pdf', U)
# imsave('synth_gaussian.pdf', G)