# 필요한 라이브러리를 임포트한다.
import cv2 as cv

# 'face2.mp4' 동영상을 불러온다.
cap = cv.VideoCapture('face2.mp4')

color_mode=''
# 동영상의 각 프레임을 읽어온다.
while True:
    ret, frame = cap.read()

    # 프레임 읽기에 실패하면 루프를 종료한다.
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    key = cv.waitKey(1)
    # 사용자에게 키를 받는다
    if key == ord('y'):
        color_mode = 'COLOR_BGR2YCrCb'
    elif key == ord('h'):
        color_mode = 'COLOR_BGR2HSV'
    elif key == ord('q'):
        break


    if color_mode=="COLOR_BGR2HSV":
        img_color = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # 3 픽셀 별로 피부색인지 확인
        mask = cv.inRange(img_color, (0, 70, 50), (50, 150, 255))
        # 4 피부색 출력
        skin_detection = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('face img', skin_detection)

    elif color_mode=='COLOR_BGR2YCrCb':
        # 2 선택된 컬러모델로 변환
        img_color = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
        # 3 픽셀 별로 피부색인지 확인
        mask = cv.inRange(img_color, (0, 133, 77), (255, 173, 127))
        # 4 피부색 출력
        skin_detection = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('face img', skin_detection)
    else:
        cv.imshow('face img',frame)

cap.release()
cv.destroyAllWindows()
