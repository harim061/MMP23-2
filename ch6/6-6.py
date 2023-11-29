import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys


# opencv-contrib-python 설치: xphoto
# opencv-contrib-python = opencv-python + extra

class SpecialEffect(QMainWindow):
    def __init__(self): # 초기화면
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200, 200, 800, 200)

        pictureButton = QPushButton('사진 읽기', self)
        embossButton = QPushButton('엠보싱', self)
        cartoonButton = QPushButton('카툰', self)
        sketchButton = QPushButton('연필 스케치', self)
        oilButton = QPushButton('유화', self)
        motionButton = QPushButton('모션블러',self)
        saveButton = QPushButton('저장하기', self)

        #ComboBox
        self.pickCombo = QComboBox(self)
        #addItmes로 넣을 부분 나열 [ ] 배열 처리 index로 현재 위치 나타냄
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화', '모션블러'])  # 항목 나열(각 메뉴), 배열로 인덱스, 0부터 시작
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)

        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        motionButton.setGeometry(510, 10, 100, 30)
        saveButton.setGeometry(610, 10, 100, 30)
        self.pickCombo.setGeometry(610, 40, 110, 30)
        quitButton.setGeometry(720, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 170)

        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction)
        motionButton.clicked.connect(self.motionBlurFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        # 콤보박스의 클릭 시의 콜백함수는 여기 x, 버튼의 콜백함수 내에서 인덱스 활요해서 사용

    def pictureOpenFunction(self):
        fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        self.img = cv.imread(fname[0])
        if self.img is None: sys.exit('파일을 찾을 수 없습니다.')

        cv.imshow('Painting', self.img)

    def motionBlurFunction(self):
        motionFliter = np.ones((1, 30)) * (1 / 30)  # 합 = 1
        self.motion = cv.filter2D(self.img, -1, motionFliter)
        cv.imshow("Motion Blur", self.motion)

    def embossFunction(self):
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])

        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)  # 음수 처리 위해 16비트로 바꿔줘야 함
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))

        cv.imshow('Emboss', self.emboss)

    def cartoonFunction(self):
        self.cartoon = cv.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv.imshow('Cartoon', self.cartoon)

    def sketchFunction(self):
        self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
        cv.imshow('Pencil sketch(gray)', self.sketch_gray)
        cv.imshow('Pencil sketch(color)', self.sketch_color)

    def oilFunction(self):
        self.oil = cv.xphoto.oilPainting(self.img, 10, 1,
                                         cv.COLOR_BGR2Lab)  # img의 BGR 중 0번 채널 (B)만 처리, BGR2Lab > L채널 사용(gray값에 해당하는 내용)
        cv.imshow('Oil painting', self.oil)

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')

        # 콤보박스 누가 선택 되었는지 값 리턴
        i = self.pickCombo.currentIndex()
        if i == 0:
            # emboss -> embossFun에서 self.emboss한 값
            cv.imwrite(fname[0], self.emboss)
        elif i == 1:
            cv.imwrite(fname[0], self.cartoon)
        elif i == 2:
            cv.imwrite(fname[0], self.sketch_gray)
        elif i == 3:
            cv.imwrite(fname[0], self.sketch_color)
        elif i == 4:
            cv.imwrite(fname[0], self.oil)
        elif i == 5:
            cv.imwrite(fname[0], self.motion)

    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()


app = QApplication(sys.argv)
win = SpecialEffect()
win.show()
app.exec_()