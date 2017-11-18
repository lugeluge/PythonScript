# encoding:utf-8
'''
根据测试图片生成的单张图片的recall值进行分类
'''
import shutil
import os

os.chdir('C:/users/luchi/desktop/test/')
txtPath = 'C:/users/luchi/desktop/test/3176cancer.log'  # 日志文件
f = open(txtPath)
log1 = open('-1recall/-1recall.log', 'w')
log2 = open('0.2recall/0.2recall.log', 'w')
log3 = open('0.5recall/0.5recall.log', 'w')
log4 = open('1recall/1recall.log', 'w')
lines = f.readlines()
name = []  # 名字
accuracy = []  # 准确率
precision = []  # 精确率
f = []  #
recall = []

for i, line in zip(range(len(lines)), lines):
    if '\xef\xbb\xbf' in line:
        line = line.replace('\xef\xbb\xbf', '')  # 剔除第一行的\xef\xbb\xbf字节。
    line = line.split('\n')

    temp = i % 5
    if temp == 0:
        name.append(line[0])
    if temp == 1:
        accuracy.append(line[0])
    if temp == 2:
        precision.append(line[0])
    if temp == 3:
        a, b = line[0].split(" ")
        recall.append(b)
    if temp == 4:
        f.append(line[0])

for i in range(len(name)):
    oldLabelName = '3176label/' + name[i] + '.png'
    oldImageName = '3176images/' + name[i] + '.jpg'
    if float(recall[i]) < 0:
        newLabelName = '-1recall/label/' + name[i] + '.png'
        newImageName = '-1recall/images/' + name[i] + '.jpg'
        shutil.copyfile(oldImageName, newImageName)
        shutil.copyfile(oldLabelName, newLabelName)
        log1.write(name[i] + '\n')
        log1.write(accuracy[i] + '\n')
        log1.write(precision[i] + '\n')
        log1.write('癌症召回率为: ' + recall[i] + '\n')
        log1.write(f[i]+'\n')
    if 0 <= float(recall[i]) < 0.2:
        newname = '0.2recall/label/' + name[i] + '.png'
        newImageName = '0.2recall/images/' + name[i] + '.jpg'
        shutil.copyfile(oldImageName, newImageName)
        shutil.copyfile(oldLabelName, newname)
        log2.write(name[i] + '\n')
        log2.write(accuracy[i] + '\n')
        log2.write(precision[i] + '\n')
        log2.write('癌症召回率为: ' + recall[i] + '\n')
        log2.write(f[i]+'\n')
    if 0.2 <= float(recall[i]) < 0.5:
        newname = '0.5recall/label/' + name[i] + '.png'
        newImageName = '0.5recall/images/' + name[i] + '.jpg'
        shutil.copyfile(oldImageName, newImageName)
        shutil.copyfile(oldLabelName, newname)
        log3.write(name[i] + '\n')
        log3.write(accuracy[i] + '\n')
        log3.write(precision[i] + '\n')
        log3.write('癌症召回率为: ' + recall[i] + '\n')
        log3.write(f[i]+'\n')
    if 0.5 <= float(recall[i]) < 1:
        newname = '1recall/label/' + name[i] + '.png'
        newImageName = '1recall/images/' + name[i] + '.jpg'
        shutil.copyfile(oldImageName, newImageName)
        shutil.copyfile(oldLabelName, newname)
        log4.write(name[i] + '\n')
        log4.write(accuracy[i] + '\n')
        log4.write(precision[i] + '\n')
        log4.write('癌症召回率为: ' + recall[i] + '\n')
        log4.write(f[i]+'\n')
    print name[i], recall[i]
print 'done'
