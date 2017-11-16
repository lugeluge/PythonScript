# coding:utf-8
'''
根据灰度图的值
制作索引图
'''
from random import randint
from PIL import Image


def randomPalette(length, min, max):
    return [randint(min, max) for x in xrange(length)]


path = 'C:/users/luchi/desktop/1_83.png'
img = Image.open(path)
# img.show()
i = randomPalette(768, 0, 255)
print i
print len(i)
img.putpalette([0,0,0,0,255,0,0,0,255]) #每三个值表示一个rgb值
print img
img.show()
img.save('C:/users/luchi/desktop/2.png')
