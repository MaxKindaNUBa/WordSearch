from wordSearchGen import Puzzle

'''
This is just a test case.
Ability to pull out words from a DB will be added soon.
Feel free to mess around with the grid size and settings.
'''

#Generating the test case
#Minimum size for this test list is (70%)
#Meaning the algo can successfully fill about 70% of the grid when the word lenghts are reasonable (3-10 words)

rows,cols = 20,20
wordList = ["APPLE","SOYSAUCE","SPINACH","BREAD","COUPLE","AIR","HONDA","PAPAYA","BEDSHEETS","ORANGE","MOTORBIKE","YATCH","PINEAPPLE","GOAT","DOG","PINATA","AVOCADO","GRAPES","DRINKING","WALKING","AMAZING","PIZZA","COCONUT","POTATOES"]

p = Puzzle(rows,cols,wordList,invExist=True,emptySpaces=False,crazyChars=False,mixCasing=False,answersOnly = True)
p.generate_grid()

p.print_puzzle()
