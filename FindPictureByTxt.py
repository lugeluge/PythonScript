'''
根据生成的train.txt文件中的信息来查找文件夹中的图片并保持到别的目录中
文本中的是png后缀，图片的是jpg后缀
'''
import os
fp = open('F:/Pathanalysis/change/VOC/train.txt', 'r')
path = 'F:/Pathanalysis/one/JPEGImages/' # 要查找的文件夹目录
changePath='F:/Pathanalysis/change/VOC/JPEGImages/'
picName=[]
fileList = os.listdir(path)
for i in fileList:
    (myfilename, myextension) = os.path.splitext(i)  # 获取文件名和后缀名
    picName.append(myfilename)
sourceLines = fp.readlines()#按行读取文件内容
for line in sourceLines:
    line=line.strip('\n')  #去除txt文本中的\n
    name=line.split('.')
    if name[0] in picName:
        oldPicPath=path+name[0]+'.jpg'
        newPicPath=changePath+name[0]+'.jpg'
        os.rename(oldPicPath, newPicPath)
print('done')