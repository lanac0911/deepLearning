# 🔵 Ⅰ. 深度學習(Deep Learning)
 ### code review
1. 讀取圖片(train/test data) 
    * 定義分類名稱(form資料夾)
    * 透過loop將所有圖片貼標(分類)，並規格化(resize...)
     ```python
     class_names = ['daisy','dandelion','rose','sunflower','tulip']
    ```
2. 將train/test data 的label,images分出來操作
    * label以int型態儲存
    * images以float型態儲存
    * 將train資料打亂(for隨機性)
    ```python
    X = [] #images
    Y = [] #labels
    for features, labels in data:
        X.append(features)
        Y.append(labels)
    X = np.array(X, dtype = 'float32')
    Y = np.array(Y, dtype = 'int32')
    ```

3. 將分類資訊以pkl(pickle)儲存
    * 下次使用可直接載入使用，省時
   ```python
    #pickle儲存
    pickle.dump(train_images, open('train_images.pkl', 'wb'))
    #pickle讀取
    train_images = pickle.load(open('train_images.pkl', 'rb'))
    ```
    
4. 針對images標準化
    * / 255，因三原色範圍由0-255
   ```python
    train_images = train_images / 255 
    ```    
----
5. 建模
