import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle           
import seaborn as sn
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Activation, Dropout, Flatten

data_dir = ['flowers', 'flowers_test']
# data_dir = 'D:/myProject(D)/2022Project/DeepLearning/flowers_test'
class_names = ['daisy','dandelion','rose','sunflower','tulip']

IMG_SIZE = 100
train_data = []
test_data = []

for dir in data_dir:
    for clas in class_names:
        folder = os.path.join(dir, clas)  #'daisy','dandelion','rose','sunflower','tulip'
        label = class_names.index(clas)
        print("Loading",clas, "...")
        for img in os.listdir(folder):
            #讀取+處理
            img_path = os.path.join(folder, img)
            img_arr = cv2.imread(img_path)
            img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)
            img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
            #label
            if dir == 'flowers' :
                train_data.append([img_arr, label])
            else:
                test_data.append([img_arr, label])
    
#        
# random.shuffle(train_data)

train_images = []
test_images = []
train_labels = []
test_labels = []

def load_data(data):
    X = [] #images
    Y = [] #labels
    for features, labels in data:
        X.append(features)
        Y.append(labels)
    X = np.array(X, dtype = 'float32')
    Y = np.array(Y, dtype = 'int32')
    return (X, Y)

(train_images,train_labels) = load_data(train_data)
(test_images,test_labels) = load_data(test_data)
train_images, train_labels = shuffle(train_images, train_labels, random_state=25)


print("train_images len",len(train_images))
print("test_images len",len(test_images))
print("train_images.shape",train_images.shape)
print("test_images.shape",test_images.shape)
print("test_images lab",test_labels)
print("train_images lab",train_labels)
##
# #pickle儲存
# pickle.dump(train_images, open('train_images.pkl', 'wb'))
# pickle.dump(train_labels, open('train_labels.pkl', 'wb'))
#pickle讀取
# train_images = pickle.load(open('train_images.pkl', 'rb'))
# train_labels = pickle.load(open('train_labels.pkl', 'rb'))

#標準化
print("------------------------------")

train_images = train_images / 255 
print("train_images len",len(train_images))
print("test_images len",len(test_images))
print("train_images.shape",train_images.shape)
print("test_images.shape",test_images.shape)
print("test_images lab",test_labels)
print("train_images lab",train_labels)
#訓練
input_shape = (IMG_SIZE, IMG_SIZE, 3)
model = Sequential([
    Conv2D(16, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),

    Conv2D(32, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),

    Conv2D(64, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.2),

    Flatten(),
    Dense(128,  input_shape=train_images.shape[1:], activation='relu'),
    Dense(5, activation='softmax'),
])
print("訓練",len(train_images),"張資料")
#model執行
epochs = 10
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_images, train_labels,
    epochs=epochs, 
    # batch_size=128, 
    validation_split=0.1
)

#測試
scores = model.evaluate(test_images, test_labels)  
print("scores=",scores[1]) #[0]:loss [1]:accuracy

#預測
predictions = model.predict(test_images)     # Vector of probabilities
pred_labels = np.argmax(predictions, axis = 1)  # 取出機率最大的 index
print('pred_labels:',pred_labels)


##---PLT----------------------------
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

#1. loss折線圖
plt.title('train_loss')
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.plot(loss)
#1.2
epochs_range = range(epochs)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')

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
test_images = test_images.astype('uint8')
plt.figure(figsize=(12,6))
for i in range(0, 10, 1):
    plt.subplot(4, 4, i+1)
    plt.tight_layout()
    plt.axis('off')
    # prob = predictions[pred_labels[i]]
    # print('prob:',prob)
    index = pred_labels[i]
    text = class_names[test_labels[i]] 
    text = text + '  (Correct)' if test_labels[i] == pred_labels[i] else text + '   (Incorrect)'  
    plt.title(text)
    plt.imshow(test_images[i])
plt.show()