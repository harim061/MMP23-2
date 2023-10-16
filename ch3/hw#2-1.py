# 필요한 라이브러리를 임포트한다.
import cv2 as cv

# 'face2.jpg' 이미지를 불러온다.
img = cv.imread('face2.jpg')



# 이미지가 제대로 로드되었는지 확인한다.
if img is None:
    print("no img")

# 무한루프로 사용자의 키 입력을 기다린다.
while True:
    # 원본 이미지를 화면에 표시한다.
    cv.imshow("face img", img)
    key = cv.waitKey()


    # 사용자가 'q' 키를 누르면 프로그램을 종료한다.
    if key == ord('q'):
        break

    # 1 Keybord로 컬러모델 선택
    # 사용자가 'y' 키를 누르면 YCbCr 컬러 모델을 사용하여 피부색을 검출한다.
    elif key == ord('y'):

        # 2 선택된 컬러모델로 변환
        img_color = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
        # 3 픽셀 별로 피부색인지 확인
        mask = cv.inRange(img_color, (0, 133, 77), (255, 173, 127))
        # 4 피부색 출력
        skin_detection = cv.bitwise_and(img, img, mask=mask)
        cv.imshow('COLOR_BGR2YCrCb', skin_detection)
        cv.waitKey(0)

    # 사용자가 'h' 키를 누르면 HSV 컬러 모델을 사용하여 피부색을 검출한다.
    elif key == ord('h'):

        # 2 선택된 컬러모델로 변환
        img_color = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        # 3 픽셀 별로 피부색인지 확인
        mask = cv.inRange(img_color, (0, 70, 50), (50, 150, 255))
        # 4 피부색 출력
        skin_detection = cv.bitwise_and(img, img, mask=mask)
        cv.imshow('COLOR_BGR2HSV', skin_detection)
        cv.waitKey(0)

# 모든 창을 닫는다.
cv.destroyAllWindows()
