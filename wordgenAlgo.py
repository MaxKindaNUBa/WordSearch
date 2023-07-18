import random

grid = [['.' for i in range(15)] for i in range(15)]
mistakes=[]
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


def check_empty(orientation,word,nlIndex,wlIndex):
    lenght = len(word)

    if orientation=="h":
        for i in range(lenght):
            if grid[nlIndex][wlIndex+i] not in ['.',word[i]] : 
                return False
        else:
            return True
        
    elif orientation=="v":
        for i in range(lenght):
            if grid[nlIndex+i][wlIndex] not in ['.',word[i]] : 
                return False
        else:
            return True
        
    elif orientation=="d":
            for i in range(lenght):
                if grid[nlIndex+i][wlIndex+i] not in ['.',word[i]] : 
                    return False
            else:
                return True


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
        if errors >=5 and errors < 10 :
            print(f"Error type 2 : {errors}") 
            if orientation == "h" : 
                nlIndex = random.randint(0,nno-1-lenght)
            if orientation == "v" : 
                wlIndex = random.randint(0,wno-1-lenght)
            if orientation == "d" : 
                wlIndex = random.randint(0,wno-1-lenght)
                nlIndex = random.randint(0,nno-1-lenght)
        if errors >= 10 and errors <=14:
            print(f"Error type 3 : {errors}")
            orientation = random.choice(["h","v","d"])
        if errors >=14:
            wlIndex,nlIndex = default_gen(orientation,nno,wno,lenght)
        if errors >=500 :
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
    lenght = len(word)

    if info != None :
        wlIndex,nlIndex,orientation = info
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


for word in ["believer","soccer","icecream","beautifull","happy","apple","orange","motorbike","yatch","pineapple","goat","dog"]:
    word_place(word,15,15)


#Will be unquoted when the program is actually deployed
'''
for lis in range(len(grid)):
    for j in range(len(grid[lis])):
        if grid[lis][j] == '.':
            grid[lis][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            continue

'''
for i in grid:
    print(i)

print(f"Words that couldnt be added : {mistakes}")