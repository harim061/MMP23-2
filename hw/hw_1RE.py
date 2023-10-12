import cv2 as cv
import numpy as np
import math
import sys

img = np.zeros((600,800,3),np.uint8)
img[:]=(255,255,255)

BrushSize = 5
LColor,RColor= (255,0,0),(0,0,255)

def draw(event,x,y,flags,param):
    global ix,iy

    if event==cv.EVENT_LBUTTONDOWN or event==cv.EVENT_RBUTTONDOWN:
        ix,iy =x,y
    elif flags==cv.EVENT_FLAG_SHIFTKEY and event==cv.EVENT_LBUTTONUP:
        cv.line(img,(ix,iy),(x,y),(2550,0,0),5)
    elif flags==cv.EVENT_FLAG_ALTKEY and event==cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,33,240),5)
    elif flags==cv.EVENT_FLAG_ALTKEY and event==cv.EVENT_RBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (152, 33, 240), cv.FILLED)
    elif flags==cv.EVENT_FLAG_CTRLKEY and event==cv.EVENT_LBUTTONUP:
        r = int(math.sqrt((x-ix)**2 + (y-iy)**2))
        cv.circle(img,(ix,iy),r,(34,134,0),3)
    elif flags == cv.EVENT_FLAG_CTRLKEY and event == cv.EVENT_RBUTTONUP:
        r = int(math.sqrt((x - ix) ** 2 + (y - iy) ** 2))
        cv.circle(img, (ix, iy), r, (234, 34, 0), -1)
    elif flags==cv.EVENT_FLAG_RBUTTON and event==cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),BrushSize,RColor)
    elif flags==cv.EVENT_FLAG_LBUTTON and event==cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),BrushSize,LColor)

    cv.imshow("draw",img)

cv.namedWindow('draw')
cv.imshow('draw',img)

cv.setMouseCallback('draw',draw)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break