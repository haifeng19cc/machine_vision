# -*- coding: utf-8 -*-

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



