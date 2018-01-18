#coding:utf-8
"""
测试numpy数组操作
"""
import numpy as np
from PIL import Image
# path='E:\\caffe\\caffe cudnn\\caffe\\fcn.berkeleyvision.org-master\\data\\pascal\\MYVOC\\JPEGImages\\0_45.jpg'
# img=Image.open(path)
# arr=np.array(img,dtype=np.float32)
# print arr.shape
# arr=arr[:,:,::-1]
# print arr
# arr=arr.transpose((2,0,1))
# print arr.shape
# print 'transpose'
# print arr


# a=np.arange(196608).reshape((3,256,256))
# print a
# print a.shape
# print a[:,:,::-1]

#print a
# a = np.array([
#               [
#                   [1, 5, 5, 2],
#                   [9, -6, 2, 8],
#                   [-3, 7, -9, 1]
#               ],
#
#               [
#                   [-1, 5, -5, 2],
#                   [9, 6, 2, 8],
#                   [3, 7, 9, 1]
#               ]
#             ])
# b=np.argmax(a, axis=0)
# print b
# print b.shape
import numpy as np
a=np.arange(30).reshape(2,3,5)
print a
print 'transpose'
print a.transpose(1,0,2)
