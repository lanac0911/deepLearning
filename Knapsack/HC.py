import compoents
import varibles

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


#------------------------------------
def HillClimb() :
    i = 0
    #random合法初始值
    (initSol, inti_w, init_v) = compoents.initialState()
    # print("inti_w",inti_w)
    # print("init_v",init_v)
    # print("-----------------------")
    while i < 500:
        (stage, flag) = compoents.HillClimbing() #初始值pair
        print("遞迴",i, stage)
        if not flag: break
        i += 1
        


def main():
    #initialize
    varibles.varibles()
    loadData()
    HillClimb()

main()


# print("capcity", capcity)
# print("weights", weights)
# print("values", values)