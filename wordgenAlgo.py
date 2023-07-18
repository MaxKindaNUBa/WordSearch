import random

grid = [['.' for i in range(15)] for i in range(15)]


def check_empty(orientation,word,nlIndex,wlIndex):
    lenght = len(word)

    if orientation=="h":
        for i in range(lenght):
            if grid[nlIndex][wlIndex+i] != '.' : 
                return False
        else:
            return True
        
    elif orientation=="v":
        for i in range(lenght):
            if grid[nlIndex+i][wlIndex] != '.' : 
                return False
        else:
            return True
        
    elif orientation=="d":
            for i in range(lenght):
                if grid[nlIndex+i][wlIndex+i] != '.' : 
                    return False
            else:
                return True


def find_spot(word,nno,wno):
    lenght = len(word)
    orientation = random.choice(["h","v","d"])
    nlIndex,wlIndex = 0,0
    errors = 0

    if orientation == "h" : 
        wlIndex = random.randint(0,wno-1-lenght)
        nlIndex = random.randint(0,nno-1)

    elif orientation == "v" : 
        nlIndex = random.randint(0,nno-1-lenght)
        wlIndex = random.randint(0,wno-1)
        
    elif orientation == "d" : 
        wlIndex = random.randint(0,wno-1-lenght)
        nlIndex = random.randint(0,nno-1-lenght)
        
    while True:
        if errors >=0 and errors <5:
            if orientation == "h" : 
                wlIndex = random.randint(0,wno-1-lenght)
            if orientation == "v" : 
                nlIndex = random.randint(0,nno-1-lenght)
            if orientation == "d" : 
                wlIndex = random.randint(0,wno-1-lenght)
                nlIndex = random.randint(0,nno-1-lenght)       
        if errors >=5 and errors < 10 : 
            if orientation == "h" : 
                nlIndex = random.randint(0,nno-1-lenght)
            if orientation == "v" : 
                wlIndex = random.randint(0,wno-1-lenght)
            if orientation == "d" : 
                wlIndex = random.randint(0,wno-1-lenght)
                nlIndex = random.randint(0,nno-1-lenght)
        if errors >= 10:
            orientation = random.choice(["h","v","d"])
            
        print(f"Checking for : {word}, with {errors} errors, and current pos {nlIndex},{wlIndex} and {orientation} orientation" )
        if check_empty(orientation,word,nlIndex,wlIndex) == True: 
            errors=0
            return wlIndex,nlIndex,orientation        
        else:
            errors+=1


def word_place(word,nno,wno):

    wlIndex,nlIndex,orientation = find_spot(word,nno,wno)
    lenght = len(word)

    if orientation == "h":
        for i in range(lenght):
            print(nlIndex,wlIndex+i)
            grid[nlIndex][wlIndex+i] = word[i]
    elif orientation == "v" : 
        for i in range(lenght):
            print(nlIndex+i,wlIndex)
            grid[nlIndex+i][wlIndex] = word[i]
    elif orientation == "d" : 
        for i in range(lenght):
            print(nlIndex+i,wlIndex+i)
            grid[nlIndex+i][wlIndex+i] = word[i]

for word in ["believer","soccer","icecream","beautifull","happy","apple","orange"]:
    word_place(word,15,15)

for i in grid:
    print(i)


