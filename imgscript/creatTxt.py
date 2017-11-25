#coding:utf-8
'''
创建txt文件
'''
import os
train=open('train.txt',"w")
val = open('val.txt',"w")
test = open("test.txt","w")
imglist=os.listdir('F:/Pathanalysis/change/twoclasses/JPEGImages/')
lengh=len(imglist)
filename=[]
for name in imglist:
    (myfilename, myextension) = os.path.splitext(name)  # 获取文件名和后缀名
    filename.append(int(myfilename[2:]))
filename.sort()
for index,img in enumerate(filename):
    if index%6==0:
        val.write('1_'+str(img)+'\n')
    elif index%6==1:
        test.write('1_' + str(img) + '\n')
    else:
        train.write('1_' + str(img) + '\n')
train.close()
val.close()
test.close()
print 'done'