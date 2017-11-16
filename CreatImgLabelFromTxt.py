#coding:utf-8
'''
根据下载的坐标信息来创建Label图，然后进行不规则图形区域绘制坐标信息
'''
from PIL import Image
from PIL import ImageDraw

f=open("317639a9-4f1e-4092-bbd3-a0f42a042f2e.txt")
lines = f.readlines()
len1=len(lines)
i=0
L=[]

def roiTest():
    x=0
    srcImg = Image.new('L',(28827,35444))
    draw = ImageDraw.Draw(srcImg)
    global i
    for line in lines:
        line = line.split()
        L.append(line)
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


    srcImg.save('newGray.png')



if __name__ == '__main__':
    roiTest()
