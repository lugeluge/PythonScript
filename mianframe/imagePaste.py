#coding:utf-8
import PIL.Image as Image
import os, sys
mw = 256 # 图片大小
toImage = Image.new('L', (25171, 11802))#构造图片的宽和高，如果图片不能填充完全会
#出现黑色区域
def paste(path):

    for y in range(10):#0-46
        for x in range(12):#0-98
            fname = "%d_%d.png" %(y,x)
            fromImage = Image.open(path+fname)
            toImage.paste(fromImage, (x * fromImage.size[0], y * fromImage.size[1]))
    toImage.save('F:/Pathanalysis/haili/middlemodel.png')
def splitimage(src, rownum, colnum, dstpath):
    """
    在图片拼接之前先把合成的图片给切割成六张中图，测试
    中图在模型中工不工作，如果不工作就没有写的必要了
    :param src: 图片路径
    :param rownum: 要切割的行
    :param colnum: 要切割的列
    :param dstpath: 保存的位置
    :return:
    """
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, str(r)+'_' + str(c) + '.' + ext))
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')
if __name__ == '__main__':
    path='F:/Pathanalysis/haili/2e1/'
    paste(path)
    # path = 'F:/Pathanalysis/change/newtwo/testlabel/0c3d/0c3d.jpg'
    # # src = input('请输入图片文件路径：')
    # src = path
    # if os.path.isfile(src):
    #     # dstpath = input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
    #     dstpath = 'F:/Pathanalysis/change/newtwo/testlabel/0c3d/middle/'
    #     if (dstpath == '') or os.path.exists(dstpath):
    #         row = int(input('请输入切割行数：'))
    #         col = int(input('请输入切割列数：'))
    #         if row > 0 and col > 0:
    #             splitimage(src, row, col, dstpath)
    #         else:
    #             print('无效的行列切割参数！')
    #     else:
    #         print('图片输出目录 %s 不存在！' % dstpath)
    # else:
    #     print('图片文件 %s 不存在！' % src)
