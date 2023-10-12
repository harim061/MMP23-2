import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def draw(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(x,y),(x+30,y+500),(255,0,0),3)
    elif event == cv.EVENT_RBUTTONDOWN:  # 마우스 오른쪽 버튼 클릭했을 때
        cv.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), 2)
    cv.imshow('rect',img)

cv.namedWindow('rect')
cv.imshow('rect',img)

cv.setMouseCallback('rect',draw)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break