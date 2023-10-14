# 필요한 라이브러리를 임포트한다.
import cv2 as cv
import cvlib as cvl

ksize = 31

# 'face2.jpg' 이미지를 불러온다.
img = cv.imread('face2.jpg')

# 1 얼굴 검출
# 이미지에서 얼굴을 감지한다.
faces, confidences = cvl.detect_face(img)

# 2 검출된 얼굴 부분만 추출
# 감지된 각 얼굴에 대하여 블러 효과를 적용한다.
for (x, y, x2, y2), conf in zip(faces, confidences):
    cv.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
    roi = img[y:y2, x:x2]  # 얼굴 영역을 지정한다.
    # 3 추출된 얼굴 부분만 모자익 처리
    roi = cv.GaussianBlur(roi, (ksize, ksize), 0.0)  # 가우시안 블러를 적용한다.
    # 4 모자익 처리된 얼굴을 원래 영상에 적용
    img[y:y2, x:x2] = roi  # 원본 이미지에 블러 처리된 얼굴 영역을 대체한다.

# 결과를 표시한다.
cv.imshow('face detection', img)
cv.waitKey()
cv.destroyAllWindows()
