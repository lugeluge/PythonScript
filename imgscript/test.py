#coding=utf-8
from PIL import Image
from PIL import ImageStat
import os
import cv2
import numpy as np
def Binarization(src):
    img = cv2.imread(src)   #numpy数组类型
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    #cv2.imwrite('C:/users/luchi/desktop/df58black.jpg', binary)
    img = Image.fromarray(binary)
    type = img.getcolors()
    if int(type[0][1])==0 and int(type[0][0])>3000:
        return True
    return False
def convertL(path):
    img = Image.open('C:/users/luchi/desktop/imgtest/2e.jpg')
    img2 = img.convert("L")
    img2.save('C:/users/luchi/desktop/imgtest/gray.jpg')
def getmean(path):
    width = 34085
    height = 30072
    x = width / 256
    y = height / 256
    img1 = Image.open(path + '0_f_0_0_0.jpg').convert('L')
    img2 = Image.open(path + '0_f_0_0_%s.jpg' % x).convert('L')
    img3 = Image.open(path + '0_f_0_%s_0.jpg' % y).convert('L')
    img4 = Image.open(path + '0_f_0_%s_%s.jpg' % (y, x)).convert('L')
    count = (int(ImageStat.Stat(img1).mean[0]) + int(ImageStat.Stat(img2).mean[0]) + int(
        ImageStat.Stat(img3).mean[0]) + int(ImageStat.Stat(img4).mean[0])) / 4
    return count

def gettrain(path):
    log = open('C:/users/luchi/desktop/imgtest/0c.txt','w')
    #mean = getmean(path)
    movepath='C:/users/luchi/desktop/imgtest/0cmove/'
    imglist=os.listdir(path)
    for img in imglist:
        if Binarization(path+img):
            print img
            movepic(path+img,movepath+img)
            log.write(img[:-4]+'\n')
    log.close()
def movepic(path,movepath):
    os.rename(path, movepath)
if __name__ == '__main__':
    path='C:/Users/luchi/Desktop/imgtest/0c3d12d3-f8cc-4b96-9499-9c996d5fde77/'
    gettrain(path)