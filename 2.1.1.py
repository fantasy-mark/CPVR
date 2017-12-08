# *_*coding:utf-8 *_*
from PIL import Image
from numpy import *
from pylab import *
import harris

im = array(Image.open('test1.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
imshow(harrisim)
# 参数3为角点阈值, 观察不同阈值(0.01-0.5)
filtered_coords = harris.get_harris_points(harrisim, 6, 0.02)
harris = harris.plot_harris_points(im, filtered_coords)
