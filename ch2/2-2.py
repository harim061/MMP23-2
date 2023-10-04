import cv2 as cv
import sys

img=cv.imread('soccer.jpg')	# 영상 읽기
# imread('파일이름')
# 다른 path면 위치 앞에 주면 됨


print(type(img))
# <class 'numpy.ndarray'> => 'soccer.jpg'는 numpy.ndarray

print(img.shape)
# (948, 1434, 3)
# (배열의 새로 크기, 배열의 가로 크기, 색상 크기 (각각의 화소 크기 = 3byte(color)))
# img.shape[0] = 948


# b g r
# (850,50)위치에 있는 화솟값
print(img[850,50,0], img[850,50,1],img[850,50,2])
print(img[450][500][0], img[450][500][1],img[450][500][2])
print(img[450][1000][0], img[450][1000][1],img[450][1000][2])

# 예외처리
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

# cv.imshow("생성될 윈도우창의 이름", 이미지)
cv.imshow('Image Display',img)	# 윈도우에 영상 표시


# waitKey()가 없으면 imshow() ->destroyAllWindows() 해줌
# 화면에서 보여지자 마자 바로 destroy해주기 떄문에
cv.waitKey()

# 사용한 위도우 종료하고 끝내라
cv.destroyAllWindows()