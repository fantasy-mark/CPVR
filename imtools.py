# -*- coding = utf-8 -*-
import os

def get_imlist(path):
    """ 返回目录所有JPG图像的文件名列表 """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]