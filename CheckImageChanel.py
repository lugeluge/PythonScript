# coding=utf-8
'''检测图片信息，甬道数，灰度信息等等'''
from PIL import  Image
import numpy as np
img = Image.open('E:/lccode/python/PythonScript/newGray.png')
imgary = np.array(img)
print img.getcolors()
