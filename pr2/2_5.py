import cv2 as cv
import numpy as np
import sys

cap=cv.VideoCapture('../ch10/slow_traffic_small.mp4')
cap2 =cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("nope")

frames=[]

while True:
    ret,frame= cap.read()

    if not ret:
        print('fin')
        break

    cv.imshow('video',frame)

    key= cv.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('c'):
        frames.append(frame)

cv.destroyAllWindows()

if(len(frames)>0):
    imgs=frames[0]

    for i in range(1,min(5,len(frames))):
        imgs=np.hstack((imgs,frames[i]))

    cv.imshow('hstack',imgs)

    cv.waitKey()
    cv.destroyAllWindows()