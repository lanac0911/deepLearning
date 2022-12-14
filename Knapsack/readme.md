
# ðµ â¡. è¶åç¼å¼æ¼ç®æ³
## 1. Hill Climbling
---
### 12/17 æ´æ°(å¹³æ»å)
* **åæ¬(åé¡)**ï¼
    * æ²æé©ç¶å©ç¨ãç¬å±±æ¼ç®æ³ãä¸æ­¥æ­¥ç¬(æ¾é°å±)çç¹æ§ï¼å¨åå¹¾æ¬¡ç¬çéç¨ä¸­ï¼**å¾å¿«å°±éå°ç¬¬ä¸åãå±±é ã**ï¼å°è´é²éå©é£å¡å¨é£é (åA)
* **åæ¬(ç¼ç¾)**ï¼
    * **æ¯é1 bit å°±é²è¡ç¿»è½**(**å±énæ¬¡**)ï¼ç¶è§å¯ï¼æå¤§çåå æ¯ï¼åå¹¾é¨çè·¯ç·å·²ç¶**èå¥½èæ»¿**ï¼å¾å®¹æå°±è¶éå®¹éãææå°æ¾é°å±çéç¨åäºåªåã

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HC2.jpg" width="auto" height="400" />

`åA`

---
* **åªåï¼æ¾é°å±**ï¼
    1.  å°binaryæ¸**åæååãå¾å**(æ¬éè¼ãæ¬éé)(å·²ç±å° â å¤§æåº)
    2. ãå ä¸åï¼æ¸ä¸åãæä½é½è¦å¾ãååãå¾åãä¸­é¸ä¸å(æ¯æ¬¡ç±é¨æ©æ©çæ±ºå®)
   3. è¥åå¥½ååãå¾åé½ç¡æ³åå æ¸
   4. åé¨æ©åä¸ä½ååç¿»è½
* **åªåï¼æ³æ³**ï¼
    * è¨­è¨éæ¨£çæ¹å¼ä¸»è¦æ¯çºäºï¼**æ¨è¼åé/æ¨éåè¼**ï¼è®å®¹éé¨æä¸ç´è¢«åéå¶ï¼èæ¯å¯ä¾ååæ¯å°ãä¿®æ­£ (åB)

    ```python
    ------- (callee)
    def delOrAdd_HeavyOrLight(list, mode):
        # mode=0åå¢å  , mode=1ååªæ¸
        hasNeig = False; d = dict()
        indices = [i for i, x in enumerate(list) if x == mode]
        if(len(indices) >= 1): #åªä¸åè¼ç
            idx = random.choice(indices) #é¨æ©æä¸å1
            list[idx] = int(not mode)#åª
            hasNeig = True
        d['flag'] = hasNeig 
        d['new_oper_list'] = list 
        return d

    ------- (caller)
        doAdd = random.random() #ååãå¾åèª°è¦åå 
        doDel = random.random() #ååãå¾åèª°è¦åæ¸
        #å ------
        if doAdd > 0.5: #éç+1
            res = delOrAdd_HeavyOrLight(end_list, 0)  #add Heavy
        else: #è¼ç+1
            res = delOrAdd_HeavyOrLight(front_list, 0) #add Light
        #æ¸-------
        if doDel > 0.5: #éç-1
            res = delOrAdd_HeavyOrLight(end_list, 1) #del Heavy    
        else: #è¼ç-1
            res = delOrAdd_HeavyOrLight(front_list, 1) #del Light


    ```

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HILL.jpg" width="auto" height="600" />

`åB`

---

### â» æ¹æ³
1. **æµç¨å**
```mermaid
    graph LR;
    id1([åå§è§£]) -- æ¯å©ä½åé²è¡ç¿»è½ --> id2[é°å±å];
    id2 -- è¨ç®ç¸½éw,ç¸½å¹å¼v -->  id3[w=ç¸½é,v=å¹å¼]
    id3 --> id4{wåæ³<br>ä¸våªæ¼åå§è§£?} 
    id4 -- æ¯ --> id5[åä»£åå§è§£ææ«æè§£]
    id4 -- å¦ --> id6[åå§è§£å³æ«æè§£]
    id5 ----> id7{éè¿´çµæ?}
    id6 ----> id7
    id7 -- æ¯ --> id2
    id7 -- å¦ --> id8([æçµè§£])
```    

