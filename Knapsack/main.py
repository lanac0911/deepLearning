import compoents
import varibles
import matplotlib.pyplot as plt

paths = ['p07_c.txt', 'p07_w.txt', 'p07_p.txt']

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
        if path == paths[0] :
            varibles.capcity = int(f.read())
            # varibles.capcity = int(varibles.capcity / 2)
        elif path == paths[1]:
            varibles.weights = loadDataLoop(f)
        else:
            varibles.values = loadDataLoop(f)

        f.close()


history = []
#------------------------------------
def HillClimb() :
    i = 0
    compoents.initialState() #初始值/解
    while i < varibles.iteraNum:
        (stage) = compoents.HillClimbing() #初始值
        history.append(stage['value'])
        i += 1
    return stage

def SA() :
    i = 0
    compoents.initialState() #初始值/解
    while i < varibles.iteraNum:
        (stage) = compoents.SimulationAnnealing() #初始值
        history.append(stage['value'])
        i += 1
    return stage


if __name__ == '__main__':
  #initialize
    varibles.varibles()
    loadData()
    choice = 0
    ans = {}
    while(1):
        inputn = input("\n――――選擇模式 ―――― \n 1：Hill Climbing       ｜\n 2：Simulation Annealing｜ \n―――――――――――――\n")
        choice = inputn
        if(choice == "1"): ans = HillClimb(); break
        elif(choice == "2"): ans = SA(); break
        else: print("錯誤，請重新輸入")
 #print結果
    print("\n=========================================\n")
    print('* Objects數：{:>4}'.format(f' {int(varibles.objNums)}'))
    print('* 迭代次數：{:>4}'.format(f'{varibles.iteraNum}'))
    print(f"* Objects Weight： {varibles.weights}")
    print(f"* Objects Value： {varibles.values}")
    print("------------------------------------------\n")
    print(f"* 結果：\n value：{ans['value']}\n weight：{ans['weight']}\n pick：{ans['blist']}")
    print("=========================================\n")
  #畫圖 40-60  1458
    # yrange = (min(history),)
    plt.figure()
    plt.ylabel('values')
    plt.xlabel('times')
    plt.plot(history)        
    # plt.ylim(yrange)
    plt.show()

