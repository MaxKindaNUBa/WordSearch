from apiCalls import *
from tkinter import *
from tkinter.ttk import *
from tktooltip import ToolTip
from ttkthemes import ThemedStyle


def openWordMaker(row,col):
    demoFinder = wordFinder(row,col)
    demoFinder.mainloop()

class wordFinder(Tk):
    def __init__(self,row,col):
        super().__init__()
        self.title("Word Finder")
        self.geometry("580x560")
        self.row = row
        self.col = col

        self.theme = ThemedStyle()
        self.theme.set_theme("breeze")
        self.ansPercent = int(0.4*(self.row*self.col))
        self.wordList()
        self.placeWidgets()
        
    def updateRows(self,box : Label,slider : IntVar):
        val = slider.get()
        box.config(text=str(val)) 


    def wordList(self):
        self.wordframe = Frame(self)
        self.wordbox = Text(self.wordframe, width=55,height=15,font=("Courier",12,"bold"),borderwidth=2,bg="#5aaef2",wrap="word")
        self.scroll = Scrollbar(self.wordframe,orient="vertical",command=self.wordbox.yview)
        self.wordbox.config(yscrollcommand=self.scroll.set)
        fillbutton = Button(self.wordframe,text="Auto-Fill words for topic",command=lambda: self.genWords(int(self.wcountE.get()),int(self.startrE.get()),int(self.endrE.get())))

        ToolTip(self.wordbox,msg="Seperate the words by commas.Letters shound be in lowercase. \nFor Example  \n\napple , mango , cherry , pineapple")
        self.wordbox.grid(row=0,column=0,sticky="NSEW")
        fillbutton.grid(row=1,column=0,pady=5,padx=5,sticky="NSEW")
        self.scroll.grid(row=0,column=1,sticky="NSEW")

    def placeWidgets(self):

        self.windowtitle = Label(self,text="Words Finder",font=("Courier",26,"bold","underline"),borderwidth=5)
        self.wcount = Label(self,text="Number of words to be added: ",font=("Courier",14),borderwidth=3)
        self.wcountE = Entry(self,font=("Courier",16),width=3)

        self.startr = Label(self,text="Minimum word lenght : ",font=("Courier",16))
        self.startrsize = IntVar(self)
        self.startrsize.set(4)
        self.startrcount = Label(self,width=2,font=("Courier",16,"bold"),text="4")
        self.startrE = Scale(self,variable=self.startrsize,orient="horizontal",from_=4,to=15, command=lambda x: self.updateRows(self.startrcount,self.startrsize))
        
        self.endr = Label(self,text="Minimum word lenght : ",font=("Courier",16))
        self.endrsize = IntVar(self)
        self.endrsize.set(4)
        self.endrcount = Label(self,width=2,font=("Courier",16,"bold"),text="4")
        self.endrE = Scale(self,variable=self.endrsize,orient="horizontal",from_=4,to=15, command=lambda x: self.updateRows(self.endrcount,self.endrsize))

        self.findButt = Button(self,text="Confirm List",padding=5)

        self.recAnsPercent = Label(self,text=f"Recomended number of letters to be findable: {self.ansPercent}",font=("Courier",14,"bold"),borderwidth=3)
        ToolTip(self.recAnsPercent,msg="The recommended number of letters which maybe hidden within the puzzle. \n\nThis is important as too high of a value can either make the puzzle too cluttered \nor even break the game")

        self.obtAnsPercent = Label(self,text=f"Total given number of letters to be findable: 0",font=("Courier",14,"bold"),borderwidth=3)


        self.windowtitle.grid(row=0,column=0,columnspan=2,sticky="NS")
        self.wcount.grid(row=1,column=0,sticky="NSW")
        self.wcountE.grid(row=1,column=1,columnspan=2,sticky="NSW")

        self.startr.grid(row=3,column=0,sticky="NSEW")
        self.startrcount.grid(row=3,column=1,sticky="NSW")
        self.startrE.grid(row=4,column=0,columnspan=2,sticky="NS")

        self.endr.grid(row=5,column=0,sticky="NSEW")
        self.endrcount.grid(row=5,column=1,sticky="NSW")
        self.endrE.grid(row=6,column=0,columnspan=2,sticky="NS")
        self.findButt.grid(row=9,column=0,columnspan=2,sticky="NS")
        self.wordframe.grid(row=7,column=0,columnspan=2,sticky="NSEW")
        self.recAnsPercent.grid(row=8,column=0,columnspan=2,padx=10,sticky="NSEW")
        self.obtAnsPercent.grid(row=9,column=0,columnspan=2,padx=10,sticky="NSEW")
    
    def genWords(self,num,min,max):
        words = asyncio.run(get_words(min,max,int(num)))
        for i in words:
            self.wordbox.insert(END,i+ ' , ')
        self.updateAnsPercent()
    
    def updateAnsPercent(self):
        self.listOfWords = self.wordbox.get(0.0,END).split(' , ')[:-1]
        count = 0
        for i in self.listOfWords:
            count+=len(i)
        self.obtAnsPercent.config(text=f"Total given number of letters to be findable: {count}")


openWordMaker(15,15)