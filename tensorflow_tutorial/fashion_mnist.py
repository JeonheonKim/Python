import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist

# Data split [Training Set, Test Set]
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() 

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Normalization (0 ~ 1) : 학습의 속도와 local optimum 에 빠지지 않게 하기 위해 사용
train_images = train_images / 255.0 
test_images = test_images / 255.0

# Create Model 
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),     # 
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')    # SoftMax를 마지막 활성함수로 사용
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.summary()

model.fit(train_images, train_labels, epochs=5, verbose=0 )

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n테스트 정확도:', test_acc)

