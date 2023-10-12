import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')
BrushSize= 5
LColor=(255,0,0)

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event,x,y,flags,params):
    global ix,iy
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSize,LColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON :  # 마우스 오른쪽 버튼 클릭했을 때
        cv.circle(img, (x, y), BrushSize, LColor, -1)
    cv.imshow('rect',img)

cv.namedWindow('rect')
cv.imshow('rect',img)

cv.setMouseCallback('rect',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break