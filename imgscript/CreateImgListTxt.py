#coding:utf-8
'''
将目录下的文件生成到txt文件中
'''
import os
path='F:\\Pathanalysis\\change\\newtwo\\testlabel\\2e95\\cvmiddlejpg\\'
log  =open('C:/users/luchi/desktop/cvmiddle.txt','w')
imglist = os.listdir(path)
for i in imglist:
    name,last=os.path.splitext(i)
    log.write(name+'\n')
log.close()