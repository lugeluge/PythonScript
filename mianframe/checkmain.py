#coding:utf-8
"""

"""
from PIL import Image
from PIL import ImageDraw
import os
import cv2
import shutil

def cutImg(img, width, height, changeSize, changePath,flag):
    count=0
    for i in range(width // changeSize + 1):
        for j in range(height // changeSize + 1):
            if (i == width // changeSize and j == height // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + width % changeSize,
                                   j * changeSize + height % changeSize))
            elif (i == width // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + width % changeSize,
                                   j * changeSize + changeSize))
            elif (j == height // changeSize):
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + changeSize,
                                   j * changeSize + height % changeSize))
            else:
                cutImg = img.crop((i * changeSize, j * changeSize, i * changeSize + changeSize,
                                   j * changeSize + changeSize))
            if flag:
                cutImg.putpalette([0, 0, 0, 0, 0,255, 0, 255,0])  # 每三个值表示一个rgb值
                cutImg.save(changePath + '0_f_0_%s_%s.png' % (j, i))
            count+=1
            #print('%d_%d' % (i, j))


def multCut(path,changePath,flag=True):
    """

    :param path: 要打开的图片的路径
    :param changePath: 裁剪图片存放路径
    :return:
    """
    img = Image.open(path)
    # 创建路径
    ifexistpath(changePath)
    # 原图片宽高
    width = img.size[0]
    height = img.size[1]
    # 要裁剪的图片大小
    changeSize = 256

    cutImg(img, width, height, changeSize, changePath,flag)
    img.close()

def ifexistpath(path, flag=True):
    """
    判断路径是否存在
    :param path:输入要判断的路径
    :param flag: 如果不存在默认创建，不创建请重新赋值
    :return:
    """
    if not os.path.exists(path):
        print('不存在要改变的路径', path)
        if flag:
            os.mkdir(path)
            print('创建成功')
    else:
        print '路径已存在'
def Binarization(src):
    """
    二值化图片
    :param src:
    :return: 返回黑色是否大于2000 如果大于返回false
    """
    img = cv2.imread(src)  # numpy数组类型
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    # cv2.imwrite('C:/users/luchi/desktop/df58black.jpg', binary)
    img = Image.fromarray(binary)
    type = img.getcolors()
    if int(type[0][1]) == 0 and int(type[0][0]) > 2000:
        return False
    return True


def gettrain(path, movepath):
    """
    图片二值化，并判断有没有细胞
    :param path: 要判断二值化的图片文件夹
    :param movepath: 没有细胞复制图片的文件夹
    """

    ifexistpath(path, flag=False)
    ifexistpath(movepath,flag=True)
    imglist = os.listdir(path)
    for img in imglist:
        if Binarization(path + img):
            print img
            movepic(path + img, movepath + img)



def movepic(path, movepath):
    os.rename(path, movepath)
def twoclasses(txt_path,save_path,name):
    """
    :param txt_path: 文本所在文件夹
    :param save_path: 保存路径
    :param name: 要打开的文件名
    :return:
    """
    txt_path=txt_path+name+'.txt'
    ifexistpath(save_path)
    f = open(txt_path)
    lines = f.readlines()
    len1 = len(lines)
    i = 1
    L = []
    x = 0

    for line in lines:
        line = line.split()
        L.append(line)
    widht, height = int(L[0][0]), int(L[0][1])
    srcImg = Image.new('L', (widht, height))
    draw = ImageDraw.Draw(srcImg)
    while int(i) < len1:
        b = []
        for j in range(i + 2, i + 2 + int(L[i][0])):
            x, y = L[j][0].split(',')
            b.append(float(x))
            b.append(float(y))
        b = tuple(b)
        if L[i + 1][1] == '255':  # L[i+1]是颜色rgb   特别注意
            x = 1
        if L[i + 1][2] == '255':
            x = 1
        draw.polygon(b, x)
        i = i + 2 + int(L[i][0])

    srcImg.save(save_path + name + '.png')
    f.close()
    srcImg.close()
def imgList(path):
    filename = []
    imglist = os.listdir(path)
    for j in imglist:
        (myfilename, myextension) = os.path.splitext(j)  # 获取文件名和后缀名
        filename.append(myfilename)
    return filename

def movepicfromList(path,imglist,movepath):
    """

    :param path: 文件存在的路径
    :param imglist: JPEGImages中存在的文件
    :param movepath: 移动的文件夹
    :return:
    """
    ifexistpath(movepath)
    filelist = os.listdir(path)
    for img in filelist:
        (myfilename, myextension) = os.path.splitext(img)  # 获取文件名和后缀名
        if myfilename in imglist:
            shutil.move(path+img,movepath)#movepath 是一个文件夹

if __name__ == '__main__':

    path='F:/Pathanalysis/change/newtwo/'

    name=['2e956431-326d-42b2-bc83-4b5308bfd8f4','0c3d12d3-f8cc-4b96-9499-9c996d5fde77']
    # 二值化图片,并写入文件夹
    picname=[]
    for i in name:
        trainpath=path+'original/'+i+'/'
        nocell=path+'original/nocell/'+str(i)+'/'
        gettrain(trainpath,nocell)

    print '二值化完成'

    #制作label图
    for i in name:
        twoclasses(path+'txt/',path+'biglabel/',i)
        multCut(path+'biglabel/'+i+'.png',path+'biglabel/'+i+'/')
    print '索引图制作完成'

    #根据jpg中的图片来移动索引图
    for i in name:
        imglist = imgList(path+'original/'+i+'/')
        labelimg =path+'biglabel/'+i+'/'
        movepath = path+'testlabel/'+i+'/'
        movepicfromList(labelimg, imglist, movepath)
        print 'label图片移动完毕，和JPEGIimages中一致'
    print 'lablel制作完成'
