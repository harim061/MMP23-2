import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("fail")

frames = []
while True:
    ret,frame = cap.read()

    if not ret:
        print("fin")
        break

    # gray 영상으로 바꿔보기
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # 영상 절반으로 만들기
    gray_samll = cv.resize(gray_frame,dsize=(0,0),fx=0.5,fy=0.5)
    cv.imshow('video',gray_frame)

    key=cv.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('c'):
        frames.append(frame)


if(len(frames)>0):
    imgs=frames[0]
    for i in range(1,min(3,len(frames))):
        imgs=np.hstack((imgs,frames[i]))

    cv.imshow("hstack",imgs)
    cv.waitKey()
    cv.destroyAllWindows

cap.release()
cv.destroyAllWindows