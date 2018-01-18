#coding:utf-8
"""
训练完图片后计算图片的精确率，recall值
"""
from PIL import Image
import numpy as np
model = np.array(Image.open('F:/Pathanalysis/change/newtwo/testlabel/0c3d/middlemodel.png')).flatten()
print 'model'
label=np.array(Image.open('F:/Pathanalysis/change/newtwo/testlabel/0c3d/0c3dgray.png')).flatten()
print 'label'
tp = 0 #癌症相同 ture positive 相关正类
count = 0 #细胞对应相等
count1= 0 #细胞对应不等
fp =0   #癌症false positives 无关负类
fn=0    #癌症 false negatives 正类判定为负类
tn =0   #癌症 ture negatives  负类判定为负类
a=0
print '开始'
for i,j in zip(model,label):
    i=float(i)
    j=float(j)
    if i==j:
        count+=1
        if i==1:
            tp+=1


        if i==0:
            tn+=1
    else:
        count1+=1
        if i==1 and j==0:
            fp+=1
        if i==0 and j==1:
            fn+=1


print '该图片的像素对应相等率为:',float(count)/float(count+count1),'\%\n'
print '该图片的精确率为       :',float(tp)/float(tp+fp),'\%\n'
print '该图片的召回率为       :',float(tp)/float(tp+fn),'\%\n'
print '该图片的f值为         :',float(2*tp)/float(2*tp+fn+fp),'\%\n'