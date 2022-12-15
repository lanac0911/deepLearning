import random
import varibles
import math

now_state = { 'blist':[], 'weight':0, 'value':0 }
best_state = { 'blist':[], 'weight':0, 'value':0 }
def NewState(blist, w, v):
    now_state['blist'] = blist
    now_state['weight'] = w
    now_state['value']= v
#>>>>>>>>>>>>>>>>>Hill Climbing<<<<<<<<<<<<<<<<<
#---------Random"合法"初始狀態(解)----------
def initialState():
    pickBound = math.pow(2, int(varibles.objNums/2)) #upperbound: 2^15
    inti_w = init_v = 0
    while(1):
        initNum = format(random.randrange(1, pickBound), 'b') #範圍: 1 - 2^15
        blist = binToList(initNum) #拆成list
        (w, v) = calTotalWandV(blist)  #計算weight & value
        
        if w <= varibles.capcity: #是否合法
            inti_w = w
            init_v = v
            break
    NewState(blist, inti_w, init_v)
    return (initNum, inti_w, init_v) #回傳"合法"二進位數

def binToList(bin):
    len_pick = len(bin)
    len_total = varibles.objNums

    blist = [int(i) for i in list(format(bin))] #binary拆開to List
    blist += [0] * (len_total - len_pick) #補0
    return blist

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


#----------15個neig找best
def HillClimbing():
    temp_state = now_state.copy()
    temp_v = now_state['value']
    print("****",now_state)
    #Find neighbors *15
    for index, pick in enumerate(now_state['blist']):
        new_list = now_state['blist'].copy()
        new_list[index] = int(not pick)
        (w, v) = calTotalWandV(new_list)
        print("新的:",new_list)
        print("w:",w)
        print("v:",v)
        print("-v----------------------")
        if w <= varibles.capcity: #合法
            if v > temp_v: #新better than 舊
                temp_state['blist'] = new_list
                temp_state['weight'] = w
                temp_v = v
                # print("合法情況",temp_state)
                # print("原始情況",now_state)
                
                print("replace********")

    NewState(temp_state['blist'], temp_state['weight'], temp_v)  
    return (now_state)

#>>>>>>>>>>>>>>>>>Simulation Annealing<<<<<<<<<<<<<<<<<
def SimulationAnnealing():
    T0 = 100
    TF = 1
    RATIO = 0.9
    now_val = 0
    print("nori_state", now_state)
    best_state = now_state.copy()
    
    t = T0
    while t >= TF:
        # for index, pick in enumerate(now_state['blist']):
        for i in range(0, varibles.objNums, 1): 
            new_list = now_state['blist'].copy()
            new_list[i] = int(not new_list[i])
            (w, v) = calTotalWandV(new_list)
            # print("新的:",new_list)
            print("new_list", new_list, "w:",w, "v:",v)
            print("best_state:",best_state)
            print("now_state:",now_state)
            #best.
            if w > varibles.capcity: print("wjump"); continue #非法，跳過
            if w <= varibles.capcity: #合法
                if v > best_state['value']: #新better than 舊
                    print("***更新BEST")
                    best_state['blist'] = new_list
                    best_state['weight'] = w
                    best_state['value'] = v
                    flag = True    
            #temp
            if v > now_state['value'] : #優於當前解 -> 更新
                print("***直接更新")
                NewState(new_list, w, v)
            else: #由機率判斷
                dx = (v - now_state['value']) / T0
                # print("dx",dx)
                if(random.random() < math.exp(dx)):
                    print("***機率更新")
                    NewState(new_list, w, v)
        t *= RATIO
        print("-----------------------")

        print

    # return (now_state)
    return (best_state)
