from math import ceil
from random import randint,choice
from numpy import random as npRandom

class Puzzle():
    def __init__(self,rows,cols,wordList,invExist=False,mixCase=False) -> None:
        self.grid = [['.' for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        self.wordList = wordList
        self.temp_mistakes = []
        self.remakeCount = 0
        self.invExist = invExist
        self.mixCase = mixCase
        self.wSort(self.wordList)
        
        self.attempt_placing()
        #self.fill_empty()
        if self.mixCase == True:
            self.mixCasing()
        
    def mixCasing(self):
        for lis in range(self.rows):
            for j in range(self.cols):
                mixCh = choice([0,1])
                if mixCh == 1:
                    self.grid[lis][j] = self.grid[lis][j].upper()
                else:
                    self.grid[lis][j] = self.grid[lis][j].lower()

    def fill_empty(self):
        for lis in range(self.rows):
            for j in range(self.cols):
                if self.grid[lis][j] == '.':
                    self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                else:
                    continue

    def attempt_placing(self):
        for word in self.wordList:
            self.word_place(word,self.rows,self.cols)
        
        if self.temp_mistakes.copy() != []:
            print("2nd attempt for mistakes : ",self.temp_mistakes)
            for word in self.temp_mistakes:
                if self.second_spot(word,self.rows,self.cols):
                    self.temp_mistakes.remove(word)
        else:
            print("No mistakes")
            
        if len(self.temp_mistakes) !=0 :
            if self.remakeCount < 6: 
                print(f"Remaking {self.remakeCount} times")  
                self.grid = [['.' for i in range(cols)] for i in range(rows)]
                self.temp_mistakes.clear()
                self.remakeCount +=1
                self.attempt_placing()
            else:
                print("Failed to place words : ",self.temp_mistakes)
        else:
            print("Placing successfull")

    def wSort(self,lis):
        for i in range(0,len(lis)):
            for j in range(0,len(lis)-1-i):
                if len(lis[j])<len(lis[j+1]):
                    lis[j],lis[j+1]=lis[j+1],lis[j]

    def getMaxWordLength(self,wlis):
        return len(wlis[0])

    def getSumLength(self,wlis):
        s=0
        for w in wlis:
            s+= len(w)
        return s
    
    def word_place(self,word,nno,wno):
        info = self.find_spot(word,nno,wno)
        if info != None :
            wlIndex,nlIndex,orientation,inv = info
            if inv == 1:
                word = word[::-1]
            if orientation == "h":
                self.place_horizontal(word,nlIndex,wlIndex)
            elif orientation == "v" : 
                self.place_vertical(word,nlIndex,wlIndex)
            elif orientation == "md" : 
                self.place_Mdiagonal(word,nlIndex,wlIndex)
            elif orientation == "sd":
                self.place_Sdiagonal(word,nlIndex,wlIndex)
#needs more work
    def second_spot(self,word,nno,wno):
        lenght = len(word)
        for i in range(0,wno-lenght):
            if self.check_empty("h",word,0,i,0):
                self.place_horizontal(word,0,i,0)
                print(f"placed {word} at 'h',0,{i},0")
                return True
            elif self.check_empty("h",word,0,i,1):
                self.place_horizontal(word,0,i,1)
                print(f"placed {word} at 'h',0,{i},1")
                return True
            elif self.check_empty("h",word,nno-1,i,0):
                self.place_horizontal(word,nno-1,i,0)
                print(f"placed {word} at 'h',{nno-1},{i},0")
                return True
            elif self.check_empty("h",word,nno-1,i,1):
                self.place_horizontal(word,nno-1,i,1)
                print(f"placed {word} at 'h',{nno-1},{i},1")
                return True
        else:        
            for i in range(0,nno-lenght):
                if self.check_empty("v",word,i,wno-1,0):
                    self.place_vertical(word,i,wno-1,0)
                    print(f"placed {word} at 'v',{i},{wno-1},0")
                    return True
                elif self.check_empty("v",word,i,wno-1,1):
                    self.place_vertical(word,i,wno-1,1)
                    print(f"placed {word} at 'v',{i},{wno-1},1")
                    return True
                elif self.check_empty("v",word,i,0,0):
                    self.place_vertical(word,i,0,0)
                    print(f"placed {word} at 'v',{i},0,0")
                    return True
                elif self.check_empty("v",word,i,0,1):
                    self.place_vertical(word,i,0,1)
                    print(f"placed {word} at 'v',{i},0,1")
                    return True

    def check_empty(self,orient,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        if orient=="h":
            for i in range(lenght):
                if self.grid[nlIndex][wlIndex+i] not in ['.',word[i]] : 
                    return False
            else:
                return True
        elif orient=="v":
            for i in range(lenght):
                if self.grid[nlIndex+i][wlIndex] not in ['.',word[i]] : 
                    return False
            else:
                return True
        elif orient=="md":
                for i in range(lenght):
                    if self.grid[nlIndex+i][wlIndex+i] not in ['.',word[i]] : 
                        return False
                else:
                    return True
        elif orient=="sd":
                for i in range(lenght):
                    if self.grid[nlIndex+i][wlIndex-i] not in ['.',word[i]] : 
                        return False
                else:
                    return True
                
    def place_horizontal(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            self.grid[nlIndex][wlIndex+i] = word[i]

    def place_vertical(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            self.grid[nlIndex+i][wlIndex] = word[i]

    def place_Mdiagonal(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            self.grid[nlIndex+i][wlIndex+i] = word[i]

    def place_Sdiagonal(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            self.grid[nlIndex+i][wlIndex-i] = word[i]

    def default_gen(self,orient,nno,wno,lenght):
        wlIndex,nlIndex = 0,0
        if orient == "h" : 
            wlIndex = randint(0,wno-1-lenght)
            nlIndex = randint(0,nno-1)
        elif orient == "v" : 
            nlIndex = randint(0,nno-1-lenght)
            wlIndex = randint(0,wno-1)    
        elif orient == "md" : 
            wlIndex = randint(0,wno-1-lenght)
            nlIndex = randint(0,nno-1-lenght) 
        elif orient == "sd":
            wlIndex = randint(lenght-1,wno-1)
            nlIndex = randint(0,nno-1-lenght)
        return wlIndex,nlIndex
     
    def find_spot(self,word,nno,wno):
        lenght = len(word)
        orientation = choice(["h","v","md","sd"])
        inv = 0 
        if self.invExist == True:
            inv = npRandom.choice((0,1),p=[0.7,0.3])
        nlIndex,wlIndex = 0,0
        errors = 0
        wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            
        while True:
            if errors >0 and errors <5:
                if orientation == "h" : 
                    wlIndex = randint(0,wno-1-lenght)
                if orientation == "v" : 
                    nlIndex = randint(0,nno-1-lenght)
                if orientation == "md" : 
                    wlIndex = randint(0,wno-1-lenght)
                    nlIndex = randint(0,nno-1-lenght) 
                if orientation == "sd":
                    wlIndex = randint(lenght-1,wno-1)
                    nlIndex = randint(0,nno-1-lenght)     
            elif errors >=5 and errors < 10 :
                if orientation == "h" : 
                    nlIndex = randint(0,nno-1-lenght)
                if orientation == "v" : 
                    wlIndex = randint(0,wno-1-lenght)
                if orientation == "md" : 
                    wlIndex = randint(0,wno-1-lenght)
                    nlIndex = randint(0,nno-1-lenght)
                if orientation == "sd":
                    wlIndex = randint(lenght-1,wno-1)
                    nlIndex = randint(0,nno-1-lenght)
            elif errors >=10 and errors<25:
                wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            elif errors >=25 and errors<100:
                orientation = choice(["h","v","md","sd"])
                wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            elif errors >=100:
                self.temp_mistakes.append(word)        
                break 

            if self.check_empty(orientation,word,nlIndex,wlIndex,inv) == True: 
                errors=0
                return wlIndex,nlIndex,orientation,inv
            elif self.check_empty(orientation,word,nlIndex,wlIndex,(inv+1)%2) == True:
                errors=0
                return wlIndex,nlIndex,orientation,(inv+1)%2
            else:
                errors+=1

    def print_puzzle(self):
        for line in self.grid:
            for i in line:
                print(i,end='  ')
            print()


#Generating the test case
#Minimum size for this test list is 14x14 (70%)
rows,cols = 14,14
wordList = ["APPLE","SOYSAUCE","SPINACH","BREAD","COUPLE","AIR","HONDA","PAPAYA","BEDSHEETS","ORANGE","MOTORBIKE","YATCH","PINEAPPLE","GOAT","DOG","PINATA","AVOCADO","GRAPES","DRINKING","WALKING","AMAZING","PIZZA","COCONUT","POTATOES"]
p = Puzzle(rows,cols,wordList,invExist=False,mixCase=False)
print("\n\n")
p.print_puzzle()
print("\nFind the words : ")
print(wordList)
