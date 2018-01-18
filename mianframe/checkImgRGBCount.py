#-*- coding:utf-8 -*-

"""
提取图片轮廓
"""
import cv2
from PIL import Image
import os
import numpy as np
def getInfo(img):
    type = img.getcolors()
    return type
def Binarization(src):
    img = cv2.imread(src)   #numpy数组类型
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #cv2.imwrite('C:/users/luchi/desktop/black2.jpg', binary)
    return binary
def cutImg(img, width, height, changeSize, changePath):
    for i in range(width // changeSize + 1):
        for j in range(height // changeSize + 1):
            if (i == width // changeSize and j == height // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + width % changeSize,
                                   j * changeSize + height % changeSize))
            elif (i == width // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + width % changeSize,
                                   j * changeSize + changeSize))
            elif (j == height // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + changeSize,
                                   j * changeSize + height % changeSize))
            else:
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + changeSize,
                                   j * changeSize + changeSize))

            type=getInfo(cutImg)
            txt.write('%d_%d' % (j, i) + str(type) + '\n')
            cutImg.save(changePath + '0_f_0_%s_%s.png' % (j, i))
            cutImg.close()
            print('%d_%d' % (j, i))

def multCut(img,path):

    if not os.path.exists(path):
        print('不存在要改变的路径', path)
        os.mkdir(path)
        print('创建成功')
    # 原图片宽高
    width = img.size[0]
    height = img.size[1]
    # 要裁剪的图片大小
    changeSize = 256
    mode = img.mode  # 图片rgb还是其他
    print(mode)  # 这里需要的是 P 模式，博客是用matlab代码进行的格式转换，python转换的p模式不知能不能用
    print(img.format)  # 图片格式
    cutImg(img, width, height, changeSize, path)
    img.close()
def movepic():
    txt = open()
if __name__ == '__main__':
    path='C:/users/luchi/desktop/2e.jpg'

    savePath=path[:-4]+"/"
    txt = open(savePath + 'log.txt', 'w')
    img=Binarization(path)
    img=Image.fromarray(img)
    multCut(img,savePath)
    txt.close()