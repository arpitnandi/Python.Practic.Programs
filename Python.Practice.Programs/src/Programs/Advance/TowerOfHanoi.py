import pyautogui


class TowerOfHanoi:
    
    global Status
    global flag
    global i
    global Lavel
    global Chances
     
    global Tower
    global Tower_1
    global Tower_2
    global Tower_3
    
    Status="new game"
    flag=False
    
    Tower=[]
    Tower_1=[]
    Tower_2=[]
    Tower_3=[]
    
    
    def game(self, Status):
        global Lavel
        global Tower
        global Tower_1
        global Tower_2
        global Tower_3
        if Status=="new game":
            Lavel=int(input("Select the level of difficulty:\n"))
        if Status=="retry" or Status=="lavel up":
            for i in range(Lavel):
                if len(Tower_1)!=0:
                    Tower_1.pop()
                if len(Tower_2)!=0:
                    Tower_2.pop()
                if len(Tower_3)!=0:
                    Tower_3.pop()
            if Status=="lavel up":
                Lavel+=1
                global Chances
                Chances=Lavel*Lavel
        for i in range(Lavel):
            Tower.append(Lavel-i)
        Tower_1=Tower
        self.printBackground(Lavel,Tower_1,Tower_2,Tower_3)
        Status="continue"
       
        
    def printBackground(self, Lavel,T_1,T_2,T_3):
        Width=(Lavel*2-1)+2
        Height=Lavel+3
        print()
        H=Height
        while H>0:
            print("||",end='')
            W=Width*3
            while W>0:
                if H==Height-1 and (W<=Width*3 or W>=1):
                    print("  ",end='')
                elif (H==Height or H==1) and (W<=Width*3 or W>=1):
                    print("==",end='')
                elif (H<Height-1 or H>1) and (W<=Width*3 or W>=1):
                    if H-1<=len(T_1):
                        self.printDisk(T_1[H-2], Lavel)
                    elif H-1>len(T_1):
                        i=Width
                        while i>0:
                            print("  ",end='')
                            i-=1
                    if H-1<=len(T_2):
                        self.printDisk(T_2[H-2], Lavel)
                    elif H-1>len(T_2):
                        i=Width
                        while i>0:
                            print("  ",end='')
                            i-=1
                    if H-1<=len(T_3):
                        self.printDisk(T_3[H-2], Lavel)
                    elif H-1>len(T_3):
                        i=Width
                        while i>0:
                            print("  ",end='')
                            i-=1
                    break
                W-=1
            print("||")
            H-=1
        print()
        
    def printDisk(self, Order, Lavel):
        if Order>0:
            self.printPatern(Lavel-Order+1, "  ")
            self.printPatern(Order*2-1, "[]")
            self.printPatern(Lavel-Order+1, "  ")
            
        
    def printPatern(self, Width, Patern):
        while Width>0:
            print(Patern,end='')
            Width-=1
    
        
    def moveDisk(self, Action):
        global Tower_1
        global Tower_2
        global Tower_3
        global Status
        if Action=="12" or Action=="21" or Action=="13" or Action=="31" or Action=="23" or Action=="32":
            try:
                global Chances
                if Action=="12":
                    if len(Tower_2)==0:
                        Tower_2.append(Tower_1.pop())
                        Chances-=1
                    if Tower_2[len(Tower_2)-1]>Tower_1[len(Tower_1)-1]:
                        Tower_2.append(Tower_1.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
                elif Action=="21":
                    if len(Tower_1)==0:
                        Tower_1.append(Tower_2.pop())
                        Chances-=1
                    elif Tower_1[len(Tower_1)-1]>Tower_2[len(Tower_2)-1]:
                        Tower_1.append(Tower_2.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
                elif Action=="13":
                    if len(Tower_3)==0:
                        Tower_3.append(Tower_1.pop())
                        Chances-=1
                    elif Tower_3[len(Tower_3)-1]>Tower_1[len(Tower_1)-1]:
                        Tower_3.append(Tower_1.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
                elif Action=="31":
                    if len(Tower_1)==0:
                        Tower_1.append(Tower_3.pop())
                        Chances-=1
                    elif Tower_1[len(Tower_1)-1]>Tower_3[len(Tower_3)-1]:
                        Tower_1.append(Tower_3.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
                elif Action=="23":
                    if len(Tower_3)==0:
                        Tower_3.append(Tower_2.pop())
                        Chances-=1
                    elif Tower_3[len(Tower_3)-1]>Tower_2[len(Tower_2)-1]:
                        Tower_3.append(Tower_2.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
                elif Action=="32":
                    if len(Tower_2)==0:
                        Tower_2.append(Tower_3.pop())
                        Chances-=1
                    elif Tower_2[len(Tower_2)-1]>Tower_3[len(Tower_3)-1]:
                        Tower_2.append(Tower_3.pop())
                        Chances-=1
                    else:
                        print("[ WARNNING : ***The top most disk must be the smallest at a time*** ]")
            except:
                pass
            self.printBackground(Lavel,Tower_1,Tower_2,Tower_3)
        elif Action=="exit":
            Status="exit"
        else:
            print("\n***",Action," is an Invalid Move***\n[ Type ('12'/'21'/'31'/'13'/'23'/'32' as your move) Or ('exit' if you want to end the game) ]")
    
        
    def gameOver(self):
        print("\n***Game Over***")
        self.endGame()
        
    def checkVictory(self, Tower, Chances):
        for i in range(Lavel):
            global flag
            if len(Tower)==Lavel and Tower[Lavel-1]==i+1 and Tower[i]==Lavel:
                flag=True
                Status="victory"
                break
            elif len(Tower)==0:
                flag=False
                break
        if flag and Chances>0:
            print("\n***You Win the game***")
            self.lavelUp()
        if flag==False and Chances==0:
            self.gameOver()
    
        
    def lavelUp(self):
        global flag
        global Status
        S=input("\n***Do you wanna continue***\n");
        if S=="yes":
            Status="lavel up"
            flag=False
            self.game(Status)
        elif S=="no":
            Status="exit"
    
        
    def endGame(self):
        global Status
        S=input("\n***Do you wanna try again?***\n");
        if S=="yes":
            Status="retry"
        elif S=="no":
            Status="exit"
        else:
            print("\n***Please answer either: [yes]/[no]***")
            self.endGame()
            
        
    def cleareConsole(self):
        R = pyautogui
        R.keyDown("Shift")
        R.keyDown("F10")
        R.press("R")
        R.keyUp("F10")
        R.keyUp("Shift")

        
T=TowerOfHanoi()
 
T.game(Status)
while Status!="exit":
    if Status=="retry" or Status=="lavel up":     
        T.game(Status)
    Chances=Lavel*Lavel
    while Chances>0 and flag==False:
        if Chances<=3 and Chances!=1:
            print("\n",Chances," chances left")
        if Chances==1:
            print("\nLast chance")
        T.checkVictory(Tower_2, Chances);
        if Status!="exit":
            T.moveDisk(input("\n"))
        elif Status=="exit":
            break
    if flag==False and Status!="exit":
        T.gameOver()
    if Status=="exit":
        print("\n***Exiting Game***")
T.cleareConsole()