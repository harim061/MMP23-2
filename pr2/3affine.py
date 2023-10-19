import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')

rows,cols = img.shape[:2]

src_point = np.float32([[0,0],[cols-1,0],[0,rows-1]])
dst_point = np.float32([[cols-1,0],[0,0],[cols-1,rows-1]])

affine_matrix = cv.getAffineTransform(src_point,dst_point)
img_symmetry = cv.warpAffine(img,affine_matrix,(cols,rows))

cv.imshow('origin',img)
cv.imshow('img_symmetry',img_symmetry)

cv.waitKey()
cv.destroyAllWindows()