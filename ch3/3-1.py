import cv2 as cv
import sys

img=cv.imread('soccer.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('original_RGB',img)
# cv.imshow('Upper left half', img[세로절반, 가로절반, 색은 전부])
cv.imshow('Upper left half',img[0:img.shape[0]//2,0:img.shape[1]//2,:])

# cv.imshow('Upper left half', img[세로 1/4 ~ 3/4 , 가로 1/4 ~ 3/4, 색은 전부])
cv.imshow('Center half',img[img.shape[0]//4:3*img.shape[0]//4,img.shape[1]//4:3*img.shape[1]//4,:])

# cv.imshow('R channel', img[전부, 전부, 색은 red])
cv.imshow('R channel',img[:,:,2])
# cv.imshow('G channel', img[전부, 전부, 색은 green])
cv.imshow('G channel',img[:,:,1])
# cv.imshow('B channel', img[전부, 전부, 색은 blue])
cv.imshow('B channel',img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()