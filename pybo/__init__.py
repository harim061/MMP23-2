import os
import cv2 as cv
from flask import Flask, render_template, request, send_from_directory, Response
from werkzeug.utils import secure_filename
from .img_processing import embossing, cartoon, pencilGray, pencilColor, oilPainting, detailEnhance
import numpy as np
import sys

def create_app():
    app = Flask(__name__, static_url_path='')

    app.secret_key = os.urandom(24)
    app.config['RESULT_FOLDER'] = 'result_images'  # 반드시 폴더 미리 생성
    app.config['UPLOAD_FOLDER'] = 'uploads'  # 반드시 폴더 미리 생성


    # app.config에 선언한 upload folder 안에 있는 filename을 찾음
    @app.route('/upload_img/<filename>')
    def upload_img(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.route('/result_img/<filename>')
    def result_img(filename):
        return send_from_directory(app.config['RESULT_FOLDER'], filename)

    @app.route('/img_result', methods=['GET', 'POST'])
    def img_result():
        if request.method == 'POST':
            f = request.files['file']

            # /upload에 저장하기
            # 기본 path : pybo
            basepath = os.path.dirname(__file__)

            # 그 아래있는 uploads , 그 밑에 있는 filename
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            file_name = os.path.basename(file_path)
            img = cv.imread(file_path)

            # style 변수에 옵션 값 전달
            style = request.form.get('style')

            if style == "Embossing":
                output = embossing(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_emboss.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "Cartoon":
                output = cartoon(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_cartoon.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "PencilGray":
                output = pencilGray(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_pencilgray.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "PencilColor":
                output = pencilColor(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_pencilcolor.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "OilPainting":
                output = oilPainting(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_oil.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "Detail":
                output = detailEnhance(img)

                # /result_images에 저장
                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_detail.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
        return ''

    # /img_processing 요청이 들어왔을 때
    @app.route('/img_processing/',methods=['GET'])
    def img_processing():
        return render_template('img_processing.html')

    @app.route('/')
    def index():
        return render_template('index.html')


    return app




