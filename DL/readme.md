# 🔵 Ⅰ. 深度學習(Deep Learning)


### ◻ 想法&方法
> 我的電腦很雜，很多程式佔了空間不好清理，導致跑起來速度非常慢，也會遇到GPU不夠的情況，都需要慢慢去調整

1. **載入圖片**
    * 原本用file stream概念去Loop讀取，後來發現效率差，要花很長時間讀取，後改用`image_dataset_from_directory`
    * **image_dataset_from_directory**：[官方範例](https://www.tensorflow.org/tutorials/images/classification?hl=zh_tw)中使用的keras內建函式，可以很方便的對imgs進行處理
        * 如：圖片resize、batch大小、資料切割...)
        * [官方文件](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory)

2. **資料預處理**
    * 續上，將img陣列resize(統一規格)
    * 再將陣列每一元素 / 255成介於0-1的數 (減輕計算負擔)

3. **建模、訓練**
    * 使用CNN建三層
4. **印出相關資訊**
    * loss、accuracy 折線圖(收斂) (圖一)
        * 一開始有test data的accuracy卡住的情況，考慮是過度配適的問題，加上dropout
    * 混淆矩陣 (圖一)
        * 途中發現daisy偽真/假的情況特別多，後來發現是自己誤刪了部分圖片 
    * 隨機10張圖&其結果 (圖二)

---

### ◻ 結果

**準確率：98.4%**

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/m10.jpg" width="auto" height="400" />

`圖一`


<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/loss_acc.jpg" width="auto" height="400" />

`圖二`



### ◻ code review
0. **參數設定**
     ```python
    BATCH_SIZE = 32 #一次抓取的量
    IMG_SIZE = 128 
    epochs = 15 #步數
    ```

1. **讀取圖片(train/test data)**
    * 定義圖片資料夾路徑
     ```python
    data_dir = pathlib.Path('D:/lanac/deepLearning/DL/flowers')
    ```
2. **讀imgs&部分預處理**
    * seed：每次隨收成不同的值，去轉換data
    * image_size: 對所有圖片統一Size
    * batch_size: 一次抓取的量
    ```python
    
    train_data = tf.keras.preprocessing.image_dataset_from_directory(
      data_dir,
      seed=123,
      image_size=(IMG_SIZE, IMG_SIZE),
      batch_size=BATCH_SIZE
    )
    ```

3. **性能優化**
    * 根據官方文件的建議
    * .cache() : 第一次load後，會將img保存memory
    * .prefetch()：可以先做預處理
    ```python
    AUTOTUNE = tf.data.AUTOTUNE
    train_data = train_data.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    test_data = test_data.cache().prefetch(buffer_size=AUTOTUNE)
    ```    

4. **建模&部分預處理**
    * 圖片/255 -> 減輕計算負擔
    * 三層(卷積+池化)
        * 增加神經元數目，速度↓，準確度↑
        * DropOut：沒有dropout前，會有少部分「過度適配」情況，故每一層固定丟掉一些，增加隨機性
        * 回歸到Dense進行分類
        *  Relu的優點在於：收斂速度快
       ```python
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
       ```
5. **開始訓練**
    * adam：學習速度是動態的，跟著模型而調整
    * sparse_categorical_crossentropy：分類時常用這個
   ```python
    model.compile(
        optimizer='adam', 
        loss='sparse_categorical_crossentropy', #分類時常用
        metrics=['accuracy']
    )

    history = model.fit(
      train_data,
      validation_data=test_data,
      epochs=epochs
    )  
   ```
   
6. **讀取訓練資料**
    * 訓練後貼的標籤&真正的標籤
   ```python
    pred_labels = np.array([])
    test_labels = np.array([])
    for x, y in test_data:
        predictions = model.predict(x)
        pred_labels = np.concatenate([pred_labels, np.argmax(predictions,axis = 1) ])
        test_labels = np.concatenate([test_labels, y.numpy()])
   ```
   
   7. **畫圖**
       1. train data(訓練集) & test data(測試集)的 (圖一)
           * loss折線圖(收斂) 
           * accuracy折線圖(收斂)
        2. 混淆矩陣 (圖一)
        3. 隨機印出10張圖片&其結果 (圖二)


### ◻ 參考資料
 1. [TensorFlow官方分類範例](https://www.tensorflow.org/tutorials/images/classification?hl=zh_tw)
 2. [TensorFlow官方image_dataset_from_directory文件](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory)
