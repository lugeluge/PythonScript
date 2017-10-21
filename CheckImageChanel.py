# coding=utf-8
'''检测图片信息，甬道数，灰度信息等等'''
from PIL import  Image
import numpy as np
img = Image.open('C:/Users/luchi/Desktop/0F83_0_f_0_30_18.png')
img2 = Image.open('E:/caffe/caffe cudnn/caffe/fcn.berkeleyvision.org-master/data/pascal/VOC2012/SegmentationClass/2007_000032.png')
img3=Image.open('C:/Users/luchi/Desktop/ImageGrey.png')
print np.unique(img)
print np.unique(img2)
print  img.mode
print img2.mode
print img3.mode,'image3'