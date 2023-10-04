import cv2 as cv
import sys


# 웹캡이 있는 경우 카메라와 연결 시도
# cv.VideoCapture(노트북에 있는 웹캠 ,cv.CAP_DSHOW)
# cap=cv.VideoCapture(0, cv.CAP_DSHOW)

# 동영상 파일
cap=cv.VideoCapture('../ch10/slow_traffic_small.mp4')

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
while True:
    # 비디오를 구성하는 프레임 획득
    ret,frame=cap.read() # ret(frame을 잘 불러왔는가 T or F) , frame(2차원의 이미지)

    # 더이상 frame이 없을 때 (ex.웹캠을 끔, 동영상 다 플레이 했을 떄)
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    # gray 영상으로 바꿔보기
    frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # 영상 절반크기
    frame = cv.resize(frame, dsize=(0,0),fx=0.5,fy=0.5)

    cv.imshow('Video display',frame)
    
    key=cv.waitKey(1)	# 1밀리초 동안 키보드 입력 기다림
    if key==ord('q'):	# 'q' 키가 들어오면 루프를 빠져나감
        break 

# 자원정리
cap.release()			# 카메라와 연결을 끊음
cv.destroyAllWindows()