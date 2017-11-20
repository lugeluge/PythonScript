#coding:utf-8
'''
使用python 批量移动一个文件夹下的子文件夹中的内容到别的目录。该目录下的文件不受影响
该子文件如果有子文件结果未知
'''
import os
import shutil

path = "F:/Pathanalysis/change/imgCut/label/"
changPath = path
if not os.path.exists(path):
    print('不存在目录')
    exit()
if not os.path.exists(changPath):
    print('不存在要改变的路径', changPath)
    os.mkdir(changPath)
    print('创建成功')
listDir1 = os.listdir(path)  # 用list保存文件夹目录
listLen = len(listDir1)  # 有多少个子文件夹
print(listLen)
print(listDir1)
num=0
for j in range(listLen):

    print(listDir1[j])
    file = path + '/' + listDir1[j]
    isdir = os.path.isdir(file)
    if isdir:
        childPath = os.listdir(file)
        childLen = len(childPath)
        for k in range(childLen):
            result = file + '/' + childPath[k]
            childFileName = changPath + "/"+'1_'+str(num)+'.png'
            num=num+1
            print(childFileName)
            os.rename(result, childFileName)
        # 都移动完后判断是否是空文件夹，是就删除
        if not os.listdir(file):
            print('删除%s空文件'%listDir1[j])
            os.rmdir(file)
            # os.rename(src, dst) src -- 要修改的目录名  dst -- 修改后的目录名