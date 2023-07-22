import random

def sort(lis):
    for i in range(0,len(lis)):
        for j in range(0,len(lis)-1-i):
            if len(lis[j])<len(lis[j+1]):
                lis[j],lis[j+1]=lis[j+1],lis[j]

def default_gen(orientation,nno,wno,lenght):
    wlIndex,nlIndex = 0,0
    if orientation == "h" : 
        print("Making horizontal points")
        wlIndex = random.randint(0,wno-1-lenght)
        nlIndex = random.randint(0,nno-1)

    elif orientation == "v" : 
        print("Making vertical points")
        nlIndex = random.randint(0,nno-1-lenght)
        wlIndex = random.randint(0,wno-1)
        
    elif orientation == "d" : 
        print("Making diagonal points")
        wlIndex = random.randint(0,wno-1-lenght)
        nlIndex = random.randint(0,nno-1-lenght) 

    return wlIndex,nlIndex

def place_horizontal(word,nlIndex,wlIndex):
    lenght = len(word)
    for i in range(lenght):
        print(nlIndex,wlIndex+i)
        grid[nlIndex][wlIndex+i] = word[i]
def place_vertical(word,nlIndex,wlIndex):
    lenght = len(word)
    for i in range(lenght):
        print(nlIndex+i,wlIndex)
        grid[nlIndex+i][wlIndex] = word[i]
def place_diagonal(word,nlIndex,wlIndex):
    lenght = len(word)
    for i in range(lenght):
        print(nlIndex+i,wlIndex+i)
        grid[nlIndex+i][wlIndex+i] = word[i]


def check_empty(orientation,word,nlIndex,wlIndex):
    lenght = len(word)

    if orientation=="h":
        for i in range(lenght):
            print(f"Checking empty in {nlIndex},{wlIndex+i}")
            if grid[nlIndex][wlIndex+i] not in ['.',word[i]] : 
                return False
        else:
            return True
        
    elif orientation=="v":
        for i in range(lenght):
            print(f"Checking empty in {nlIndex+i},{wlIndex}")
            if grid[nlIndex+i][wlIndex] not in ['.',word[i]] : 
                return False
        else:
            return True
        
    elif orientation=="d":
            for i in range(lenght):
                print(f"Checking empty in {nlIndex+i},{wlIndex+i}")
                if grid[nlIndex+i][wlIndex+i] not in ['.',word[i]] : 
                    return False
            else:
                return True


def second_spot(word,nno,wno):
    lenght = len(word)
    if check_empty("h",word,0,0):
        place_horizontal(word,0,0)
    elif check_empty("h",word,0,wno-1-lenght):
        place_horizontal(word,0,wno-1-lenght)
    elif check_empty("h",word,nno-1,0):
        place_horizontal(word,nno-1,0)
    elif check_empty("h",word,nno-1,wno-1-lenght):
        place_horizontal(word,nno-1,wno-1-lenght)
    elif check_empty("v",word,0,0):
        place_vertical(word,0,0)
    elif check_empty("v",word,wno-1,0):
        place_vertical(word,wno-1,0)
    elif check_empty("v",word,nno-1-lenght,0):
        place_vertical(word,nno-1-lenght,0)
    elif check_empty("v",word,nno-1-lenght,wno-1):
        place_vertical(word,nno-1-lenght,wno-1)

 
def find_spot(word,nno,wno):
    lenght = len(word)
    orientation = random.choice(["h","v","d"])
    nlIndex,wlIndex = 0,0
    errors = 0
    wlIndex,nlIndex = default_gen(orientation,nno,wno,lenght)
        
    while True:
        if errors >0 and errors <5:
            print(f"Error type 1 : {errors}")
            if orientation == "h" : 
                wlIndex = random.randint(0,wno-1-lenght)
            if orientation == "v" : 
                nlIndex = random.randint(0,nno-1-lenght)
            if orientation == "d" : 
                wlIndex = random.randint(0,wno-1-lenght)
                nlIndex = random.randint(0,nno-1-lenght)       
        elif errors >=5 and errors < 10 :
            print(f"Error type 2 : {errors}") 
            if orientation == "h" : 
                nlIndex = random.randint(0,nno-1-lenght)
            if orientation == "v" : 
                wlIndex = random.randint(0,wno-1-lenght)
            if orientation == "d" : 
                wlIndex = random.randint(0,wno-1-lenght)
                nlIndex = random.randint(0,nno-1-lenght)
        elif errors >= 10 and errors <=14:
            print(f"Error type 3 : {errors}")
            orientation = random.choice(["h","v","d"])
        elif errors >=14 and errors<25:
            wlIndex,nlIndex = default_gen(orientation,nno,wno,lenght)
        elif errors >=25 and errors<100:
            orientation = random.choice(["h","v","d"])
            wlIndex,nlIndex = default_gen(orientation,nno,wno,lenght)
        elif errors >=100:
            mistakes.append(word)        
            break 

        print(f"Checking for : {word}, with {errors} errors, and current pos {nlIndex},{wlIndex} and {orientation} orientation" )
        if check_empty(orientation,word,nlIndex,wlIndex) == True: 
            errors=0
            return wlIndex,nlIndex,orientation        
        else:
            errors+=1

def word_place(word,nno,wno):
    info = find_spot(word,nno,wno)

    if info != None :
        wlIndex,nlIndex,orientation = info
        if orientation == "h":
            place_horizontal(word,nlIndex,wlIndex)
        elif orientation == "v" : 
            place_vertical(word,nlIndex,wlIndex)
        elif orientation == "d" : 
            place_diagonal(word,nlIndex,wlIndex)

    if len(mistakes) != 0 :
        print("Placing the mistaken words")
        for word in mistakes:
            second_spot(word,nno,wno)



grid = [['.' for i in range(15)] for i in range(15)]
wordList = ["BELIEVER","SOCCER","ICECREAM","BEAUTY","HAPPY","APPLE","ORANGE","MOTORBIKE","YATCH","PINEAPPLE","GOAT","DOG","PINATA","AVOCADO","GRAPES","DRINKING","WALKING","PIZZA"]
sort(wordList)
print(wordList)

mistakes=[]

for word in wordList:
    word_place(word,15,15)


#Will be unquoted when the program is actually deployed

for lis in range(len(grid)):
    for j in range(len(grid[lis])):
        if grid[lis][j] == '.':
            grid[lis][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            continue
        

for i in grid:
    print(i)

print(f"Find the words : {wordList}")