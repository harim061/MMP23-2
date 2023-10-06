import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')
img=cv.resize(img,dsize=(0,0),fx=0.4,fy=0.4)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.putText(gray,'soccer',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
# cv.imshow('Original',gray)

# GaussianBlur(이미지,(필터크기,필터크기),시그마값 = 종의 높이)
smooth=np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),cv.GaussianBlur(gray,(15,15),0.0)))
# cv.imshow('Smooth',smooth)

# 3x3 직접 필터를 입혀주기
femboss=np.array([[-1.0, 0.0, 0.0],
                  [ 0.0, 0.0, 0.0],
                  [ 0.0, 0.0, 1.0]])

gray16=np.int16(gray) #  gray = 1byte = 8bits -> 값을 잃어버리게 되어서 16bit로 늘려둠

# clip 연산 filter2D로 입히기
emboss=np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255))
emboss_bad=np.uint8(cv.filter2D(gray16,-1,femboss)+128)

# cv.filter(영상,-1,필터이름)
emboss_worse=cv.filter2D(gray,-1,femboss)

# cv.imshow('Emboss',emboss)
# cv.imshow('Emboss_bad',emboss_bad)
# cv.imshow('Emboss_worse',emboss_worse)

faverage = np.array([[1.0/9.0, 1.0/9.0,1.0/9.0],
                     [1.0/9.0,1.0/9.0,1.0/9.0],
                     [1.0/9.0,1.0/9.0,1.0/9.0]])

fsharpening1 = np.array([[0.0, -1.0, 0.0],
                     [ -1.0 , 4.0, -1.0],
                     [0.0 , -1.0, 0.0]])

fsharpening2 = np.array([[0.0, -1.0, 0.0],
                     [ -1.0 , 5.0, -1.0],
                     [0.0 , -1.0, 0.0]])

result =cv.filter2D(gray,-1,fsharpening1)
# cv.imshow('faverage',result)

gray=cv.imread('coins.png',cv.IMREAD_GRAYSCALE)

# openCV에서 제공하는 함수들
# blur하는 필터의 크기가 클수록 블러가 더 심함
average=cv.blur(gray,(9,9))
cv.imshow('result -average',average)

median = cv.medianBlur(gray,3)
cv.imshow('result -median',median)

# 가우시안 필터처럼 가운데에 가중치를 더 줌 (각 픽셀과 주변요소들로부터 가중 평균을 구함)
# 스무딩 : 값이 비슷하면 포함 / 값이 비슷 ㄴㄴ(에지) 포함 ㄴㄴ
# 즉 픽셀값의 차이도 같이 사용하며 유사한 픽셀에 더 큰 가중치를 줌
# 중요한 에지를 가우시안에 의해서 스무딩하지 않겠다 = 경계선을 유지하며 스무딩
bilateral = cv.bilateralFilter(gray, -1, sigmaColor=5,sigmaSpace=5)
cv.imshow('result - bilateral', bilateral)

cv.waitKey()
cv.destroyAllWindows()