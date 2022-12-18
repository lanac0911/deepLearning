import random
import varibles
import math

now_state = { 'blist':[], 'weight':0, 'value':0 } # Now：「現在」的狀態
best_state = { 'blist':[], 'weight':0, 'value':0 } # (for SA) Best：「全域最佳」的狀態

#---------更新Now狀態---------
def UpdateNowState(blist, w, v):
    now_state['blist'] = blist
    now_state['weight'] = w
    now_state['value']= v

#---------Random"合法"初始狀態(解)----------
def initialState():
    global best_state
    pickBound = math.pow(2, int(varibles.objNums)) #upperbound: 2^15
    inti_w = 0; init_v = 0
    while(1):
        initNum = format(random.randrange(int(pickBound/2) , pickBound), 'b') #範圍: (2^15/2) - 2^15
        blist = binToList(initNum) #拆成list
        (w, v) = calTotalWandV(blist)  #計算weight & value
        
        if w <= varibles.capcity: #是否合法
            inti_w = w
            init_v = v
            break
    print("初始解",blist)
    UpdateNowState(blist, inti_w, init_v) #存入Now狀態
    best_state = now_state.copy() #(SA)初始先設為Best

    return (initNum, inti_w, init_v) #回傳"合法"二進位數

#---------binary數拆成List---------
def binToList(bin):
    len_pick = len(bin)
    len_total = varibles.objNums

    blist = [int(i) for i in list(format(bin))] #binary拆開to List
    blist += [0] * (len_total - len_pick) #補0
    return blist

#----------計算weight和value----------
def calTotalWandV(blist):
    tempWeight = 0
    tempValue = 0
    for i in enumerate(blist):
        if(i[1] == 1):
            tempValue += varibles.values[i[0]]
            tempWeight += varibles.weights[i[0]]
    # print("總重:",tempWeight)
    # print("總價值:",tempValue)
    return(tempWeight, tempValue)


#----------找鄰居的方法(HC)----------
def delOrAdd_HeavyOrLight(list, mode):
    # mode=0做增加 , mode=1做刪減
    hasNeig = False; d = dict()
    indices = [i for i, x in enumerate(list) if x == mode]
    if(len(indices) >= 1): #刪一個輕的
        idx = random.choice(indices) #隨機挑一個1
        list[idx] = int(not mode)#刪
        hasNeig = True
    d['flag'] = hasNeig 
    d['new_oper_list'] = list 
    return d



#>>>>>>>>>>> HILL CLIMBL <<<<<<<<<<
def HillClimbing():
    # for index, pick in enumerate(now_state['blist']): #遍歷每個位元
    # for i in range(0,varibles.objNums-1 ,1): #遍歷每兩位元
    new_list = now_state['blist'].copy()
    now_v = now_state['value']
    front = int(varibles.objNums / 2); 
    front_list = new_list[:front] #前半
    end_list = new_list[front:] #後半
    flag1 = False; flag2 = False #加/減有無找到鄰居

   # 找鄰居：
   #    將binary數分成前半、後半(權重輕、權重重)(已由小 → 大排序))
   #    〔加一個，減一個〕操作都要從【前半、後半】中選一個(每次由隨機機率決定)
   #    若剛好前半、後半都無法再加減
   #    則隨機取一位元做翻轉

    doAdd = random.random() #前半、後半誰要做加
    doDel = random.random() #前半、後半誰要做減
    #加------
    if doAdd > 0.5: #重的+1
        res = delOrAdd_HeavyOrLight(end_list, 0)  #add Heavy
        end_list = res['new_oper_list']
        flag1 = res['flag']
    else: #輕的+1
        res = delOrAdd_HeavyOrLight(front_list, 0) #add Light
        front_list = res['new_oper_list']
        flag1 = res['flag']
    #減-------
    if doDel > 0.5: #重的-1
        res = delOrAdd_HeavyOrLight(end_list, 1) #del Heavy
        end_list = res['new_oper_list']
        flag2 = res['flag']
    else: #輕的-1
        res = delOrAdd_HeavyOrLight(front_list, 1) #del Light
        front_list = res['new_oper_list']
        flag2 = res['flag']
    new_list = front_list + end_list
    #都失敗-----
    if (flag1 or flag2) == 0: #隨機翻轉一位元
        idx = random.randrange(0, varibles.objNums)
        new_list[new_list] = (not new_list[idx])

    (w, v) = calTotalWandV(new_list)
    if w <= varibles.capcity: #合法
        if v > now_v: #新better than 舊 => 交換
            UpdateNowState(new_list, w, v)  
    
    return (now_state)


#>>>>>>>>>>> Simulation Annealing <<<<<<<<<<
def SimulationAnnealing():
    T0 = 180 #初始溫度 (影響解的搜索範圍)
    TF = 1 #臨界溫度
    RATIO = 0.9 #收斂速度 (過快較可能找不到最佳解)
    t = T0

    while t >= TF:
        for index, pick in enumerate(now_state['blist']): #遍歷每個位元
            (now_w, now_v) = calTotalWandV(now_state['blist'])
            #生成 neighbors(test)
            test_list = now_state['blist'].copy()
            test_list[index] = int(not pick)
            (test_w, test_v) = calTotalWandV(test_list)
            #best更新
            if test_w > varibles.capcity: continue #非法，跳過
            if test_w <= varibles.capcity: #合法
                if test_v > best_state['value']: #新better than 舊
                    best_state['blist'] = test_list
                    best_state['weight'] = test_w
                    best_state['value'] = test_v
            #now更新
            if test_v > now_v : #優於當前解 -> 更新
                UpdateNowState(test_list, test_w, test_v)
            else: #由機率判斷
                proba = float(test_v - now_v) / t
                if(random.random() < math.exp(proba)):
                    UpdateNowState(test_list, test_w, test_v)
        t *= RATIO 
    return (best_state)
