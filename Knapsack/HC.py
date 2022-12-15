import compoents
import varibles
import matplotlib.pyplot as plt

paths = ['p07_c.txt', 'p07_w.txt', 'p07_p.txt']
iterationNums = 10 #遞迴次數
initialState = 0 #初始解

#---------讀取TXT資料進入list----------            
def loadDataLoop (src) :
    list = []
    for line in src.readlines():
        line = line.strip('\n')
        list.append(int(line))
    return list

def loadData():
    for path in paths:
        f = open(path, 'r')
        if path == 'p07_c.txt' :
            varibles.capcity = int(f.read())
        elif path == 'p07_w.txt':
            varibles.weights = loadDataLoop(f)
        else:
            varibles.values = loadDataLoop(f)

        f.close()


data = []
#------------------------------------
def HillClimb() :
    i = 0
    #random合法初始值
    compoents.initialState() #初始值/解
    # print("inti_w",inti_w)
    # print("init_v",init_v)
    # print("-----------------------")
    while i < varibles.iteraNum:
        (stage) = compoents.HillClimbing() #初始值pair
        print("遞迴",i+1, stage)
        data.append(stage['value'])
        # if not flag: break
        i += 1
    print("vali",varibles.values)
    print("weights",varibles.weights)




def main():
    #initialize
    varibles.varibles()
    loadData()
    HillClimb()
    plt.figure()
    plt.ylabel('values')
    plt.xlabel('times')
    plt.plot(data)        
    plt.ylim(1200,1500)
    plt.show()

main()


# print("capcity", capcity)
# print("weights", weights)
# print("values", values)