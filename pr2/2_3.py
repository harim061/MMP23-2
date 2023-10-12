import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit("no img")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray,dsize=(0,0),fx=0.7,fy=0.2)

cv.imshow('gray',gray)
cv.imshow('small gray',gray_small)

cv.waitKey()
cv.destroyAllWindows()