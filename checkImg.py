'''
判断图片是否是单一的黑色，如果是就移走
'''
from PIL import Image
import  os
path='C:/Users/Administrator/Desktop/imgcut'
changPath = "C:/Users/Administrator/Desktop/black"
if not os.path.exists(changPath):
    print('不存在要改变的路径',changPath)
    os.mkdir(changPath)
    print('创建成功')
#image = Image.open('C:/Users/Administrator/Desktop/imgcut/1.png')
imgList =os.listdir(path)
for i in imgList:
    image = Image.open(path+"/"+i)
    type = image.getcolors() #获取每种图片的种类颜色和数量 返回一个list 类型
    count = int(type[0][1][0])+int(type[0][1][1])+int(type[0][1][2])
    # [(31695, (8, 255, 0)), (33841, (0, 0, 0))] list 然后是嵌套元组
    typeNum =len(type) #获取颜色数量
    #print(type[0][1][0]) #获取 第一个list中的r甬道颜色
    #print(type)#打印获取到的值
    #print(typeNum) #打印颜色数量
    #print('打印颜色rgb的和',count)# 打印颜色rgb的和
    if(typeNum==1 and count==0):
        print("这张图片是黑色的")
        os.rename(path+"/"+i,changPath+"/"+i)
    else:
        print("不是黑色")

print('done')