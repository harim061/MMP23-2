import skimage
import numpy as np
import cv2 as cv

orig=skimage.data.horse() #배경 1, 물체 0 black
img=255-np.uint8(orig)*255 # 0/1 -> 0/255 -> 255
cv.imshow('Horse',img)

contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

img2=cv.cvtColor(img,cv.COLOR_GRAY2BGR)		# 컬러 디스플레이용 영상
cv.drawContours(img2,contours,-1,(255,0,255),2)
cv.imshow('Horse with contour',img2)

# 각각의 경계선 중 하나 이용
contour=contours[0]
print(contour.shape)

# moments 계산
m=cv.moments(contour)				# 몇 가지 특징 
area=cv.contourArea(contour)
cx,cy=m['m10']/m['m00'],m['m01']/m['m00']

# arcLength 둘레의 길이 구함
perimeter=cv.arcLength(contour,True)
roundness=(4.0*np.pi*area)/(perimeter*perimeter)
print('면적=',area,'\n중점=(',cx,',',cy,')','\n둘레=',perimeter,'\n둥근 정도=',roundness)

img3=cv.cvtColor(img,cv.COLOR_GRAY2BGR)		# 컬러 디스플레이용 영상

# 대략적인 모향 (다각형) 8 숫자로 도형을 정의 경계선에서 얼마만큼 떨어뜨리게 함??
# 8 이 작을 수록 가까워짐
contour_approx=cv.approxPolyDP(contour,8,True)	# 직선 근사
cv.drawContours(img3,[contour_approx],-1,(0,255,0),2)
print(contour_approx.shape)
contour_approx=cv.approxPolyDP(contour,20,True)	# 직선 근사
cv.drawContours(img3,[contour_approx],-1,(0,255,255),2)

# (20,1,2) 2054개 중 20개의 화소값을 이용하겟엄
print(contour_approx.shape)

# 볼록 다각형? 움푹 말구!
hull=cv.convexHull(contour)			# 볼록 헐
# reshape 배열의 형태를 바꿈 -> 왜? 영상 보기~
hull=hull.reshape(1,hull.shape[0],hull.shape[2])
cv.drawContours(img3,hull,-1,(0,0,255),2)
print(hull.shape)

cv.imshow('Horse with line segments and convex hull',img3)

cv.waitKey()
cv.destroyAllWindows()