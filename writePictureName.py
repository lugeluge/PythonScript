'''
批量读取文件名，并写入txt文件中
'''
import os
import shutil

path = 'C:/Users/Administrator/Desktop/imgcut'
fileList = os.listdir(path)
fp = open('C:/Users/Administrator/Desktop/f1.txt', 'w')  # r只读，w可写，a追加
#以图片不带后缀的文件名进行排序，不能出现字母，只能是数字
def numberList():
    filename=[]
    for j in fileList:
        (myfilename,myextension)=os.path.splitext(j)#获取文件名和后缀名
        filename.append(int(myfilename))
    filename.sort()

    for i in filename:
        fp.write(str(i)+".png"+"\n")
#以string文件名进行排序
def stringList():
    for i in fileList:
      fp.write(i+"\n")
if __name__ == '__main__':
    numberList()
    #stringList()
    print('done')
