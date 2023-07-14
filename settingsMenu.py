from wordFinder import * 


class wordsearchGen(Tk):
    def __init__(self):
        super(wordsearchGen,self).__init__()
        self.title("WordSearch Generator")
        self.geometry("430x720")
        self.style = ThemedStyle()
        self.style.set_theme("breeze")
        self.radioButtons()
        self.placeWidgets()
    
    def updateRows(self,box : Label,slider : IntVar):
        val = slider.get()
        box.config(text=str(val))

    def radioButtons(self):
        self.caseval = IntVar()
        self.caseval.set(1)
        self.buttonframe = Frame(self)
        values = {"Uppercase letters only":1,"Lowercase letters only":2
                  ,"Mix of both cases      ":3}
        for text,value in values.items():
            Radiobutton(self.buttonframe,text=text, variable=self.caseval,value=value).pack(side="top")


    def getInfo(self):
        info = {}
        info["rows"] = int(self.rowE.get())
        info["cols"] = int(self.colE.get())
        info["case"] = self.caseval.get()


    def placeWidgets(self):
        self.windowtitle = Label(self,text="WordSearch Generator",font=("Courier",26,"bold","underline"),borderwidth=5)
        self.cas = Label(self,text="Case Options : ",font=("Courier",16),borderwidth=5)
        self.rows = Label(self,text="Number of Rows : ",font=("Courier",16))
        self.cols = Label(self,text="Number of Columns : ",font=("Courier",16))
        self.words = Button(self,text="Enter your words",command=lambda: openWordMaker(self,int(self.rowE.get()),int(self.colE.get())))
        
        self.genButton = Button(self,text="Generate puzzle",command=self.getInfo)

        self.rsize = IntVar(self)
        self.rsize.set(10)
        self.csize= IntVar(self)
        self.csize.set(10)

        self.rowE = Scale(self,variable=self.rsize,orient="horizontal",from_=10,to=100, command=lambda x: self.updateRows(self.rowcount,self.rsize))
        self.colE = Scale(self,variable=self.csize,orient="horizontal",from_=10,to=100, command=lambda x: self.updateRows(self.colcount,self.csize))
        self.rowcount = Label(width=2,font=("Courier",16,"bold"),text="10")
        self.colcount = Label(width=2,font=("Courier",16,"bold"),text="10")
        
        self.showWords = Label(self,font=("Courier",12,"bold"))
        self.showWords.config(text="No words chosen yet")

        self.windowtitle.grid(row=0,column=0,columnspan=2,sticky="NSEW")
        self.rows.grid(row=1,column=0,sticky="NSW ",pady=10)
        self.rowcount.grid(row=1,column=1,sticky="NSW")
        self.rowE.grid(row=2,column=0,sticky="NSEW",padx=60,columnspan=2)
        self.cols.grid(row=3,column=0,sticky="NSW ",pady=10)
        self.colcount.grid(row=3,column=1,sticky="NSW")
        self.colE.grid(row=4,column=0,sticky="NSEW",padx=60,columnspan=2)
        self.cas.grid(row=5,column=0,sticky="NSEW",pady=10)
        self.buttonframe.grid(row=6,column=0,sticky="NSW",padx=50,columnspan=2)
        self.showWords.grid(row=7,column=0,columnspan=2,sticky="NSEW",pady=10)
        self.words.grid(row=8,column=0,sticky="NS",columnspan=2)
        self.genButton.grid(row=9,column=0,columnspan=2,sticky="NS")






window = wordsearchGen()
window.mainloop()