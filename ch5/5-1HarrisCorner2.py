import cv2 as cv
import numpy as np
import sys

# 10 / 26

# 콜백함수 저장해둬서 자동으로 실행됨
def onCornerHarris(thresh):
    # 정규화를 시킴 -> 트랙바는 정수만 다루기 때문
    CN = cv.normalize(C, 0, 400, cv.NORM_MINMAX)
    rcorners = []
    for j in range(1, C.shape[0] - 1):  # 비최대 억제
        for i in range(1, C.shape[1] - 1):
            if CN[j, i] > thresh and sum(
                sum(CN[j, i] > CN[j - 1:j + 2, i - 1:i + 2])) == 8:  # 주변 8개와 비교해서 [ji]가 더 큰 값이 8이면, 모든 이웃보다 큰값을 가지면

                # 코너들을 모아두고
                rcorners.append((i, j))
    # 한번에 그려줌
    for pt in rcorners:
        cv.circle(img, pt, 3, (255, 0, 255), -1)  # 좌표 표시
    print("임계값: %2d , 코너 개수: %2d" % (thresh, len(rcorners)))
    # createTracbar 2번째 인자랑 같음 / 여기에 트랙바를 붙이겠다!
    cv.imshow("harris detect", img)


img = cv.imread('shapes3.png', cv.IMREAD_COLOR)
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

median = cv.medianBlur(img, 3)
gray = cv.cvtColor(median, cv.COLOR_BGR2GRAY)

blockSize = 4  # 이웃 화소 범위
apertureSize = 3  # 소벨 마스크 크기
k = 0.04
thresh = 5  # 코너 응답 임계값

# 반드시 gray!! / blockSize = patch의 크기 / apertureSize = sobel mask 크기 / k = 응답함수 계산을 위한 상수값
C = cv.cornerHarris(gray, blockSize, apertureSize, k)  # OpenCV 제공 함수

onCornerHarris(thresh)

# createTrackbar 이벤트 생성
# (변수 이름,창의 이름, 변수 이름 => track bar가 현재 가리키는 지점, 최대값, 좌우로 움직일 때 마다 자동으로 호출되는 콜백함수)
cv.createTrackbar("Threshold", "harris detect", thresh, 30, onCornerHarris)


cv.waitKey(0)
cv.destroyAllWindows()