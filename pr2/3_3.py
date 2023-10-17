import cv2 as cv
import sys

img =cv.imread('soccer.jpg')

t,imgO = cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

print(t)

cv.imshow('r',img[:,:,2])
cv.imshow('otsu',imgO)

cv.waitKey()
cv.destroyAllWindows()
