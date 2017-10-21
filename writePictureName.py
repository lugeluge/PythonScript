# coding=UTF-8（等号换为”:“也可以）
import os
import shutil

path='E:/caffe/caffe cudnn/caffe/fcn.berkeleyvision.org-master/data/pascal/MYVOC/SegmentationClass'
fileList = os.listdir(path)
fileListNum = len(fileList)
fp = open('E:/caffe/caffe cudnn/caffe/fcn.berkeleyvision.org-master/data/pascal/MYVOC/ImageSets/Segmentation/val.txt', 'w')  # r只读，w可写，a追加
#以图片不带后缀的文件名进行排序，不能出现字母，只能是数字
def numberList():
    filename=[]
    for j in fileList:
        (myfilename,myextension)=os.path.splitext(j)#获取文件名和后缀名
        filename.append(int(myfilename))
    filename.sort()

    for i in filename:
        fp.write(str(i)+"\n")
#以string文件名进行排序
def stringList():
    for i in fileList:
        (myfilename, myextension) = os.path.splitext(i)  # 获取文件名和后缀名
        fp.write(myfilename+"\n")
def randomList(num):
    count=0
    sum=0
    for i in fileList:
        (myfilename, myextension) = os.path.splitext(i)
        if (count%num==0):
            fp.write(myfilename + "\n")
            sum=sum+1
        count=count+1
    print sum
if __name__ == '__main__':
    #numberList()  #图片名称是数字时，可以选择该函数，以数字大小排序
    #stringList()
    num = 5
    randomList(num)
    print('done')
