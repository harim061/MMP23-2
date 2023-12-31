import numpy as np
import cv2 as cv
import sys
# 한글 출력을 위한
from PIL import ImageFont,ImageDraw,  Image

# 욜로를 가져옴
def construct_yolo_v3():
    # 80개 물체를 저장해둠
    f=open('coco_names_kor.txt', 'r',encoding='UTF-8')
    class_names=[line.strip() for line in f.readlines()]

    model=cv.dnn.readNet('yolov3.weights','yolov3.cfg')
    layer_names=model.getLayerNames()
    print(layer_names)
    # out_layer 욜로의 결과를 출력하는 층 / 3개 존재
    out_layers=[layer_names[i-1] for i in model.getUnconnectedOutLayers()]
    print(out_layers)
    
    return model,out_layers,class_names

# 욜로를 이용함
def yolo_detect(img,yolo_model,out_layers):
    height,width=img.shape[0],img.shape[1]
    # 정규화, resize
    test_img=cv.dnn.blobFromImage(img,1.0/256,(448,448),(0,0,0),swapRB=True)
    
    yolo_model.setInput(test_img)
    output3=yolo_model.forward(out_layers)
    
    box,conf,id=[],[],[]		# 박스, 신뢰도, 부류 번호
    for output in output3:
        print(len(output))
        # 14x14 / 56x56 에 해당하는 블록의 크기 만큼
        for vec85 in output:
            scores=vec85[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            if confidence>0.5:	# 신뢰도가 50% 이상인 경우만 취함
                print(vec85)
                centerx,centery=int(vec85[0]*width),int(vec85[1]*height)
                w,h=int(vec85[2]*width),int(vec85[3]*height)
                x,y=int(centerx-w/2),int(centery-h/2)
                box.append([x,y,x+w,y+h])
                conf.append(float(confidence))
                id.append(class_id)

            # 겹친 정도가 40% 이하면 다른 물체이다.
    ind=cv.dnn.NMSBoxes(box,conf,0.5,0.4)
    objects=[box[i]+[conf[i]]+[id[i]] for i in range(len(box)) if i in ind]
    return objects

model,out_layers,class_names=construct_yolo_v3()		# YOLO 모델 생성
colors=np.random.uniform(0,255,size=(len(class_names),3))	# 부류마다 색깔

img=cv.imread('busy_street.jpg')
if img is None: sys.exit('파일이 없습니다.')

res=yolo_detect(img,model,out_layers)	# YOLO 모델로 물체 검출

# 한국어로 출력 1
font = ImageFont.truetype('fonts/gulim.ttc',20)
img_pil =Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)

for i in range(len(res)):			# 검출된 물체를 영상에 표시
    x1,y1,x2,y2,confidence,id=res[i]
    text=str(class_names[id])+'%.3f'%confidence
    # cv.rectangle(img,(x1,y1),(x2,y2),colors[id],2)
    # cv.putText(img,text,(x1,y1+30),cv.FONT_HERSHEY_PLAIN,1.5,colors[id],2)

    # 한국어로 출력 2
    draw.rectangle((x1,y1,x2,y2),outline=tuple(colors[id].astype(int)),width=2)
    draw.text((x1,y1+30), text,font=font,fill=tuple(colors[id].astype(int)),width=2)

# 한국어로 출력 3
img=np.array(img_pil)
cv.imshow("Object detection by YOLO v.3",img)

cv.waitKey()
cv.destroyAllWindows()