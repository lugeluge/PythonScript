#-*- coding:utf-8 -*-

"""
提取图片轮廓
"""
import cv2
from PIL import Image
import numpy as np
label=cv2.imread('C:/users/luchi/desktop/23.png')
img = cv2.imread('C:/users/luchi/desktop/2e.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#i = Image.fromarray(binary)
#print i.getcolors()
image, cnts ,hierarchy= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print cnts,'cets'
#print hierarchy
cv2.drawContours(img, cnts, -1, (0, 0, 255), 3)
cv2.imwrite('C:/users/luchi/desktop/my.jpg',img)
cv2.imshow("img", img)
cv2.waitKey(0)
