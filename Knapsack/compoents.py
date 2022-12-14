import random
import varibles
import math

now_state = { 'blist':[], 'weight':0, 'value':0 }

def NewState(blist, w, v):
    now_state['blist'] = blist
    now_state['weight'] = w
    now_state['value']= v

#---------Random"合法"初始狀態(解)----------
def initialState():
    pickBound = math.pow(2, int(varibles.objNums/2)) #15個先取一半
    initNum = 0
    inti_w = init_v = 0
    while(1):
        initNum = format(random.randrange(1, pickBound), 'b')
        blist = binToList(initNum)
        (w, v) = calTotalWandV(blist)    
        
        if w <= varibles.capcity: 
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
    # print("進來的2進位=",bin)
    tempWeight = 0
    tempValue = 0
    for i in enumerate(blist):
        if(i[1] == 1):
            tempValue += varibles.values[i[0]]
            tempWeight += varibles.weights[i[0]]
    # print("總重:",tempWeight)
    # print("總價值:",tempValue)
    return(tempWeight, tempValue)
    

def HillClimbing():
    flag = False
    temp_state = now_state.copy()
    print("****",now_state)
    #Find neighbors *15
    for index, pick in enumerate(now_state['blist']):
        new_list = now_state['blist'].copy()
        new_list[index] = int(not pick)
        (w, v) = calTotalWandV(new_list)
        print("新的:")
        print("new_list:",new_list)
        print("w:",w)
        print("v:",v)
        print("-v----------------------")
        if w <= varibles.capcity: #合法
            if v > temp_state['value']: #新better than 舊
                flag = True
                temp_state['blist'] = new_list
                temp_state['weight'] = w
                temp_state['value'] = v
                print("合法情況",temp_state)
                print("原始情況",now_state)
                print("-----------------------")

    NewState(temp_state['blist'], temp_state['weight'], temp_state['value'])  
    return (now_state, flag)


