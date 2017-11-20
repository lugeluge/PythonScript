#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import os
import numpy as np


# 图片裁剪
# crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数,特别注意是元组
# 各元素为（left, upper, right, lower），
# （距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
# 坐标系统的原点（0, 0）是左上角。

# 图片裁剪并保存，因为图片在最后不一样大，所以需要判断，是不是最后一个
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
            cutImg.save(changePath + '0_f_0_%s_%s.png' % (j, i))
            print('%d_%d' % (i, j))


def multCut(pngName):
    img = Image.open('F:/Pathanalysis/%s.png' % pngName)
    # 创建路径
    changePath = "F:/Pathanalysis/change/imgCut/" + pngName[:4] + '/'  # 左闭右开区间
    if not os.path.exists(changePath):
        print('不存在要改变的路径', changePath)
        os.mkdir(changePath)
        print('创建成功')
    # 原图片宽高
    width = img.size[0]
    height = img.size[1]
    # 要裁剪的图片大小
    changeSize = 256
    mode = img.mode  # 图片rgb还是其他
    print(mode)  # 这里需要的是 P 模式，博客是用matlab代码进行的格式转换，python转换的p模式不知能不能用
    print(img.format)  # 图片格式
    cutImg(img, width, height, changeSize, changePath)
    img.close()


if __name__ == '__main__':
    name = ['0f83c078-f8c2-4ebc-afab-844209241f06', '2e956431-326d-42b2-bc83-4b5308bfd8f4',
            '15abcdb3-3bf7-48b3-9a1d-5be79aec66ec',
            '42bb1ded-7f48-4a83-a56b-a8e748ad2362', 'c8c0c1e2-3546-4f16-857d-8e53f6c08321',
            'c5703c0f-17fe-4d23-af20-f339d72ec354',
            'ffe2f7cf-fcd2-45db-9cd7-474af98992fc']
    for i in name:
        print(i)
        #multCut(i)
    print('done')
    multCut('317639a9-4f1e-4092-bbd3-a0f42a042f2e')
