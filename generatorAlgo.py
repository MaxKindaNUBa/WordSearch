from random import randint

words = ['beliers' , 'ankh' , 'jolty' , 'vair' , 'kiblah' , 'gaugers' , 'cementa' , 'nidi' , 'fort' , 'zing'] 

grid = [[' ' for i in range(10)] for i in range(15)]


def check_empty(nlIndex,wlIndex,lenght,orient):
    if orient == "h":
        for i in range(lenght):
            if grid[nlIndex][wlIndex+i] != ' ':
                return False
        else:
            return True


def trial_gen(lenght,wlistlenght,nlistlenght):
    wLIndex,nLIndex = randint(0,wlistlenght-1),randint(0,nlistlenght-1)
    errorCount = 0

    while True:
        if errorCount > 3:
            nLIndex = randint(0,nlistlenght-1)
            errorCount = 0
        else:
            if (wlistlenght-1)-wLIndex < lenght:
                wLIndex = randint(0,wlistlenght-1)
                errorCount+=1
            else:
                break   
    return nLIndex,wLIndex

def place_horizontal(word,wlistlenght,nlistlenght):
    lenght = len(word)
    nlIndex,wlIndex = trial_gen(lenght,wlistlenght,nlistlenght)
    count=0
    while True:
        if ((wlistlenght-1-wlIndex) > lenght) and check_empty(nlIndex,wlIndex,lenght,"h"):
            for i in word:
                grid[nlIndex][wlIndex+count] = i
                print(i,nlIndex,wlIndex+count)
                count+=1
            break
        else:
            nlIndex,wlIndex = trial_gen(lenght,wlistlenght,nlistlenght)

def place_vertical(word,wlistlenght,nlistlenght):
    lenght = len(word)
    nlIndex,wlIndex = trial_gen(lenght,nlistlenght,wlistlenght)
    count=0
    while True:
        if ((nlistlenght-1-nlIndex) > lenght) and check_empty(wlIndex,nlIndex,lenght,"h"):
            for i in word:
                grid[wlIndex][nlIndex+count] = i
                print(i,nlIndex,wlIndex+count)
                count+=1
            break
        else:
            nlIndex,wlIndex = trial_gen(lenght,nlistlenght,wlistlenght)
   
for i in words:
    place_horizontal(i,10,15)


print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
for i in grid:
    print(i)
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
