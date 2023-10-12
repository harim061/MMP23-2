import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event,x,y,flags,params):
    global ix,iy
    if event==cv.EVENT_LBUTTONDOWN:
        ix,iy= x,y
    elif event == cv.EVENT_LBUTTONUP:  # 마우스 오른쪽 버튼 클릭했을 때
        cv.rectangle(img, (ix, iy), (x,y), (255, 0, 0), 2)
    cv.imshow('rect',img)

cv.namedWindow('rect')
cv.imshow('rect',img)

cv.setMouseCallback('rect',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break