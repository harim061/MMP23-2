import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')

# cv.calcHist([이미지],[몇번쨰?? color imgdml bgr 중 r],None,[가로 길이],[값의 범위])
h=cv.calcHist([img],[2],None,[256],[0,256]) # 2번 채널인 R 채널에서 히스토그램 구함
# color="색의 색" linewidth=선 굵기
plt.plot(h,color='r',linewidth=1)


hg= cv.calcHist([img],[1],None,[256],[0,256])
plt.plot(hg,color='g',linewidth=2,linestyle='dotted')

hb= cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hb,color='b',linewidth=3,linestyle='dashed')


plt.show()

# plt로 imshow하기
img2=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img2) # rgb라서 색이 다르게 보여짐
plt.show()