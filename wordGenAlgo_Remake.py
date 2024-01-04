from math import ceil
from random import randint,choice
from numpy import random
class Puzzle():
    def __init__(self,rows,cols,wordList) -> None:
        self.grid = [['.' for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        self.wordList = wordList
        self.temp_mistakes = []
        
        self.wSort(self.wordList)
        self.overlap_count = ceil(1.5*(len(self.wordList)/self.getMaxWordLength(self.wordList)/rows/cols*self.getSumLength(self.wordList)))
        print("Overlap count : ",self.overlap_count)

        for word in self.wordList:
            self.word_place(word,self.rows,self.cols)
        print("Mistakes : ",self.temp_mistakes)

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
            elif orientation == "d" : 
                self.place_diagonal(word,nlIndex,wlIndex)
        else:
            print(f"{word} gave error !!")
            self.temp_mistakes.append(word)

    def check_empty(self,orient,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        if orient=="h":
            for i in range(lenght):
                print(f"Checking empty in {nlIndex},{wlIndex+i}")
                if self.grid[nlIndex][wlIndex+i] not in ['.',word[i]] : 
                    return False
            else:
                return True
        elif orient=="v":
            for i in range(lenght):
                print(f"Checking empty in {nlIndex+i},{wlIndex}")
                if self.grid[nlIndex+i][wlIndex] not in ['.',word[i]] : 
                    return False
            else:
                return True
        elif orient=="d":
                for i in range(lenght):
                    print(f"Checking empty in {nlIndex+i},{wlIndex+i}")
                    if self.grid[nlIndex+i][wlIndex+i] not in ['.',word[i]] : 
                        return False
                else:
                    return True
                
    def place_horizontal(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            print(nlIndex,wlIndex+i)
            self.grid[nlIndex][wlIndex+i] = word[i]

    def place_vertical(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            print(nlIndex+i,wlIndex)
            self.grid[nlIndex+i][wlIndex] = word[i]

    def place_diagonal(self,word,nlIndex,wlIndex,inv=0):
        lenght = len(word)
        if inv == 1:
            word = word[::-1]
        for i in range(lenght):
            print(nlIndex+i,wlIndex+i)
            self.grid[nlIndex+i][wlIndex+i] = word[i]

    def default_gen(self,orient,nno,wno,lenght):
        wlIndex,nlIndex = 0,0
        if orient == "h" : 
            print("Making horizontal points")
            wlIndex = randint(0,wno-1-lenght)
            nlIndex = randint(0,nno-1)
        elif orient == "v" : 
            print("Making vertical points")
            nlIndex = randint(0,nno-1-lenght)
            wlIndex = randint(0,wno-1)    
        elif orient == "d" : 
            print("Making diagonal points")
            wlIndex = randint(0,wno-1-lenght)
            nlIndex = randint(0,nno-1-lenght) 
        return wlIndex,nlIndex
     
    def find_spot(self,word,nno,wno):
        lenght = len(word)
        orientation = choice(["h","v","d"])
        inv = random.choice((0,1),p=[0.7,0.3])
        nlIndex,wlIndex = 0,0
        errors = 0
        wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            
        while True:
            if errors >0 and errors <5:
                print(f"Error type 1 : {errors}")
                if orientation == "h" : 
                    wlIndex = randint(0,wno-1-lenght)
                if orientation == "v" : 
                    nlIndex = randint(0,nno-1-lenght)
                if orientation == "d" : 
                    wlIndex = randint(0,wno-1-lenght)
                    nlIndex = randint(0,nno-1-lenght)       
            elif errors >=5 and errors < 10 :
                print(f"Error type 2 : {errors}") 
                if orientation == "h" : 
                    nlIndex = randint(0,nno-1-lenght)
                if orientation == "v" : 
                    wlIndex = randint(0,wno-1-lenght)
                if orientation == "d" : 
                    wlIndex = randint(0,wno-1-lenght)
                    nlIndex = randint(0,nno-1-lenght)
            elif errors >= 10 and errors <=14:
                print(f"Error type 3 : {errors}")
                orientation = choice(["h","v","d"])
            elif errors >=14 and errors<25:
                wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            elif errors >=25 and errors<100:
                orientation = choice(["h","v","d"])
                wlIndex,nlIndex = self.default_gen(orientation,nno,wno,lenght)
            elif errors >=100:
                self.temp_mistakes.append(word)        
                break 

            print(f"Checking for : {word}, with {errors} errors, and current pos {nlIndex},{wlIndex} and {orientation} orientation" )
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
                print(i,end=' ')
            print()



rows,cols = 15,15
wordList = ["APPLE","COMPREHENSIBLE","HONDA","PAPAYA","BEDSHEETS","ORANGE","MOTORBIKE","YATCH","PINEAPPLE","GOAT","DOG","PINATA","AVOCADO","GRAPES","DRINKING","WALKING","AMAZING","PIZZA","COCONUT","POTATOES"]
p = Puzzle(rows,cols,wordList)
p.print_puzzle()
