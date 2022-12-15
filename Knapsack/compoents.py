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
    inti_w = init_v = 0
    while(1):
        initNum = format(random.randrange(int(pickBound/2) , pickBound), 'b') #範圍: 1 - 2^15
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


#>>>>>>>>>>> HILL CLIMBL <<<<<<<<<<
def HillClimbing():
    test_state = now_state.copy()
    now_v = now_state['value']
    #生成 neighbors *15 (翻轉每兩位元)
    for index, pick in enumerate(now_state['blist']): #遍歷每個位元
    # for i in range(0,varibles.objNums-1 ,1): #遍歷每兩位元
        new_list = now_state['blist'].copy()
        new_list[index] = int(not pick )
        (w, v) = calTotalWandV(new_list)
        if w <= varibles.capcity: #合法
            if v > now_v: #新better than 舊 => 交換
                test_state['blist'] = new_list
                test_state['weight'] = w
                now_v = v

    UpdateNowState(test_state['blist'], test_state['weight'], now_v)  
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
                    flag = True    
            #now更新
            if test_v > now_v : #優於當前解 -> 更新
                UpdateNowState(test_list, test_w, test_v)
            else: #由機率判斷
                proba = float(test_v - now_v) / t
                if(random.random() < math.exp(proba)):
                    UpdateNowState(test_list, test_w, test_v)
        t *= RATIO 
    return (best_state)
