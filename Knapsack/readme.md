
# 🔵 Ⅱ. 超啟發式演算法
## 1. Hill Climbling

### ◻ 方法
1. **流程圖**
```mermaid
    graph LR;
    id1([初始解]) -- 每兩位元進行翻轉 --> id2[鄰居們];
    id2 -- 計算總重w,總價值v -->  id3[w=總重,v=價值]
    id3 --> id4{w合法<br>且v優於初始解?} 
    id4 -- 是 --> id5[取代初始解成暫時解]
    id4 -- 否 --> id6[初始解即暫時解]
    id5 ----> id7{遞迴結束?}
    id6 ----> id7
    id7 -- 是 --> id2
    id7 -- 否 --> id8([最終解])
```    

### ◻ 想法&發現
* **初始解**：(同SA)
    * random一範圍 $(2^{n}/2)$ ~ $2^{n}$ 的數 initNum (decimal)
        * 測試後發現，取較大的數，意同盡量**取重量較輕的**，所需的迭代次數較少，故原範圍 $1$ ~ $2^{n}$ ，改成從 $(2^{n}/2)$ 開始取
        * eg. 11000 (24) 優於 10011(19)
    * initNum轉為binary並分割成list(array)
    * 計算總重 & 總價值
    * 但扔會卡在「區域最佳解」
* **生成鄰居**
    * 基本作法：有一n bit的二進位數，每一bit做翻轉，
        * 例：n=3時，001有 ***1***01、0***1***1，00***0***
        * 需做n次
    * 我的想法：每隔兩位元再做一次翻轉
        * 例：n=5時，01001有 ***1***1001、01***1***01，00100***0***
        * 只需一半的時間
        * 補充在 【◻ 結果】
### ◻ 結果
1. 由程式&收斂圖(圖一)可發現，爬山演算法：
    * `優點`：容易實作
    * `缺點`：容易卡在 **「區域最佳解」**
    
2. 鄰居
    * 使用我的想法`「每兩bit」翻轉`，在資料數n不夠大時，較**不易取得(最靠近的)最佳解** (圖二)
    * 固本題n=15下，選用`「每一bit」翻轉` (圖一)

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HC2.jpg" width="auto" height="400" />

`圖一`


<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HC2-2.jpg" width="auto" height="400" />

`圖二`


### ◻ code review
> 省略部分Code，只擷取重要的部分
> 
> HC跟SA共用main.py程式碼，執行時可選擇要實施哪一個演算法
* **架構**
    ```
    |-- Knapsack   
    |--- p07_{c,p,w}.txt
    |--- main.py  
    |--- compoents.py  #功能函式們 (HC&SA共用)
    |--- varibles.py  #存放global變數&參數設定
    ```

1. **讀取txt檔**
    * 使用f stream讀取重量/容量/價值
   ```python
    for path in paths:
        f = open(path, 'r')
        if path == 'p07_c.txt' :
            varibles.capcity = int(f.read())
        ......
   ```
2. **Hill Climb演算法**
    * **初始化**
        * random"合法"的初始值/解
        * 並算出總價值&重量
        ```python
            compoents.initialState() #初始值/解

            def initialState():
                global best_state
                pickBound = math.pow(2, int(varibles.objNums)) #upperbound: 2^15
                while(1):
                    initNum = format(random.randrange(1, pickBound), 'b') #範圍: 1 - 2^15
                    blist = binToList(initNum) #拆成list
                    (w, v) = calTotalWandV(blist)  #計算weight & value

                    if w <= varibles.capcity: #是否合法
                        ......
        ```    
    * **main：開始執行500次迭代**
        ```python

            while i < varibles.iteraNum:
                stage = compoents.HillClimbing() 
                i += 1
        ```

    * **定義Neighbors鄰居**
        * 每元進行**翻轉**(0→1,1→0)    
        * 若**合法**(重量w符合)，且**更佳**(價值v大於原來的)，則**取代**初始解，成為新的初始解(暫時解)
         ```python

            def HillClimbing():
                temp_state = now_state.copy() #取得初始解
                for index, pick in enumerate(now_state['blist']): #遍歷每個位元
                    new_list = now_state['blist'].copy()
                    new_list[i] = int(not new_list[i])
                    (w, v) = calTotalWandV(new_list)
                    if w <= varibles.capcity: #合法
                        if v > temp_v: #新better than 舊
                            ......(取代)  
                #取代初始解,成為新的初始解(暫時解)
                NewState(temp_state['blist'], temp_state['weight'], temp_v)   
        ```
