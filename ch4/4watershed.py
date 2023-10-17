import cv2 as cv
import numpy as np

# Image loading
img = cv.imread("water_coins.jpg")

# image grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshold Processing
ret, bin_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
# cv.imshow('binarized image',bin_img)
# white(object) noise removal
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

# 침식을 하고 팽창 : 화이트 노이즈가 없어짐
b_opening = cv.dilate(cv.erode(bin_img,kernel,iterations=2),kernel,iterations=2)	# 열기
# cv.imshow('b_opening image',b_opening)
# sure background area

# 팽창을 시켜줘요 여기서 검정은 ㄹㅇ 배경이다!
sure_bg = cv.dilate(b_opening,kernel,iterations=3)
cv.imshow('sure_bg image',sure_bg)

# sure foreground area
# distanceTransform : Binary 이미지에서  픽셀값이 0인 배경으로부터의 거리를 픽셀값이 255인 영역에 표현하는 방법
dist_transform = cv.distanceTransform(b_opening,cv.DIST_L2,5)
# 2 : 거리 공식
# 3 : 마스크 크기
dist=dist_transform * 10
dist=np.uint8(dist)
cv.imshow('dist_transform',dist)

dist = dist_transform * 10
dist = np.uint8(dist)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# 제일 밝은 값의 0.7%는 무조건 물체다!
cv.imshow('sure_fg',sure_fg)

# unknown region
sure_fg = np.uint8(sure_fg)
# 확실 배경 - 확실 물체 하면 히잉 잘 몰라~
unknown = cv.subtract(sure_bg,sure_fg)
cv.imshow('unknow',unknown)


# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero

# unknown은 0 확실한 sure_fg는 번호!
markers[unknown==255] = 0

markers = cv.watershed(img,markers)
# 2개의 영역이 만나는 지점
img[markers == -1] = [255,0,0]
img[markers == 1] =[200,0,200]
img[markers==2] = [127,0,127]
cv.imshow("watershed results", img)

cv.waitKey()
cv.destroyAllWindows()