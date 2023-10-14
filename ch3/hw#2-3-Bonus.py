import cv2 as cv
import numpy as np

# 'rose.png' 이미지를 불러온다.
img = cv.imread('rose.png')
rows, cols = img.shape[:2]

# 현재 이미지를 복사하여 누적 회전을 위한 초기 이미지로 사용한다.
current_img = img.copy()

# 마우스 콜백 함수 정의
def rotate(event, x, y, flags, param):
    global current_img  # 전역 변수를 사용하여 현재 이미지를 업데이트한다.

    # 왼쪽 마우스 버튼 클릭 시 시계 반대 방향으로 회전
    if event == cv.EVENT_LBUTTONDOWN:
        src_point = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_point = np.float32([[0, rows - 1], [cols - 1, rows - 1], [0, 0]])
        affine_matrix = cv.getAffineTransform(src_point, dst_point)
        current_img = cv.warpAffine(current_img, affine_matrix, (cols, rows))
        cv.imshow('rotate', current_img)

    # 오른쪽 마우스 버튼 클릭 시 시계 방향으로 회전
    elif event == cv.EVENT_RBUTTONDOWN:
        src_point = np.float32([[0, 0], [0, rows - 1], [cols - 1, 0]])
        dst_point = np.float32([[cols - 1, 0], [0, 0], [cols-1, rows - 1]])
        affine_matrix = cv.getAffineTransform(src_point, dst_point)
        current_img = cv.warpAffine(current_img, affine_matrix, (cols, rows))
        cv.imshow('rotate', current_img)

# 이미지를 화면에 표시하고 마우스 콜백 함수를 설정한다.
cv.namedWindow('rotate')
cv.imshow('rotate', img)
cv.setMouseCallback('rotate', rotate)

# 사용자의 키 입력을 대기한다. 'q' 키를 누르면 프로그램을 종료한다.
while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