### â» æ³æ³&ç¼ç¾
* **åå§è§£**ï¼(åSA)
    * randomä¸ç¯å $(2^{n}/2)$ ~ $2^{n}$ çæ¸ initNum (decimal)
        * æ¸¬è©¦å¾ç¼ç¾ï¼åè¼å¤§çæ¸ï¼æåç¡é**åééè¼è¼ç**ï¼æéçè¿­ä»£æ¬¡æ¸è¼å°ï¼æåç¯å $1$ ~ $2^{n}$ ï¼æ¹æå¾ $(2^{n}/2)$ éå§å
        * eg. 11000 (24) åªæ¼ 10011(19)
    * initNumè½çºbinaryä¸¦åå²ælist(array)
    * è¨ç®ç¸½é & ç¸½å¹å¼
    * ä½ææå¡å¨ãååæä½³è§£ã
* **çæé°å±**
    * åºæ¬ä½æ³ï¼æä¸n bitçäºé²ä½æ¸ï¼æ¯ä¸bitåç¿»è½ï¼
        * ä¾ï¼n=3æï¼001æ ***1***01ã0***1***1ï¼00***0***
        * éånæ¬¡
    * æçæ³æ³ï¼æ¯éå©ä½åååä¸æ¬¡ç¿»è½
        * ä¾ï¼n=5æï¼01001æ ***1***1001ã01***1***01ï¼00100***0***
        * åªéä¸åçæé
        * è£åå¨ ãâ» çµæã
### â» çµæ
1. ç±ç¨å¼&æ¶æå(åä¸)å¯ç¼ç¾ï¼ç¬å±±æ¼ç®æ³ï¼
    * `åªé»`ï¼å®¹æå¯¦ä½
    * `ç¼ºé»`ï¼å®¹æå¡å¨ **ãååæä½³è§£ã**
    
2. é°å±
    * ä½¿ç¨æçæ³æ³`ãæ¯å©bitãç¿»è½`ï¼å¨è³ææ¸nä¸å¤ å¤§æï¼è¼**ä¸æåå¾(æé è¿ç)æä½³è§£** (åäº)
    * åºæ¬é¡n=15ä¸ï¼é¸ç¨`ãæ¯ä¸bitãç¿»è½` (åä¸)

<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HC2.jpg" width="auto" height="400" />

`åä¸`


<img src="https://github.com/lanac0911/deepLearning/blob/main/imgs/HC2-2.jpg" width="auto" height="400" />

`åäº`


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
2. **Hill Climbæ¼ç®æ³**
    * **åå§å**
        * random"åæ³"çåå§å¼/è§£
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

    * **å®ç¾©Neighborsé°å±**
        * æ¯åé²è¡**ç¿»è½**(0â1,1â0)    
        * è¥**åæ³**(ééwç¬¦å)ï¼ä¸**æ´ä½³**(å¹å¼vå¤§æ¼åä¾ç)ï¼å**åä»£**åå§è§£ï¼æçºæ°çåå§è§£(æ«æè§£)
         ```python

            def HillClimbing():
                temp_state = now_state.copy() #åå¾åå§è§£
                for index, pick in enumerate(now_state['blist']): #éæ­·æ¯åä½å
                    new_list = now_state['blist'].copy()
                    new_list[i] = int(not new_list[i])
                    (w, v) = calTotalWandV(new_list)
                    if w <= varibles.capcity: #åæ³
                        if v > temp_v: #æ°better than è
                            ......(åä»£)  
                #åä»£åå§è§£,æçºæ°çåå§è§£(æ«æè§£)
                NewState(temp_state['blist'], temp_state['weight'], temp_v)   
        ```
        
### â» åèè³æ
 1. [PDFæå­¸æª](https://athena.ecs.csus.edu/~gordonvs/215/WeeklyNotes/03A_hillClimbingSimulatedAnnealing.pdf)
