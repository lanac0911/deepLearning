import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from sklearn.metrics import confusion_matrix
import seaborn as sn

from tensorflow import keras
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.layers import Rescaling
from tensorflow.keras.models import Sequential
import pathlib
import random


data_dir = pathlib.Path('D:/lanac/deepLearning/DL/flowers')

#參數設定
BATCH_SIZE = 32 #一次抓取的量
IMG_SIZE = 128 
epochs = 15 #步數

#讀imgs
train_data = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
#   color_mode='grayscale',
  seed=123,
  image_size=(IMG_SIZE, IMG_SIZE),
  batch_size=BATCH_SIZE
)

test_data = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
#   color_mode='grayscale',
  seed=456,
  image_size=(IMG_SIZE, IMG_SIZE),
  batch_size=BATCH_SIZE
)  

class_names = train_data.class_names #['daisy','dandelion','rose','sunflower','tulip']


#---性能優化---------
AUTOTUNE = tf.data.AUTOTUNE
#.cache() : 第一次load後，會將img保存memory 
#.prefetch()：可以先做預處理
train_data = train_data.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
test_data = test_data.cache().prefetch(buffer_size=AUTOTUNE)


#########################################
#---建模---------
model = Sequential([
    Rescaling(1.0/255 ,input_shape=(IMG_SIZE, IMG_SIZE, 3)), #標準化(因0-255組)
    #第一層
    Conv2D(16, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),
    #第二層
    Conv2D(32, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),
    #第三層
    Conv2D(64, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),
    #攤平、連接
    Flatten(),
    Dense(128,   activation='relu'),
    Dense(5, activation='softmax'),
])

#---------訓練----------
model.compile(
    optimizer='adam', #adam:學習速度是動態的
    loss='sparse_categorical_crossentropy', #分類時常用
    metrics=['accuracy']
)

history = model.fit(
  train_data,
  validation_data=test_data,
  epochs=epochs
)  

scores = model.evaluate(test_data)  


#---抓lables----------
pred_labels = np.array([])
test_labels = np.array([])
for x, y in test_data:
    predictions = model.predict(x)
    pred_labels = np.concatenate([pred_labels, np.argmax(predictions,axis = 1) ])
    test_labels = np.concatenate([test_labels, y.numpy()])


#->>>>>>>>>>>>>>>> 畫圖區PLT <<<<<<<<<<<<<<<<<<<<<<<<

acc = history.history['accuracy'] #訓練集正確率
val_acc = history.history['val_accuracy'] #測試集正確率
loss = history.history['loss'] #訓練集loss
val_loss = history.history['val_loss'] #測試集loss
epochs_range = range(epochs)

#1.折線圖
epochs_range = range(epochs)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label=' Accuracy')
plt.plot(epochs_range, val_acc, label=' Accuracy')
plt.legend(loc='lower right')
plt.title('Accuracy')
plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label=' Loss')
plt.plot(epochs_range, val_loss, label=' Loss')
plt.legend(loc='upper right')
plt.title('Loss')

#2.混淆矩陣
CM = confusion_matrix(test_labels, pred_labels)
plt.figure()
ax = plt.axes()
sn.heatmap(
    CM, annot=True, 
    annot_kws={"size": 10}, 
    xticklabels=class_names, 
    yticklabels=class_names, ax = ax
)
ax.set_title('Confusion matrix')

#3.隨機取10張
index = 1
plt.figure(figsize=(12, 10))
for images, labels in test_data.take(1): #拿一bacth的量(32)
    pred_labels_slice = pred_labels[:32].astype(int)
    rand_list = random.sample(range(0, BATCH_SIZE-1), 10) #隨機取10個
    for i in rand_list:
        plt.subplot(4, 4, index)
        plt.tight_layout()
        plt.axis('off')
        #顯示結果
        text = class_names[labels.numpy()[i]] 
        text = text + '  (Correct)' if labels.numpy()[i] == pred_labels_slice[i] else text + '   (Incorrect)'  
        plt.title(text)
        plt.imshow(images[i].numpy().astype("uint8"))
        index += 1

plt.show()