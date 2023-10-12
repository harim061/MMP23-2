import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit("이미지가 없음")

cv.imshow('soccer',img)

cv.waitKey()
cv.destroyAllWindows()
