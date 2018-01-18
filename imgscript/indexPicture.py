# coding:utf-8
'''
根据灰度图的值
制作索引图
'''
from random import randint
from PIL import Image
import os
path = r'F:\Pathanalysis\change\newtwo\testlabel\2e95\cvmodellabel/'
os.chdir(path)
imgList = os.listdir(path)
def randomPalette(length, min, max):
    return [randint(min, max) for x in xrange(length)]

for pic in imgList:
    print pic
    img = Image.open(pic)
    img.putpalette([0,0,0,0,0,255]) #每三个值表示一个rgb值
    img.save(path+pic)
print 'done'
# img = Image.open(path)
# img.putpalette([0,255,0,0,0,255]) #每三个值表示一个rgb值
# Image._show(img)