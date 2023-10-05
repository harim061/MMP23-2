import cv2 as cv
import cvlib as cvl      # cvlib, tensorflow 설치
# cvlib는 파이썬에서 얼굴, 객체 인식을 위한 사용하기 쉬운 라이브러리
# opencv와 tensorflow를 사용하고 있기 때문에, cvlib와 함께 설치해야 함

ksize = 31              # 블러 처리에 사용할 커널 크기

img = cv.imread('face2.jpg')

# 얼굴을 찾음
faces, confidences = cvl.detect_face(img)

# face에는 얼굴에 대한 정보
for (x,y, x2,y2), conf in zip(faces, confidences):
    cv.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
    roi = img[y:y2, x:x2] # 얼굴 영역 지정
    roi = cv.GaussianBlur(roi,(31,31),0.0)
    img[y:y2, x:x2 ] = roi

cv.imshow('face detection', img)

cv.waitKey()
cv.destroyAllWindows()