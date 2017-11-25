# coding:utf-8
'''
要与原图大小相同
测试alpha甬道
'''
from PIL import Image


def hideInfoInImage(img, info):
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    if info.mode != 'L' and info.mode != '1':
        info = info.convert('L')
    img.putalpha(info)
    return img


if __name__ == '__main__':
    path1 = 'C:/users/luchi/desktop/2.jpg'
    path2 = 'C:/users/luchi/desktop/2.jpg'
    band = Image.open(path1)
    img = Image.open(path2)
    img = hideInfoInImage(img,band)
    img.show()# 把band隐藏到alpha甬道,y原图看上去没有变化
    img.split()[3].show() #抽取透明甬道并显示
    img.save('C:/users/luchi/desktop/4.png')
