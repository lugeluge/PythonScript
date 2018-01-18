import  os
jpgpath='F:/Pathanalysis/three/train-test/JPEGImages/'
pngpath='F:/Pathanalysis/three/train-test/label/'
jpgset=[]
pngset=[]
jpg=os.listdir(jpgpath)
png=os.listdir(pngpath)
for i in jpg:
    (myfilename, myextension) = os.path.splitext(i)
    jpgset.append(myfilename)
for i in png:
    (myfilename, myextension) = os.path.splitext(i)
    pngset.append(myfilename)
print set(jpgset)-set(pngset)