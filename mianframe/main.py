# -*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageDraw
import os
import cv2
import shutil
import datetime

"""
制作病理图数据集的主要程序
1. 数据集的根目录中要有 original 文件夹，里面存放
下载的数据
2. 有txt文件夹，里面存放坐标
注意第一行放的是图像宽高，用空格间隔
"""


def twoclasses(txt_path, save_path, name):
    """

    :param txt_path: 文本位置
    :param save_path: 保存路径
    :param name: 要打开的文件名
    :return:
    """
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
        if int(L[i][0]) >= 3:
            draw.polygon(b, x)
        i = i + 2 + int(L[i][0])
    srcImg.putpalette([0, 0, 0, 0, 0, 255])  # 每三个值表示一个rgb值                     注意是否需要修改
    srcImg.save(save_path + name + '.png')
    f.close()
    srcImg.close()


# 图片裁剪
# crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数,特别注意是元组
# 各元素为（left, upper, right, lower），
# （距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
# 坐标系统的原点（0, 0）是左上角。

# 图片裁剪并保存，因为图片在最后不一样大，所以需要判断，是不是最后一个
def cutImg(img, width, height, changeSize, changePath, num, flag):
    count = 0
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
                cutImg.putpalette([0, 0, 0, 0, 0, 255, ])  # 每三个值表示一个rgb值    #注意是否需要修改
                cutImg.save(changePath + '0_f_0_%s_%s.png' % (j, i))
            count += 1
            # print('%d_%d' % (i, j))


def multCut(path, changePath, num, flag=True):
    """

    :param path: 要打开的图片的路径
    :param changePath: 裁剪图片存放路径
    :param num: 第几张图片
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

    cutImg(img, width, height, changeSize, changePath, num, flag)
    img.close()


def Binarization(src):
    """
    二值化图片
    :param src:
    :return: 返回黑色是否大于3000 如果大于返回false
    """
    img = cv2.imread(src)  # numpy数组类型
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)  # 注意是否需要修改
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
    :param movepath: 没有细胞移动图片的文件夹
    """
    ifexistpath(path, flag=False)
    ifexistpath(movepath)
    imglist = os.listdir(path)
    for img in imglist:
        if Binarization(path + img):
            print img
            movepic(path + img, movepath + img)


def movepic(path, movepath):
    os.rename(path, movepath)


def movepicfromdir(path, type):
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

    num = 0
    for j in range(listLen):

        print(listDir1[j])
        file = path + '/' + listDir1[j]
        isdir = os.path.isdir(file)
        if isdir:
            childPath = os.listdir(file)
            childLen = len(childPath)
            for k in range(childLen):
                result = file + '/' + childPath[k]
                childFileName = changPath + '1_' + str(num) + '.' + type  # 注意是否需要修改
                num = num + 1
                print(childFileName)
                os.rename(result, childFileName)
            # 都移动完后判断是否是空文件夹，是就删除
            if not os.listdir(file):
                print('删除%s空文件' % listDir1[j])
                os.rmdir(file)
                # os.rename(src, dst) src -- 要修改的目录名  dst -- 修改后的目录名


def imgList(path):
    filename = []
    imglist = os.listdir(path)
    for j in imglist:
        (myfilename, myextension) = os.path.splitext(j)  # 获取文件名和后缀名
        filename.append(myfilename)
    return filename


def movepicfromList(path, imglist, movepath):
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
            shutil.move(path + img, movepath)  # movepath 是一个文件夹


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


def copypicfromdir(path, movepath, i, type):
    imglist = os.listdir(path)
    ifexistpath(movepath)
    for index, img in enumerate(imglist):
        copyname = str(i) + '_' + str(index) + type
        shutil.copyfile(path + img, movepath + copyname)


def createTxt(path, imgpath, num):
    """
    创建train和val
    :param path: 要保存的txt路径
    :param imgpath: 图片所在路径
    :param num: 分配比例几比1
    :return:
    """
    train = open(path + 'train.txt', 'w')
    val = open(path + 'val.txt', 'w')
    imglist = os.listdir(imgpath)
    for index, item in enumerate(imglist):
        (myfilename, myextension) = os.path.splitext(item)  # 获取文件名和后缀名
        if index % num == 0:
            val.write(myfilename + '\n')
        else:
            train.write(myfilename + '\n')
    train.close()
    val.close()


