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
    pickBound = math.pow(2, int(varibles.objNums)) #15個先取一半
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

#----------15個neig找best
def HillClimbing():
    temp_state = now_state.copy()
    temp_v = now_state['value']
    print("****",now_state)
    #Find neighbors *15
    for i in range(0,varibles.objNums-1 , 2):
        new_list = now_state['blist'].copy()
        new_list[i] = int(not new_list[i])
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
                
                print("replace---------")

    NewState(temp_state['blist'], temp_state['weight'], temp_v)  
    return (now_state)





##----------15個neig找best
# def HillClimbing():
#     flag = False
#     temp_state = now_state.copy()
#     temp_v = now_state['value']
#     print("****",now_state)
#     #Find neighbors *15
#     for index, pick in enumerate(now_state['blist']):
#         new_list = now_state['blist'].copy()
#         idx = varibles.objNums #15
#         new_list[index] = int(not pick)
#         (w, v) = calTotalWandV(new_list)
#         print("新的:")
#         print("w:",w)
#         print("v:",v)
#         print("-v----------------------")
#         if w <= varibles.capcity: #合法
#             if v > temp_v: #新better than 舊
#                 # flag = True
#                 temp_state['blist'] = new_list
#                 temp_state['weight'] = w
#                 temp_v = v
#                 # print("合法情況",temp_state)
#                 # print("原始情況",now_state)
                
#                 print("replace---------")

#     NewState(temp_state['blist'], temp_state['weight'], temp_v)  
#     return (now_state)


