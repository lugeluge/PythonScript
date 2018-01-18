# -*- coding:utf-8 -*-
# 图片拼接
import PIL.Image as Image
import os, sys

mw = 256 # 图片大小+图片间隔
ms = 5

msize = mw * ms


fpre = "x" #图片前缀
toImage = Image.new('RGB', (msize, msize))

for y in range(1, 48):  ## 先试一下 拼一个5*5 的图片
    for x in range(1, 99):

        # 之前保存的图片是顺序命名的，x_1.jpg, x_2.jpg ...
        fname = "0_f_0_%d_%d.jpg"%y%x

        fromImage = Image.open(fname)
        #fromImage =fromImage.resize((mw, mw), Image.ANTIALIAS)   # 先拼的图片不多，不用缩小

        toImage.paste(fromImage, ((x-1) * mw, (y-1) * mw))

toImage.save('E:\MGCache\image.jpg')
