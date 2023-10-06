import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('morph.jpg',cv.IMREAD_UNCHANGED)

# t,bin_img=cv.threshold(img[:,:,3],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
t, b = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.imshow(b,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# b=bin_img[bin_img.shape[0]//2:bin_img.shape[0],0:bin_img.shape[0]//2+1]
plt.imshow(b,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 컨볼루션 계산 안됩니당~ 필터의 값이 아님 = 구조 요소에 포함 or 미포함 나타내는 것
se=np.uint8([[0,0,1,0,0],			# 구조 요소
            [0,1,1,1,0],
            [1,1,1,1,1],
            [0,1,1,1,0],
            [0,0,1,0,0]])

# cv.dilate(src,구조요소,반복)
b_dilation=cv.dilate(b,se,iterations=1)	# 팽창
plt.imshow(b_dilation,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_erosion=cv.erode(b,se,iterations=1)	# 침식
plt.imshow(b_erosion,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_closing=cv.erode(cv.dilate(b,se,iterations=1),se,iterations=1)	# 닫기 : 팽창 -> 침식
plt.imshow(b_closing,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_opening =cv.dilate(cv.erode(b,se,iterations=1),se,iterations=1) # 열기
plt.imshow(b_opening,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

morph = np.hstack((b,b_dilation,b_erosion,b_closing,b_opening))
cv.imshow('sharpening',morph)

cv.waitKey()
cv.destroyAllWindows()