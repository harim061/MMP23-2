import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')

h=cv.calcHist([img],[1],None,[256],[0,256])

plt.plot(h,color='r',linewidth=1)
plt.show()