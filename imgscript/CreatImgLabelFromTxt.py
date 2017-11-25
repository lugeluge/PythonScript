#coding:utf-8
'''
根据下载的坐标信息来创建Label图，然后进行不规则图形区域绘制坐标信息
'''
from PIL import Image
from PIL import ImageDraw


def roiTest(name):
    txt_path = 'F:/Pathanalysis/change/twoclasses/other/'
    pic_path = 'F:/Pathanalysis/change/twoclasses/other/pic/'
    f = open(txt_path+name + '.txt')
    lines = f.readlines()
    len1 = len(lines)
    i = 1
    L = []
    x=0

    for line in lines:
        line = line.split()
        L.append(line)
    widht,height=int(L[0][0]),int(L[0][1])
    srcImg = Image.new('L', (widht, height))
    draw = ImageDraw.Draw(srcImg)
    while int(i)<len1:
        print i
        print L[i+1]
        b=[]
        for j in range(i+2,i+2+int(L[i][0])):
            x,y= L[j][0].split(',')
            b.append(float(x))
            b.append(float(y))
        b=tuple(b)
        print b
        if L[i+1][1]=='255': #L[i+1]是颜色rgb
            x=1
        if L[i+1][2]=='255':
            x=2
        draw.polygon(b,x)
        i = i + 2 + int(L[i][0])


    srcImg.save(pic_path+name+'.png')
    f.close()
    srcImg.close()
def twoclasses(name):
    txt_path = 'F:/Pathanalysis/change/twoclasses/other/'
    pic_path = 'F:/Pathanalysis/change/twoclasses/other/pic/'
    f = open(txt_path+name + '.txt')
    lines = f.readlines()
    len1 = len(lines)
    i = 1
    L = []
    x=0

    for line in lines:
        line = line.split()
        L.append(line)
    widht,height=int(L[0][0]),int(L[0][1])
    srcImg = Image.new('L', (widht, height))
    draw = ImageDraw.Draw(srcImg)
    while int(i)<len1:
        print i
        print L[i+1]
        b=[]
        for j in range(i+2,i+2+int(L[i][0])):
            x,y= L[j][0].split(',')
            b.append(float(x))
            b.append(float(y))
        b=tuple(b)
        print b
        if L[i+1][1]=='255': #L[i+1]是颜色rgb
            x=0
        if L[i+1][2]=='255':
            x=1
        draw.polygon(b,x)
        i = i + 2 + int(L[i][0])


    srcImg.save(pic_path+name+'.png')
    f.close()
    srcImg.close()


if __name__ == '__main__':
    name=['0f83c078-f8c2-4ebc-afab-844209241f06','2e956431-326d-42b2-bc83-4b5308bfd8f4','15abcdb3-3bf7-48b3-9a1d-5be79aec66ec',
          '42bb1ded-7f48-4a83-a56b-a8e748ad2362','c8c0c1e2-3546-4f16-857d-8e53f6c08321','c5703c0f-17fe-4d23-af20-f339d72ec354',
          'ffe2f7cf-fcd2-45db-9cd7-474af98992fc','0c3d12d3-f8cc-4b96-9499-9c996d5fde77','317639a9-4f1e-4092-bbd3-a0f42a042f2e',
          'df58afcf-e5a5-4163-ba6b-1042cf0ec949']

    for i in name:
        print(i)
        #roiTest(i)
        twoclasses(i)

