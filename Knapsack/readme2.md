

# ðµ â¡. è¶åç¼å¼æ¼ç®æ³
## 2. Simulation Annealing

---

### 12/17 æ´æ°(å¹³æ»å)
* **åæ¬(åé¡)**ï¼
    * å¨åå¹¾æ¬¡æ¾è§£çéç¨ä¸­ï¼æ¯æ¬¡é½ååå¤§éçè¨ç®ï¼æä»¥å¾å¿«å°±éå°ãå±±é ãï¼ä½¿æ¾è³æçéç¨ä¸­åºç¾**æ·å±¤**ï¼æ²æå¥½å¥½å©ç¨ã***éç«éç¨æ­¥æ­¥é¼æ¬æä½³è§£***ãçéç¨ (åA)
* **åæ¬(ç¼ç¾)**ï¼
    * æ¯åæº«åº¦å¨çæé°å±æ¯å°ãæä½³è§£ãããæ«æè§£ãæï¼é½**ånæ¬¡**ï¼ç¶nå¤§ï¼æ¯å**è¨ç®è¤é**ï¼å®¹æè¼å¿«æ¾å°è§£ç­ï¼ä½ä¹èæè½ãä¹æé ææ·å±¤

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/SA1.jpg" width="auto" height="400" />

`åA`

---
* **åªåï¼æ¾é°å±**ï¼
    1. åæ¬æ¯å(æº«åº¦)ånæ¬¡ï¼æ¹**ç±randomä¸æ¸r**ï¼å**rå** (ç¯åï¼**$n/2$ ~ $n$**)

* **åªåï¼æ³æ³**ï¼
    * è¨­è¨éæ¨£çæ¹å¼ä¸»è¦æ¯ç¶éè§å¯å¾ï¼å¾å®¹æå¤ªæ©æ¾å°å±±é ï¼æ²æä¸æ­¥æ­¥é¼è¿ï¼æä»¥å°å®åç¯åç¸®å°+ä¸åºå®ï¼è®æ¸æç¡éåæ»
    * å¦å¤ç¶éè©¦é©ï¼å°**Tæé«1.5å (=200)**ï¼**è¨çæº«åº¦æé«10å(=10)**ã **æ¶æéåº¦åæ¢(=0.95)** ä¸é»ï¼å¾å°ä»¥ä¸è¶¨å¢å (åB)
    ```python
        while t >= TF:
            exe_time = random.randrange(int(varibles.objNums/2), int(varibles.objNums)) #è©²æº«åº¦è¦åå¹¾æ¬¡ (n/2 ~ n)
            for index in range(exe_time):
                ##æ¯å°
                ........
                ........
    ```

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/SIM.jpg" width="90%" height="AUTO" />

---


### â» æ¹æ³
1. **æµç¨å**
```mermaid
    graph RL;
    id1([åå§è§£<br>è¨­çºæä½³,æ«æè§£]) -- æ¯ä½åé²è¡ç¿»è½ --> id2[æ¾é°å±:é°å±å=ç¶åè§£];
    id2 -- è¨ç®ç¸½éw,ç¸½å¹å¼v -->  id3[w=ç¸½é,v=å¹å¼]
    id3 --> id4{wåæ³?} 
    id4 -- å¦ --> id2    
    id4 -- æ¯ --> id5{våªæ¼æä½³?}  
    id5 -- æ¯ --> id6[æ¿æææä½³è§£]
    id5 -- å¦ --> id7{våªæ¼ç¶å?} 
    id6 --> id7
    id7 -- æ¯ --> id8[æ¿ææç¶åè§£]
    id7 -- å¦ --> id9{é¨æ©æ©çr<br>å°æ¼åè¨±æ©ç?}
    id9 -- æ¯ --> id8
    id9 -- å¦ --> id10{ç®åæº«åº¦ä¸æ¯å¦ååæç´¢é°å±?}
    id10 -- å¦ --> id2 
    id10 -- æ¯ --> id11{æ¯å¦ç¿»è½å®ç¢?}
    id11 -- å¦ --> id13[éç«]
    id13 --> id2
    id11 -- æ¯ --> id12[æçµè§£]
```    

  
### â» æ³æ³&ç¼ç¾
* **åå§è§£**ï¼(åHC)
    * randomä¸ç¯å $(2^{n}/2)$ ~ $2^{n}$ çæ¸ initNum (decimal)
        * æ¸¬è©¦å¾ç¼ç¾ï¼åè¼å¤§çæ¸ï¼æåç¡é**åééè¼è¼ç**ï¼æéçè¿­ä»£æ¬¡æ¸è¼å°ï¼æåç¯å $1$ ~ $2^{n}$ ï¼æ¹æå¾ $(2^{n}/2)$ éå§å
        * eg. 11000 (24) åªæ¼ 10011(19)
    * initNumè½çºbinaryä¸¦åå²ælist(array)
    * è¨ç®ç¸½é & ç¸½å¹å¼
* **çæé°å±**
    * åºæ¬ä½æ³ï¼æä¸n bitçäºé²ä½æ¸ï¼æ¯ä¸bitåç¿»è½ï¼
        * ä¾ï¼n=3æï¼001æ ***1***01ã0***1***1ï¼00***0***
        * éånæ¬¡
    * æçæ³æ³ï¼æ¯éå©ä½åååä¸æ¬¡ç¿»è½
        * ä¾ï¼n=5æï¼01001æ ***1***1001ã01***1***01ï¼00100***0***
        * åªéä¸åçæé
        * ä½å¨ç¶åæº«åº¦ä¸çæå°æ¬¡æ¸å¤ªå°
