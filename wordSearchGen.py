from random import randint,choice
from numpy import random as npRandom

class Puzzle():
    def __init__(self,rows,cols,wordList,invExist=False,emptySpaces=False,crazyChars=False,mixCasing=False,answersOnly=False) -> None:
        self.grid = [['.' for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols
        self.wordList = wordList
        self.temp_mistakes = []
        self.answers = {}
        self.remakeCount = 0
        self.invExist = invExist
        self.emptySpaces = emptySpaces
        self.crazyChars = crazyChars
        self.mixCasing = mixCasing
        self.answersOnly = answersOnly
        self.wSort(self.wordList)

    def mixCase(self):
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

                    if self.emptySpaces == True and self.crazyChars == True:
                        option = npRandom.choice((0,1),p=[0.5,0.5]) #choosing btw empty space or charecter : 0-empty , 1-charecter
                        if option == 0:
                            let_empty = npRandom.choice((0,1),p=[0.7,0.3]) #0-filled,1-empty
                            if let_empty == 0:
                                self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        elif option == 1:
                            char = npRandom.choice((1,0),p=[0.6,0.4]) #0-alphabet,1-charecter
                            if char == 0:
                                self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                            else:
                                self.grid[lis][j] = choice("!@#$%^&*()`~,<.>/?;:'\"|[]{}")
                    elif self.emptySpaces == True:
                        let_empty = npRandom.choice((0,1),p=[0.7,0.3]) #0-filled,1-empty
                        if let_empty == 0:
                            self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    elif self.crazyChars == True:
                        char = npRandom.choice((1,0),p=[0.6,0.4]) #0-alphabet,1-charecter
                        if char == 0:
                            self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        else:
                            self.grid[lis][j] = choice("!@#$%^&*()`~,<.>/?;:'\"|[]{}")
                    else:
                        self.grid[lis][j] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                else:
                    continue

    def generate_grid(self):
        for word in self.wordList:
            coordinates = self.word_place(word,self.rows,self.cols)
            #to be added in word_place
            if coordinates == None:
                pass
            else:
                self.answers[word] = coordinates
        
        if self.temp_mistakes.copy() != []:
            for word in self.temp_mistakes:
                ans = self.second_spot(word,self.rows,self.cols)
                if ans[0]:
                    #insert things here !!!!!!!!!!
                    #True,"v",i,wno-1
                    self.answers[word] = (ans[1],ans[2],ans[3])
                    self.temp_mistakes.remove(word) 

        if len(self.temp_mistakes) !=0 :
            if self.remakeCount < 6: 
                self.grid = [['.' for i in range(self.cols)] for i in range(self.rows)]
                self.temp_mistakes.clear()
                self.remakeCount +=1
                self.attempt_placing()
            else:
                print("Failed to place words : ",self.temp_mistakes)
        else:
            print("Placing successfull\n\n")

        if self.answersOnly == False:
            self.fill_empty() 
            if self.mixCasing == True:
                self.mixCase()


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
            n,w = nlIndex,wlIndex
            if inv == 1:
                word = word[::-1]
                if orientation == "h":
                    w += len(word)
                elif orientation == "v":
                    n += len(word)
                elif orientation == "md":
                    w += len(word)-1
                    n += len(word)-1
                elif orientation == "sd":
                    n += len(word)-1
                    w -= len(word)-1

            if orientation == "h":
                self.place_horizontal(word,nlIndex,wlIndex)
            elif orientation == "v" : 
                self.place_vertical(word,nlIndex,wlIndex)
            elif orientation == "md" : 
                self.place_Mdiagonal(word,nlIndex,wlIndex)
            elif orientation == "sd":
                self.place_Sdiagonal(word,nlIndex,wlIndex)
            
            return orientation,n,w
        else:
            return None

    def second_spot(self,word,nno,wno):
        lenght = len(word)
        for i in range(0,wno-lenght+1):
            if self.check_empty("h",word,0,i,0):
                self.place_horizontal(word,0,i,0)
                return True,"h",0,i
            elif self.check_empty("h",word,0,i,1):
                self.place_horizontal(word,0,i,1)
                return True,"h",0,i+len(word)
            elif self.check_empty("h",word,nno-1,i,0):
                self.place_horizontal(word,nno-1,i,0)
                return True,"h",nno-1,i
            elif self.check_empty("h",word,nno-1,i,1):
                self.place_horizontal(word,nno-1,i,1)
                return True,"h",nno-1,i+len(word)
        else:        
            for i in range(0,nno-lenght+1):
                if self.check_empty("v",word,i,wno-1,0):
                    self.place_vertical(word,i,wno-1,0)
                    return True,"v",i,wno-1
                elif self.check_empty("v",word,i,wno-1,1):
                    self.place_vertical(word,i,wno-1,1)
                    return True,"v",i+len(word),wno-1
                elif self.check_empty("v",word,i,0,0):
                    self.place_vertical(word,i,0,0)
                    return True,"v",i,0
                elif self.check_empty("v",word,i,0,1):
                    self.place_vertical(word,i,0,1)
                    return True,"v",i+len(word),0

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