def batchmove(path, movepath=''):
    """
    批量移动当前文件夹下的所有子文件夹中的内容到别的目录，
    该文件夹下的文件不受影响
    :return:
    """
    if movepath == '':
        movepath = path
    if not os.path.exists(path):
        print('不存在目录')
        exit()
    if not os.path.exists(movepath):
        print('不存在要改变的路径', movepath)
        os.mkdir(movepath)
        print('创建成功')
    listDir1 = os.listdir(path)  # 用list保存文件夹目录
    listLen = len(listDir1)  # 有多少个子文件夹
    for j in range(listLen):

        print(listDir1[j])
        file = path + '/' + listDir1[j]
        isdir = os.path.isdir(file)
        if isdir:
            childPath = os.listdir(file)
            childLen = len(childPath)
            for k in range(childLen):
                result = file + '/' + childPath[k]
                childFileName = movepath + "/" + childPath[k]
                os.rename(result, childFileName)
            # 都移动完后判断是否是空文件夹，是就删除
            if not os.listdir(file):
                print('删除%s空文件' % listDir1[j])
                os.rmdir(file)
                # os.rename(src, dst) src -- 要修改的目录名  dst -- 修改后的目录名


def info(path, label='label/', smalllabel=False):
    """
    传入根目录，计算label图中各种图片的个数，占比
    俩个默认参数
    默认不分析smalllabel文件夹中的图片
    :param path:
    :return:
    """
    log = open(path + 'log.txt', 'w')
    label = path + label
    imglist = os.listdir(label)
    log.write('label图的总张数为： ' + str(len(imglist)))
    labelblack = 0  # 没有癌症信息的图
    labellittle = 0  # 超过一半没有癌症信息
    labelmore = 0  # 大部分都是癌症信息图
    labelblue = 0  # 全都是癌症信息的图
    for i in imglist:
        img = Image.open(label + i)
        type = img.getcolors()
        img.close()
        if type[0][1] == 0 and type[0][0] >= 65500:  # 正常细胞
            labelblack += 1
        elif type[0][1] == 0 and type[0][0] > 32768:  # 大部分是正常
            labellittle += 1
        elif type[0][1] == 0:  # 大部分是癌细胞
            labelmore += 1
        else:  # 癌细胞
            labelblue += 1
    log.write('\n其中： ')
    log.write('\n全部都是正常细胞的数量是：' + str(labelblack))
    log.write('\n大部分是正常细胞的数量是：' + str(labellittle))
    log.write('\n癌症细胞的数量为：        ' + str(labelblue))
    log.write('\n大部分是癌症细胞的数量是：' + str(labelmore))
    log.write('\n正常和癌症比例为：       ' + str(float(labelblack + labellittle) / (labelblue + labelmore))[:5] + ':1')
    if smalllabel:
        smalllabel = path + smalllabel
        if smalllabel[-1] != '/':
            smalllabel += '/'
        smalllabellist = os.listdir(smalllabel)
        log.write('\n\n 制作数据集过程中剔除不用的数量为： ' + str(len(smalllabellist)))
        background = 0  # 背景图片
        backgroundmiddle = 0  # 具有一半的背景的图片
        cancer = 0  # 具有癌细胞的图片
        for i in smalllabellist:
            img = Image.open(smalllabel + i)
            type = img.getcolors()
            img.close()
            if type[0][1] == 0 and type[0][0] > 65500:
                background += 1
            elif type[0][1] == 0 and type[0][0] > 32768:
                backgroundmiddle += 1
            else:
                cancer += 1
        log.write('\n纯背景图片为: ' + str(background))
        log.write('\n具有一大半背景图的图片为：' + str(backgroundmiddle))
        log.write('\n大部分为癌细胞图片为： ' + str(cancer))


