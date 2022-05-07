import random 
rubyList1 = []
for i in range(5):
    rubyList1.append(random.randint(0,9))

while True: 
    if rubyList1[0] == rubyList1[1] or rubyList1[0] == rubyList1[2] or rubyList1[0] == rubyList1[3] or rubyList1[0] == rubyList1[4] or rubyList1[1] == rubyList1[2] or rubyList1[1] == rubyList1[3] or rubyList1[1] == rubyList1[4] or rubyList1[2] == rubyList1[3] or rubyList1[2] == rubyList1[4] or rubyList1[3] == rubyList1[4]:
        rubyList1 = []
        for i in range(5):
            rubyList1.append(random.randint(0,9))
    else:
        print(rubyList1)
        break

running = True

runs = 0
numRuns = 1

while running:    
    command = input("Pleasee enter your command #" + str(numRuns) + ":")
    
    space = command.find(" ")
    
    countSpace = command.count(" ")
    placeNum = command[:space]
    placeLR = command[space + 1:]
    
    placeRight = command[space + 1:]
    placeLeft = command[space + 1:]
    
    
    findRight = command.find("right")
    findLeft = command.find("left")
    
    if countSpace == 1 and placeLR.isalpha() == True and placeNum.isdigit() == True:
        if placeLR == "right" or placeLR == "left":
            if placeLR == "right": 
                di = 0
                while rubyList1[di] != int(placeNum):
                    di += 1
                moveList = rubyList1[di]
                if di != 4:
                    movedList = rubyList1[di + 1]
                    rubyList1[di] = movedList
                    rubyList1[di + 1] = moveList
                else:
                    ruby0 = rubyList1[0]
                    ruby1 = rubyList1[1]
                    ruby2 = rubyList1[2]
                    ruby3 = rubyList1[3]
                    last = rubyList1.pop()
                    rubyList1[0] = last
                    rubyList1[1] = ruby0
                    rubyList1[2] = ruby1
                    rubyList1[3] = ruby2
                    rubyList1.append(ruby3)
                print(rubyList1)
                if rubyList1[0] > rubyList1[1] or rubyList1[0] > rubyList1[2] or rubyList1[0] >rubyList1[3] or rubyList1[0] > rubyList1[4] or rubyList1[1] > rubyList1[2] or rubyList1[1] > rubyList1[3] or rubyList1[1] > rubyList1[4] or rubyList1[2] > rubyList1[3] or rubyList1[2] > rubyList1[4] or rubyList1[3] > rubyList1[4]:
                    runs += 1
                    numRuns += 1
                else: 
                    print("You win. ")
                    break
                if runs > 9:
                    print("You lose. ")
                    break
            elif placeLR == "left":
                di = 0
                while rubyList1[di] != int(placeNum):
                    di += 1
                moveList = rubyList1[di]
                if di != 0:
                    movedList = rubyList1[di - 1]
                    rubyList1[di] = movedList
                    rubyList1[di - 1] = moveList
                else:
                    ruby0 = rubyList1[0]
                    rubyList1.remove(rubyList1[0])
                    rubyList1.append(ruby0)
                print(rubyList1)  
                if rubyList1[0] > rubyList1[1] or rubyList1[0] > rubyList1[2] or rubyList1[0] >rubyList1[3] or rubyList1[0] > rubyList1[4] or rubyList1[1] > rubyList1[2] or rubyList1[1] > rubyList1[3] or rubyList1[1] > rubyList1[4] or rubyList1[2] > rubyList1[3] or rubyList1[2] > rubyList1[4] or rubyList1[3] > rubyList1[4]:
                    runs += 1  
                    numRuns += 1
                else: 
                    print("You win. ")   
                    break
                if runs > 10:
                    print("You lose. ")  
                    break
        else:
            print("You need a direction. ")
    else: 
        print("You need a correct format. ")
