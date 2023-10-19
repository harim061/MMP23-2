import cv2 as cv

img = cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

apples = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,200,param1=50,param2=5,minRadius=50,maxRadius=120)
for i in apples[0]:
    # img,x,y,r
    # print(i) -> x,y,r
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)

cv.imshow('Apple detection',img)

cv.waitKey()
cv.destroyAllWindows()