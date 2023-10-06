import cv2 as cv

img=cv.imread('check.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 1차미분 소벨 연산자 적용 : 중심 * 2
# x = 1,0 (x방향의 차이)
# y = 0,1 (y방향이 차이)
grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3)
grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

# 절대값을 취해 양수 영상으로 변환
sobel_x=cv.convertScaleAbs(grad_x)
sobel_y=cv.convertScaleAbs(grad_y)

# 합치기
# 0.5 * sobel_x + 0.5 * sobel_y
edge_strength=cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0)	# 에지 강도 계산


# 2차미분
grad=cv.Laplacian(gray,cv.CV_32F)

lap = cv.convertScaleAbs(grad)

cv.imshow('laplacian',lap)


cv.imshow('Original',gray)
cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('edge strength',edge_strength)

cv.waitKey()
cv.destroyAllWindows()