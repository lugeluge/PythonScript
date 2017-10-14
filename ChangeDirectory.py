'''
使用python 批量移动文件从一个文件夹移动到另一个文件夹
'''
import os
import shutil
path="C:/Users/Administrator/Pictures/3"
changPath ="C:/Users/Administrator/Pictures/4"
if not os.path.exists(path):
    print('不存在目录')
    exit()
if not os.path.exists(changPath):
    print('不存在要改变的路径',changPath)
    os.mkdir(changPath)
    print('创建成功')
listDir1 = os.listdir(path)
listLen = len(listDir1)
print(listLen)
print(listDir1)
for j in range(listLen):

    print(listDir1[j])
    file = path+'\\'+listDir1[j]
    isdir = os.path.isdir(file)
    if isdir:
        childPath = os.listdir(file)
        childLen = len(childPath)
        for  k in range(childLen):
            result  = file+'/'+childPath[k]
            childFileName = changPath+"/"+childPath[k]
            print(childFileName)
            os.rename(result,childFileName)
#os.rename(src, dst) src -- 要修改的目录名  dst -- 修改后的目录名