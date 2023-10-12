import cv2 as cv

img=cv.imread('soccer.jpg')

if img is None:
    print("no")

cv.rectangle(img,(30,20),(300,50),(255,255,0),cv.FILLED)
cv.putText(img,'soccer',(500,300),cv.FONT_HERSHEY_TRIPLEX,4,(255,0,130),5)
cv.imshow('img',img)

cv.waitKey()
cv.destroyAllWindows()