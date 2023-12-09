import cv2 as cv
import mediapipe as mp

img=cv.imread('BSDS_376001.jpg')

mp_face_detection=mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils

# face detection 설정
face_detection=mp_face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
# 모델 인덱스는 0 또느 1
# 0 : 카메라 2m이내의 부분적 모델 촬영
# 1 : 5m이내에서 전신 모델
# 지정하지 않으면 0

# 반드시 rgb
res=face_detection.process(cv.cvtColor(img,cv.COLOR_BGR2RGB))

if not res.detections:
    print('얼굴 검출에 실패했습니다. 다시 시도하세요.')
else:
    for detection in res.detections:
        print(detection)
        # score, relative_bounding_box,
        mp_drawing.draw_detection(img,detection)
    cv.imshow('Face detection by MediaPipe',img)

cv.waitKey()
cv.destroyAllWindows()