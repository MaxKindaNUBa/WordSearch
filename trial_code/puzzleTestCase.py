from wordSearchGen import Puzzle

'''
This is just a test case.
Ability to pull out words from a DB will be added soon.
Feel free to mess around with the grid size and settings.
'''

#Generating the test case
#Minimum size for this test list is (70%)
#Meaning the algo can successfully fill about 70% of the grid when the word lenghts are reasonable (3-10 words)

rows,cols = 30,30
wordList = ["APPLE","SOYSAUCE","SPINACH","BREAD","COUPLE","AIR","HONDA","PAPAYA","BEDSHEETS",
            "ORANGE","MOTORBIKE","YATCH","PINEAPPLE","GOAT","DOG","PINATA",
            "AVOCADO","GRAPES","DRINKING","WALKING","AMAZING","PIZZA","COCONUT","POTATOES"]

p = Puzzle(rows,cols,wordList,invExist=True,emptySpaces=True,crazyChars=True,mixCasing=True,answersOnly = False)
p.generate_grid()


p.print_puzzle()

print("\n\nAnswers : ")
print(p.answers)
