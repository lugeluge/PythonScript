# coding=UTF-8（等号换为”:“也可以）
import os
import shutil

path='F:/Pathanalysis/change/twoclasses/JPEGImages/'
fileList = os.listdir(path)
fileListNum = len(fileList)
fp = open('train1.txt', 'w')  # r只读，w可写，a追加
#以图片不带后缀的文件名进行排序，不能出现字母，只能是数字
def numberList():
    filename=[]
    for j in fileList:
        (myfilename,myextension)=os.path.splitext(j)#获取文件名和后缀名
        filename.append(int(myfilename[2:]))
    filename.sort()

    for i in filename:
        fp.write('1_'+str(i)+"\n")
#以string文件名进行排序
def stringList():
    for i in fileList:
       # (myfilename, myextension) = os.path.splitext(i)  # 获取文件名和后缀名
        fp.write(i+" 0\n")
        #fp.write(i+"\n")
def randomList(num):
    f = open('E:/caffe/caffe cudnn/caffe/fcn.berkeleyvision.org-master/data/pascal/MYVOC/train.txt', 'r')
    lines=f.readlines()
    for (line,i )in zip(lines,range(len(lines))):
        line = line.strip('\n')
        if i%num ==0:
            fp.write(line+"\n")


if __name__ == '__main__':
    #numberList()  #图片名称是数字时，可以选择该函数，以数字大小排序
    stringList()
    num = 5
    #randomList(num)
    print('done')
