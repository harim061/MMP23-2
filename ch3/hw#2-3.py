import cv2 as cv
import numpy as np

# 이미지를 불러온다.
img = cv.imread('rose.png')

# 이미지의 크기를 조절한다.
img = cv.resize(img, dsize=(500, 500))
rows, cols = img.shape[:2]

current_img = img.copy()

# 마우스 콜백 함수
def rotate(event, x, y, flags, param):
    global current_img  # 전역 변수 사용

    # 1 왼쪽 마우스 버튼 클릭 시 시계 반대 방향으로 회전
    if event == cv.EVENT_LBUTTONDOWN:
        src_point = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_point = np.float32([[0, rows - 1], [cols - 1, rows - 1], [0, 0]])
        affine_matrix = cv.getAffineTransform(src_point, dst_point)
        current_img = cv.warpAffine(current_img, affine_matrix, (cols, rows))
        cv.imshow('rotate', current_img)

    # 2 오른쪽 마우스 버튼 클릭 시 시계 방향으로 회전
    elif event == cv.EVENT_RBUTTONDOWN:
        src_point = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_point = np.float32([[cols - 1, 0], [0, 0], [cols-1, rows - 1]])
        affine_matrix = cv.getAffineTransform(src_point, dst_point)
        current_img = cv.warpAffine(current_img, affine_matrix, (cols, rows))
        cv.imshow('rotate', current_img)

# 이미지 표시 및 마우스 콜백 함수 설정
cv.namedWindow('rotate')
cv.imshow('rotate', img)
cv.setMouseCallback('rotate', rotate)

# 사용자 키 입력 대기
while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
