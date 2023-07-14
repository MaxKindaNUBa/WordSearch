from random import randint

words = ['beliers' , 'ankh' , 'jolty' , 'vair' , 'kiblah' , 'gaugers' , 'cementa' , 'nidi' , 'fort' , 'zing'] 

grid = [[' ' for i in range(15)] for i in range(15)]

def trial_gen(lenght,wlistlenght,nlistlenght):
    wLIndex,nLIndex = randint(0,wlistlenght-1),randint(0,nlistlenght-1)
    errorCount = 0

    while True:
        if errorCount > 9:
            nLIndex = randint(0,nlistlenght-1)

            errorCount = 0
        else:
            wLIndex = randint(0,wlistlenght-1)
            if (wlistlenght-1)-wLIndex < lenght:
                errorCount+=1
            else:
                break   
    return nLIndex,wLIndex

def place_horizontal(word,rows,cols):
    lenght = len(word)
    nlIndex,wlIndex = trial_gen(lenght,rows,cols)

    while True:
        if grid[nlIndex][wlIndex:lenght+1].count(' ') >= lenght:
            count=0
            for i in word:
                grid[nlIndex][wlIndex+count] = i
                print(nlIndex,wlIndex+count)
                count+=1
            break
        else:
            nlIndex,wlIndex = trial_gen(lenght,rows,cols)



for i in words:
    place_horizontal(i,15,15)


print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
for i in grid:
    print(i)
print('~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
