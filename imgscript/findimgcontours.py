#-*- coding:utf-8 -*-

"""
提取图片轮廓
"""
import cv2
from PIL import Image
import numpy as np
label=cv2.imread('F:/Pathanalysis/change/newtwo/testlabel/0c3d/0c3dgray.png')
img = cv2.imread('F:/Pathanalysis/change/newtwo/testlabel/0c3d/hybrid.jpg')
gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
#i = Image.fromarray(binary)
#print i.getcolors()
image, cnts ,hierarchy= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print cnts,'cets'
#print hierarchy
cv2.drawContours(img, cnts, -1, (255, 0, 0),10)
cv2.imwrite('F:/Pathanalysis/change/newtwo/testlabel/0c3d/hybrid.jpg',img)
print 'done'
# cv2.imshow("img", img)
# cv2.waitKey(0)
