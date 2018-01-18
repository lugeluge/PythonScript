# coding:utf-8
import cv2
import numpy as np
canvas=np.zeros((300,300,3),dtype='uint8')
list=[(130,120),(100,180),(130,240),(160,200)]
contours=np.array(list)  #构造轮廓
cv2.polylines(canvas,[contours],True,(0,0,255),2) #画多边形
x,y,w,h=cv2.boundingRect(contours)
cv2.rectangle(canvas,(x,y),(x+w,y+h),250,1)
rect=cv2.minAreaRect(contours)
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(canvas,[box],0,(0,255,0),2)
cv2.imshow("test",canvas)
cv2.waitKey(0)
