#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
批量改变图片的灰度值 149改为1 29改为2 149是癌细胞29是正常细胞
'''
import numpy as np
import PIL.Image as Image
import os
path = 'E:\\caffe\\caffe cudnn\\caffe\\fcn.berkeleyvision.org-master\\data\\pascal\\MYVOC\\SegmentationClass'
changepath='E:\\caffe\\caffe cudnn\\caffe\\fcn.berkeleyvision.org-master\\data\pascal\\MYVOC\\change/'
os.chdir(path)
def changeGray():
    imageName = os.listdir(path)
    for name in imageName:
        img =Image.open(name)
        imarray=np.array(img)
        xlen = len(imarray[0])
        print xlen
        for i in range(xlen):
            for j in range(xlen):
                if imarray[i][j] == 149:
                    imarray[i][j] = 1
                if imarray[i][j] == 29:
                    imarray[i][j] = 2
        imgc = Image.fromarray(imarray)
        imgc.save(changepath+name)

if __name__ == '__main__':
    changeGray()
    print 'done'