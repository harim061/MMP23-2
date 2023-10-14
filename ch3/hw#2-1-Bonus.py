# 필요한 라이브러리를 임포트한다.
import cv2 as cv

# 'face2.mp4' 동영상을 불러온다.
cap = cv.VideoCapture('face2.mp4')

# 동영상의 각 프레임을 읽어온다.
while True:
    ret, frame = cap.read()

    # 프레임 읽기에 실패하면 루프를 종료한다.
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    # 프레임의 색상 공간을 HSV로 변환한다.
    img_color = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 피부 색상에 해당하는 HSV 범위를 설정하여 마스크를 생성한다.
    mask = cv.inRange(img_color, (0, 70, 50), (50, 150, 255))

    # 마스크를 사용하여 원본 프레임에서 피부 영역만을 추출한다.
    skin_detection = cv.bitwise_and(frame, frame, mask=mask)

    # 결과를 표시한다.
    cv.imshow('Skin Detection', skin_detection)

    # 'q' 키를 누르면 종료한다.
    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
