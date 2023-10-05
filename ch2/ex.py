import numpy as np

# ex2(2)

# a=np.array([1, 2, 3, 4, 5,6,7,8,9,10])
#
# print(a.min())
# print(a.max())
# print(a.argmin())
# print(a.argmax())
# print(a.mean())
# print(a.sum())
# print(a.cumsum())
# print(a.prod())
# print(a.cumprod())


#ex3

# import cv2 as cv
#
# img1=cv.imread('soccer.jpg')
# img2=cv.imread('soccer_gray.jpg')
#
# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
#
#
# cv.waitKey()
# cv.destroyAllWindows()



#ex4

# import cv2 as cv
#
# img = cv.imread('soccer.jpg')
#
# small=cv.resize(img,dsize=(0,0),fx=0.1,fy=0.1)
# small2=cv.resize(img,dsize=(0,0),fx=0.2,fy=0.2)
#
# cv.imshow('size 0.1', small)
# cv.imshow('size 0.2', small2)
#
# cv.waitKey()
# cv.destroyAllWindows()


#ex5

# import cv2 as cv
#
# cap = cv.VideoCapture('../ch10/slow_traffic_small.mp4')
# color_mode = 'color'
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         print("영상 끝")
#         break
#
#     key = cv.waitKey(1)
#
#     if key == ord('g'):
#         color_mode = 'gray'
#     elif key == ord('c'):
#         color_mode = 'color'
#     elif key == ord('q'):
#         break
#
#     if color_mode == 'gray':
#         frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#         cv.imshow('display_frame', frame_gray)
#     else:
#         cv.imshow('display_frame', frame)
#
#
# cv.destroyAllWindows()

#ex6

# import cv2 as cv
#
# img=cv.imread('girl_laughing.jpg')
# cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)
# cv.putText(img,'laugh',(630,24),cv.FONT_HERSHEY_TRIPLEX,1,(255,0,0),2)
# cv.arrowedLine(img,(630,24),(830,30),(255,0,0),2)
#
# cv.imshow("draw",img)
#
# cv.waitKey()
# cv.destroyAllWindows()

#ex7

# import cv2 as cv
#
# img = cv.imread('girl_laughing.jpg')
#
# def draw(event,x,y,flags,param):
#     if event==cv.EVENT_LBUTTONDOWN:
#         cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2)
#     elif event==cv.EVENT_RBUTTONDOWN:
#         cv.circle(img,(x,y),50,(0,255,0),3)
#
#     cv.imshow('drawing',img)
#
# cv.namedWindow('drawing')
# cv.imshow('drawing',img)
#
# cv.setMouseCallback('drawing',draw)
#
# while(True):
#     if cv.waitKey(1)==ord('q'):
#         cv.destroyAllWindows()
#         break


#ex8

# import cv2 as cv
# import math
# img= cv.imread('girl_laughing.jpg')
#
# def draw(event,x,y,flags,param):
#     global ix,iy
#
#     if event==cv.EVENT_LBUTTONDOWN:
#         cv.rectangle(img,(x,y),(x+200,y+300),(255,0,0),2)
#     elif event ==cv.EVENT_RBUTTONDOWN:
#         ix,iy = x,y
#
#     elif event==cv.EVENT_RBUTTONUP:
#         cv.circle(img,(ix,iy),int(math.sqrt((x - ix) ** 2 + (y - iy) ** 2)), (0,255,0),2)
#
#     cv.imshow('draw',img)
#
# cv.namedWindow('draw')
# cv.imshow('draw',img)
#
# cv.setMouseCallback('draw',draw)
#
# while True:
#     if cv.waitKey(1)==ord('q'):
#         cv.destroyAllWindows()
#         break


#ex9
import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

BrushSiz=5					# 붓의 크기
LColor,RColor=(255,0,0),(0,0,255)		# 파란색과 빨간색

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)# 마우스 왼쪽 버튼 클릭하면 파란색
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)# 마우스 오른쪽 버튼 클릭하면 빨간색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하고 이동하면 파란색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)# 오른쪽 버튼 클릭하고 이동하면 빨간색

    cv.imshow('Painting',img)		# 수정된 영상을 다시 그림

cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',painting)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break
    elif cv.waitKey(1)==ord('a'):
        BrushSiz = BrushSiz +1
    elif cv.waitKey(1)==ord('b'):
        if BrushSiz > 1:
            BrushSiz = BrushSiz -1