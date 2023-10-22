import cv2 as cv
import sys

gray = cv.imread('coins.png', cv.IMREAD_GRAYSCALE)

if gray is None:
    sys.exit('파일을 찾을 수 없습니다.')

# 더 정확하게
median = cv.medianBlur(gray,3)

# binary_inverser로 동전이 흰색으로
_, gray_bin = cv.threshold(median, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY_INV)

# labels 어떤 애들이랑 연결되어있는가?
# labels는 입력사진이랑 동일하게 만든다.
# 배경은 0/ connectedComponents 동전에게 같은 번호로 라벨링
# stats에  xy 값 저장
cnt, labels, stats, centroids = cv.connectedComponentsWithStats(gray_bin)

# 색 있는 사각형으로 나타내주기 위해서
dst = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
dst[labels==0 ] = [127,127,127]
dst[labels==1] = [127,0,0]
dst[labels==2] = [0,127,0]
dst[labels==3] = [0,0,127]
dst[labels==4]= [0,127,127]

for i in range(1, cnt): # 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
    # stats에 저장되어있는 값으로 그림
    (x, y, w, h, area) = stats[i]

    # 노이즈 제거
    if area < 20:
        continue

    # 각각의 영역마다 번호를 줌
    cv.rectangle(dst, (x, y, w, h), (255, 0, 255), 2)
    # cv.rectangle(dst,(x,y),(x+w,y+h),(255,0,255),2)

cv.imshow('original', gray)
cv.imshow('binarization', gray_bin)
cv.imshow('dst', dst)

cv.waitKey()
cv.destroyAllWindows()