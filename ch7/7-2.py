import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# 1) 데이터 수집
(x_train,y_train),(x_test,y_test)=ds.mnist.load_data()

# 2차원 -> 1차원
x_train=x_train.reshape(60000,784)
x_test=x_test.reshape(10000,784)

# 입력값(0-255)을 0-1로 정규화
x_train=x_train.astype(np.float32)/255.0
x_test=x_test.astype(np.float32)/255.0

#to_categorical : 정수 형식의 클래스 레이블을 one-hot 형식으로 변환하는데 사용
y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)

# 2) 모델 선택
mlp=Sequential()
# Dense 완전연결층  > 히든층
mlp.add(Dense(units=512,activation='tanh',input_shape=(784,)))
# Dense output 층
mlp.add(Dense(units=10,activation='softmax'))

# 3) 학습
# compile 학습 방법에 대한 지정
mlp.compile(loss='MSE',optimizer=SGD(learning_rate=0.01),metrics=['accuracy'])
# batch_size : 600000 / 128 = 4608번 => 1epoch
mlp.fit(x_train,y_train,batch_size=128,epochs=50,validation_data=(x_test,y_test),verbose=2)

# 모델 요약
mlp.summary()

# 4) 예측
res=mlp.evaluate(x_test,y_test,verbose=0)
print('정확률=',res[1]*100)

mlp.save('dmlp_trained.h5')