* **åå§æº«åº¦Tï¼æ¶æéåº¦RATIO**ï¼
    * RATIOï¼
        * å¤§ï¼éæº«å¿«ï¼è¼æ©éå¹³è¡¡(ç©©å®)ï¼ä½ä¹è¼å¯è½æ¾ä¸å°æä½³è§£
        * å°ï¼éæº«æ¢ï¼è¼èæï¼ä½ä¹å®¹æéå°æä½³è§£
        * æ ¹ææ¸¬è©¦RATIO>=0.85æï¼ãå¹¾ä¹ãé½å¯éæä½³è§£ï¼æä»¥æ­¤é¡å=0.9çºæä½³
    * Tï¼ å½±é¿è§£çæç´¢ç¯å
        * æ ¹ææ¸¬è©¦T>150æï¼è¼å¿«å¾å°å¹³è¡¡ï¼æä»¥æ­¤é¡å=180çºæä½³

### â» çµæ
1. æ¨¡æ¬éç«æ¼ç®æ³ï¼
    * `åªé»`ï¼è¼ä¸æå¡å¨ãååæä½³è§£ã
    * `ç¼ºé»`ï¼**ãæ¶æææã** å®¹æ**è¢«åå§è§£ãæº«åº¦ç­è¨­å®å½±é¿**ï¼æææéè¦è¼é·çæ¶ææéï¼ææ100æ¬¡å§å³å¯
    
<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/SA1.jpg" width="auto" height="400" />



### â» code review
> çç¥é¨åCodeï¼åªæ·åéè¦çé¨å
> 
> HCè·SAå±ç¨main.pyç¨å¼ç¢¼ï¼å·è¡æå¯é¸æè¦å¯¦æ½åªä¸åæ¼ç®æ³
* **æ¶æ§**
    ```
    |-- Knapsack   
    |--- p07_{c,p,w}.txt
    |--- main.py  
    |--- compoents.py  #åè½å½å¼å (HC&SAå±ç¨)
    |--- varibles.py  #å­æ¾globalè®æ¸&åæ¸è¨­å®
    ```

1. **è®åtxtæª**
    * ä½¿ç¨f streamè®åéé/å®¹é/å¹å¼
   ```python
    for path in paths:
        f = open(path, 'r')
        if path == 'p07_c.txt' :
            varibles.capcity = int(f.read())
        ......
   ```
2. **Simulation Annealingæ¼ç®æ³**
    * **åå§å**
        * random"åæ³"ç**åå§å¼/è§£**ï¼åè¨­çºBest
        * ä¸¦ç®åºç¸½å¹å¼&éé
        ```python
            compoents.initialState() #åå§å¼/è§£

            def initialState():
                global best_state
                pickBound = math.pow(2, int(varibles.objNums)) #upperbound: 2^15
                min = int(pickBound/2) 

                while(1):
                    initNum = format(random.randrange(min, pickBound), 'b') #ç¯å: (2^15/2) - 2^15
                    blist = binToList(initNum) #æælist
                    (w, v) = calTotalWandV(blist)  #è¨ç®weight & value

                    if w <= varibles.capcity: #æ¯å¦åæ³
                        ......
        ```    
    * **mainï¼éå§å·è¡500æ¬¡è¿­ä»£**
        ```python

            while i < varibles.iteraNum:
                stage = compoents.HillClimbing() 
                i += 1
        ```

    * **éç«éç¨**
        * åå§åæ¸è¨­å®
         ```python
            T0 = 180 #åå§æº«åº¦ (å½±é¿è§£çæç´¢ç¯å)
            TF = 1 #è¨çæº«åº¦
            RATIO = 0.9 #æ¶æéåº¦ (éå¿«è¼å¯è½æ¾ä¸å°æä½³è§£)
        ```
        * ç¶å¨æº«åº¦ç¯åå§ï¼æçºæç´¢/çæé°å±å(ç¶åè§£)
        ```python
        while t >= TF:
            for index, pick in enumerate(now_state['blist']): #éæ­·æ¯åä½å
                (now_w, now_v) = calTotalWandV(now_state['blist'])
                #çæ neighbors(test)
                test_list = now_state['blist'].copy()
                test_list[index] = int(not pick)
                (test_w, test_v) = calTotalWandV(test_list)
        ```
        * ãé°å±ãèBestãç¶åè§£æ¯è¼ï¼æ¯å¦åä»£æä½³è§£/ç¶åè§£
            * æä½³è§£Bestï¼é°å±åªæ¼Best â åä»£
            * ç¶åè§£Nowï¼
                * é°å±åªæ¼Now â åä»£
                * é°å±æ²åªæ¼Now â è¨ç®probaï¼é¨æ©çææ©çrï¼æ¯è¼probaãråæ±ºå®æ¯å¦åä»£
        ```python
         #!!çºåé¢while!!
           #bestæ´æ°
            if test_w > varibles.capcity: continue #éæ³ï¼è·³é
            if test_w <= varibles.capcity: #åæ³
                if test_v > best_state['value']: #æ°better than è
                    best_state['blist'] = test_list
                    best_state['weight'] = test_w
                    best_state['value'] = test_v
                    flag = True    
            #nowæ´æ°
            if test_v > now_v : #åªæ¼ç¶åè§£ -> æ´æ°
                UpdateNowState(test_list, test_w, test_v)
            else: #ç±æ©çå¤æ·
                proba = float(test_v - now_v) / t
                if(random.random() < math.exp(proba)):
                    UpdateNowState(test_list, test_w, test_v)       
        ```
        * éæº«
        ```python
            t *= RATIO 
        ```
        
