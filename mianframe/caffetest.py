# coding:utf-8
import numpy as np
import cv2
from PIL import Image
import matplotlib.pylab as plt
import caffe
import chardet
import io



def acc():
    # load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe

    modelpath = 'E:/caffe/caffe cudnn/caffe/fcn.berkeleyvision.org-master/voc-fcn8s/'
    caffe.set_device(0)
    caffe.set_mode_gpu()
    net = caffe.Net(modelpath + 'deploy.prototxt', modelpath + 'snapshot/train_iter_100000.caffemodel', caffe.TEST)

    dataset = np.loadtxt(
        r'F:\Pathanalysis\change\newtwo\testlabel\2e95\cvmiddle.txt',
        dtype=str)

    for d in dataset:
        print "已生成",d
        im = Image.open(
            'F:\\Pathanalysis\\change\\newtwo\\testlabel\\2e95\\cvmiddlejpg\\' + d + '.jpg')

        in_ = np.array(im, dtype=np.float32)
        in_ = in_[:, :, ::-1]
        in_ -= np.array((198.361, 149.756, 183.762))
        in_ = in_.transpose((2, 0, 1))
        # shape for input (data blob is N x C x H x W), set data
        net.blobs['data'].reshape(1, *in_.shape)
        net.blobs['data'].data[...] = in_
        # run net and take argmax for prediction
        net.forward()
        out = net.blobs['score'].data[0].argmax(axis=0)  #out是fcn8s生成的图片信息
        out=out.astype(np.int8)
        testimg=Image.fromarray(out,mode='L')
        #testimg.putpalette([0, 0, 0, 0, 0, 255, 0, 255, 0])  # 每三个值表示一个rgb值
        testimg.save('F:/Pathanalysis/change/newtwo/testlabel/2e95/cvmodellabel/'+d+'.png')
        im.close()
        testimg.close()
def paste(path,savepath,w,h):
    toImage = Image.new('L', (w, h))  # 构造图片的宽和高，如果图片不能填充完全会
    # 出现黑色区域
    for y in range(10):#0-46
        for x in range(12):#0-98
            fname = "%d_%d.png" %(y,x)
            fromImage = Image.open(path+fname)
            toImage.paste(fromImage, (x * fromImage.size[0], y * fromImage.size[1]))
    toImage.putpalette([0, 0, 0, 0, 0, 255])  # 每三个值表示一个rgb值
    toImage.show("模型生成的图")
    toImage.save(savepath+'middlelabel.png')
    toImage.close()
def findcontours(labelp,imgp,imgsave):
    label = cv2.imread(labelp)
    img = cv2.imread(imgp)
    gray = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    image, cnts, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print cnts,'cets'
    # print hierarchy
    cv2.drawContours(img, cnts, -1, (0, 0, 255), 13)
    cv2.imwrite(imgsave, img)
if __name__ == '__main__':
    acc()
    print "所有图片生成完毕，开始图片合成"
    # pastpath='F:/Pathanalysis/change/newtwo/testlabel/2e95/middlemodel/'
    # savepath='F:/Pathanalysis/change/newtwo/testlabel/2e95/'
    # paste(pastpath,savepath,25171,11802)
    # print "图片合成完毕,制作索引图制作完毕"
    # print "开始提取坐标区域信息,并绘制到原图上"
    #
    #
    # # findcontours(savepath + '2e95label.png', savepath + '2e95.jpg', savepath + 'labelline.jpg')
    # findcontours(savepath + 'middlelabel.png', savepath + 'labelline.jpg', savepath + 'hy.jpg')
    # print "绘制完毕"
    # img = Image.open(savepath+'hy.jpg')
    # img.show("信息图")
    # with open(savepath+'acc.txt','r') as f:
    #     txt=f.read()
    # type=chardet.detect(txt)
    # txt=txt.decode(type['encoding']).splitlines()
    # for i in txt:
    #     print i
    print '程序运行结束'
