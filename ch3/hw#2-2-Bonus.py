# 필요한 라이브러리를 임포트한다.
import cv2 as cv
import cvlib as cvl

cap = cv.VideoCapture('face2.mp4')
ksize = 31

# 동영상의 각 프레임을 읽어온다.
while True:
    ret, frame = cap.read()

    # 프레임 읽기에 실패하면 루프를 종료한다.
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    # 프레임에서 얼굴을 감지한다.
    faces, confidences = cvl.detect_face(frame)

    # 감지된 각 얼굴에 대하여 블러 효과를 적용한다.
    for (x, y, x2, y2), conf in zip(faces, confidences):
        cv.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
        roi = frame[y:y2, x:x2]
        roi = cv.GaussianBlur(roi, (ksize, ksize), 0.0)
        frame[y:y2, x:x2] = roi

    # 결과를 표시한다.
    cv.imshow('face detection', frame)

    # 'q' 키를 누르면 종료한다.
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
