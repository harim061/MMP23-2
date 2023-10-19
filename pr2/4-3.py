import cv2 as cv

img =cv.imread('../ch4/soccer.jpg')
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)

t,bin_gray =cv.threshold(gray,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
contour,hierarchy = cv.findContours(bin_gray,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

lcontour =[]

for i in range(len(contour)):
    if contour[i].shape[0] > 100:
        lcontour.append(contour[i])


cv.drawContours(img,lcontour,-1,(255,0,0),3)

cv.imshow('original',img)
cv.imshow('contour',bin_gray)

cv.waitKey()
cv.destroyAllWindows()