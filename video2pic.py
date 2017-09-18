# -*- coding: utf-8 -*-
"""
本程序用来将由PPT支座的视频文件，再此转换为图片。 
最近考一建，所以看了很多视频学习资料，这些视频资料都是使用的PPT讲解的，所以一直都喜欢通过截图的方式记录下来。 
后来想到了使用计算机视觉包OPENCV3来读取视频，通过对比前后帧的相似程度，直接保存不同的帧。 
对比图像相似是个很复杂的问题，网上有很多使用hash算法的教程，不过使用起来依然不是很满意，一些比较相似的图片往往对比成不相似，一些完全一样的帧计算结果也不相似。 
所以另辟蹊径，使用了比较成熟，先进，准确的ski-image来对比图片，结果当然是非常满意。 
2017.9.13
haifeng19@yeah.net
"""
import cv2
from skimage.measure import compare_ssim as ssim
vc = cv2.VideoCapture('6.mp4') #读入视频文件

def degree2(img1,img2):
    img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img12 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    imageA = cv2.resize(img11, (100, 100)) 
    imageB = cv2.resize(img12, (100, 100)) 

    s = ssim(imageA, imageB)
    if s<0:
            s=0
    return s 

c=1
if vc.isOpened(): 
    rval , frame = vc.read()
else:
    rval = False
    
while rval:
    rval, frame = vc.read()
    if c==1: 
        cv2.imwrite('image/'+str(c) + '.jpg',frame) 
        img2=frame
    elif rval==True:

        degree=degree2(frame,img2)
        img2=frame
        if degree<0.8:
            cv2.imwrite('image/'+str(c) + '.jpg',frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()

print 'over'






