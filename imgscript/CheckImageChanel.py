# coding=utf-8
'''检测图片信息，甬道数，灰度信息等等'''
from PIL import  Image
import numpy as np
import os

#在移动文件的时候要注意改文件有没有打开，打开的话会报错WindowsError: [Error 32]
#表示该文件已被锁定
def check_img_size(path,changePath):  #获取图片大小，不是256的移走
    imglist =os.listdir(path)
    for img in imglist:
        pic =Image.open(path+img)
        width=pic.width
        height=pic.height
        pic.close()
        if width!=256 or height!=256:
            os.rename(path+img,changePath+img)

if __name__ == '__main__':
    # path='F:/Pathanalysis/change/twoclass/other/label/'
    # changePath='F:/Pathanalysis/change/twoclass/other/labelsmall/'
    # #check_img_size(path,changePath)
    # img = Image.open('F:/Pathanalysis/change/newtwo/testlabel/0c3d/model.png')
    # #img.putpalette([0,0,0,0,0,255,0,0,255]) #每三个值表示一个rgb值
    # print img.getcolors()
    # print img.mode
    # print np.unique(img)
    # nimg = np.array(img)
    # print nimg.dtype
    #
    # print 'done'

    path='F:/Pathanalysis/change/newtwo/testlabel/2e95/middlemodel.png'
    img = Image.open(path)
    img.putpalette([0, 0, 0, 0, 0, 255, 0, 255, 0])
    img.save(path)






    #img = Image.open('E:/lccode/python/PythonScript/0f83c078-f8c2-4ebc-afab-844209241f06.png')
    #imgary = np.array(img)
    #print img.getcolors()