if __name__ == '__main__':
    # path为该数据集的相对根目录
    path = 'F:/Pathanalysis/three/train-test/'  # 第一处需要修改的地方

    # '2e956431-326d-42b2-bc83-4b5308bfd8f4','0c3d12d3-f8cc-4b96-9499-9c996d5fde77',没有参与训练
    nameone = ['0f83c078-f8c2-4ebc-afab-844209241f06',
               '15abcdb3-3bf7-48b3-9a1d-5be79aec66ec',
               '42bb1ded-7f48-4a83-a56b-a8e748ad2362', 'c8c0c1e2-3546-4f16-857d-8e53f6c08321',
               'c5703c0f-17fe-4d23-af20-f339d72ec354',
               'ffe2f7cf-fcd2-45db-9cd7-474af98992fc',
               '317639a9-4f1e-4092-bbd3-a0f42a042f2e',
               'df58afcf-e5a5-4163-ba6b-1042cf0ec949']
    # A389FB54-F718-4D8D-8D4B-277F471AA9C8,E8002ACF-E144-4E1A-AC3C-2D1529142D53作为测试集
    nametwo = ['6CEDFCAC-7DF3-4C92-B227-592A5FF7684D', '9f482134-21df-4d84-ad3c-ab92249668e0',
               '15F201B1-A03B-4667-A3D7-F0296A9EDF8A', '781E48D3-FB2D-4106-A3E7-E3E522219F44',
               '1860c378-c203-4aac-b2a6-72393ebd7303', '6498A9A0-070E-4482-A916-DD274D63998A',
               '087487E1-115F-4834-8407-21E2C47A17CA', '64963818-F750-49E0-9837-F145A7FE97AD']
    #  4ed75f33-c3d9-4797-9dd9-6cf0271733b0 作为测试集 其图片大小为512*512
    namethree = ['FF415E43-3948-4451-8373-B954C7DAC04A', '6cad9b89-84ab-4d36-a410-7592e830c1ae',
                 '7B6C7820-1539-42F3-9CDE-8D4B145E8D2F', '9CD9A77D-B2C5-4EE1-A4B5-B7402EDEC385',
                 '49DF94D2-29B2-4901-8160-E79642C31C64', '72e2b844-dedc-4836-85ce-7a242c64846b',
                 '159e9518-547a-4cb5-aec0-17b7c64ccc3f', 'dc45d440-bf9c-4d36-bd55-372e08679fa2']
    # fd99dbe5-d6b0-491d-a32d-917403242d5e , 68362C8D-3B1E-4ACA-9BE7-7E13E3E31B29 作为测试集
    namefour = ['02ae7e65-4a89-42d6-b364-82f88cff78cf', '02d3cdb9-58dd-4d80-b617-7ffeb84dd849',
                '4c033f58-9c26-485e-97b7-d8d63e5e2f94', '5DC73075-2DCF-4439-951C-BD5A1C5C1DB4',
                '8E82F703-28CC-4056-B4D7-16EE799B6284', '32D9DFCA-7480-4CCF-8819-0FBFE5211567',
                '66D62C58-1532-4C93-AE5C-AB2CCE6FF38D', '98C1BB35-ABF9-4F53-BC1A-39A01B9E4759']

    # 要制作的数据集的名称
    name = namethree  # 第二处需要修改的地方

   # *************************第一步：人工自行判断是否需要移动图片**********************************************************

   #  print '开始移动子文件夹中的图片到文件夹中'
   #  for item in name:
   #      # 默认文件夹名和要移动的文件夹名一致
   #      batchmove(path+'original/'+item+'/')
   #
   #  print '移动图片完毕'

   #   **************************第二步：把要训练的原始图片全都移动到JPEGImages中 等****************************************

    # 复制移动图片，并且重命名格式为 1_0....2_0...
    # 定义要移动的文件夹。和要移到的文件夹，和格式注意加点号

    # movepath = path + 'JPEGImages/'
    # ifexistpath(movepath)
    # print '要训练的原始图片全都移动到JPEGImages中'
    # for index, item in enumerate(name):
    #     sourcepath = path + 'original/' + item + '/'
    #     ifexistpath(sourcepath, flag=False)
    #
    #     copypicfromdir(sourcepath, movepath, index, '.jpg')
    # print ('移动jpg图片完毕')
    # # 图片二值化，判断图片是否含有细胞，把没有细胞的移走
    # print '开始判断图片是否包含细胞'
    # gettrainpath = path + 'JPEGImages/'
    # gettrainmovepath = path + 'nocel/'
    # gettrain(gettrainpath, gettrainmovepath)
    # print '图片判断完毕'

    # *****************************第三步：制作label图索引图*****************************************************************


    # 根据txt文件中的坐标信息来合成整张label图，并切割成小图,并且制作成索引图格式

    # print '开始制作索引图'

    # for index, i in enumerate(name):
    #     print '开始裁剪%s图片' % i
    #     txt_path = path + 'txt/' + i + '.txt'
    #     save_path = path + 'biglabel/'
    #     twoclasses(txt_path,save_path,i)   #合成lable图
    #     img_path = save_path + i + '.png'
    #     img_change_path = path + 'biglabel/' + i + '/'
    #     img_move_path = path + 'smalllabel/'
    #     multCut(img_path, img_change_path, index, flag=True)  #lable图片切割
    #     copypicfromdir(img_change_path, img_move_path, index, '.png')  # 把所有label图都移动到一个文件夹中
    #     print '裁剪%s图片完毕' % i
    # print '图片裁剪移动重命名完毕'
    #
    # 根据JPEGImages图片来移动label图
    imglist = imgList(path + 'JPEGImages/')
    labelimg = path + 'smalllabel/'
    movepath = path + 'label/'
    movepicfromList(labelimg, imglist, movepath)
    print 'label图片移动完毕，和JPEGIimages中一致'

    # 生成train，val的txt文件
    createTxt(path, path + 'JPEGImages/', 6)
    print 'txt文件创建完毕'
    #******************************第四步：分析图片信息保存到根目录的log日志中**********************************************

    print '开始对数据集进行分析'
    # 例 info(path,smalllabel='smalllabel/')
    info(path, smalllabel='smalllabel')
    print '分析完毕'
