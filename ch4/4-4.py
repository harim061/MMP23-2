import cv2 as cv 

img=cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# method 검출방법 HOUGH_GRADIENT
# dp 이미해상도 accumulator해상도 1이면 같음
# dist 검출된 원 중심 사이의 최소 거리
# param1 : canny의 높은 threshold
# param2 : 누적 threshold(몇개이상 지나는 값)
# minR, maxR : 검출된 원 반지름 범위

apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,200,param1=150,param2=20,minRadius=50,maxRadius=120)

for i in apples[0]:
    # img,x,y,r
    # print(i) -> x,y,r
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)

cv.imshow('Apple detection',img)  

cv.waitKey()
cv.destroyAllWindows()