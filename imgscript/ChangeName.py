# encoding: utf-8
#批量修改文件名
import os
#path=input("输入文件路径（结尾加/)：")
path='F:/Pathanalysis/change/imgCut/3176/'


#获取该目录下的所有文件，存入列表中
f = os.listdir(path)
n=0
for i in f:
    #设置旧文件名（路径+文件名）
    oldName=path+i
    #设置新文件名
    newName = path+'1_'+str(n)+'.png'
    os.rename(oldName,newName)
    print(oldName,'==========>',newName)

    n+=1
