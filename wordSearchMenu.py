import tkinter
from tkinter import IntVar
from tkinter.ttk import Separator,Label,Frame,Radiobutton,Entry,Scale
from ttkthemes import ThemedStyle


class mainWindow(tkinter.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.style = ThemedStyle()
        self.style.set_theme("breeze")
        self.title("Word Search Generator")
        self.geometry("900x400")
        self.header= Label(self,text="WordSearch Generator",font=("Courier",26,"bold","underline"),borderwidth=5)
        self.sep = Separator(self,orient="vertical")

        self.header.place(x=100,y=10)

        self.frame_left()
        self.lframe.place(x=20,y=60)
        self.sep.place(x=440,y=75, relwidth=0.4, relheight=0.75)
        self.frame_right()
        self.rframe.place(x=500,y=60)
    
    def radioButtons(self):
        self.caseval = IntVar()
        self.caseval.set(1)
        self.buttonframe = Frame(self.lframe)

        values = {"Uppercase letters only":1,"Lowercase letters only":2
                  ,"Mix of both cases      ":3}
        for text,value in values.items():
            Radiobutton(self.buttonframe,text=text, variable=self.caseval,value=value).pack(side="top")

    def frame_left(self):
        self.lframe = Frame(self)
        
        #title and entry box
        self.titleframe = Frame(self.lframe)
        self.topic = Label(self.titleframe,text="Title : ",font=("Courier",16))
        self.topicEnt = Entry(self.titleframe,font=("Courier",16),width=20)
        
        #label for case options
        self.cas = Label(self.lframe,text="Case Options : ",font=("Courier",16),borderwidth=5)

        #rows and cols slider and value reader in their frames
        self.rowframe = Frame(self.lframe)
        self.rows = Label(self.rowframe,text="Number of Rows : ",font=("Courier",16))
        self.rsize = IntVar(self.rowframe)
        self.rsize.set(10)
        self.rowcount = Label(self.rowframe,width=2,font=("Courier",16,"bold"),text="10")
        self.rows.grid(row=0,column=0)
        self.rowcount.grid(row=0,column=1)

        self.colframe = Frame(self.lframe)
        self.cols = Label(self.colframe,text="Number of Cols : ",font=("Courier",16))
        self.csize= IntVar(self.colframe)
        self.csize.set(10)
        self.colcount = Label(self.colframe,width=2,font=("Courier",16,"bold"),text="10")
        self.cols.grid(row=0,column=0)
        self.colcount.grid(row=0,column=1)

        self.rowE = Scale(self.lframe,variable=self.rsize,orient="horizontal",from_=10,to=100, command=lambda x: self.updateRows(self.rowcount,self.rsize))
        self.colE = Scale(self.lframe,variable=self.csize,orient="horizontal",from_=10,to=100, command=lambda x: self.updateRows(self.colcount,self.csize))
    

        #case options radiobuttons
        self.radioButtons()

        #place on titleframe
        self.topic.grid(row=0,column=0,sticky="NSE")
        self.topicEnt.grid(row=0,column=1,sticky="NSW")

        #place on lframe
        self.titleframe.grid(row=0,column=0,pady=10)

        self.rowframe.grid(row=1,column=0,sticky="NSEW",pady=6)
        self.rowE.grid(row=2,column=0,columnspan=2,sticky="NSEW",padx=30)

        self.colframe.grid(row=3,column=0,sticky="NSEW",pady=6)
        self.colE.grid(row=4,column=0,columnspan=2,sticky="NSEW",padx=30)

        self.cas.grid(row=5,column=0,sticky="NSW",pady=6)
        self.buttonframe.grid(row=6,column=0,columnspan=2,sticky="NSW",padx=20)

    def frame_right(self):
        self.rframe = Frame(self)
        
        #title and entry box
        self.numframe = Frame(self.rframe)
        self.nums = Label(self.numframe,text="No. of Words : ",font=("Courier",16))
        self.numsEnt = Entry(self.numframe,font=("Courier",16),width=5)

        #rows and cols slider and value reader in their frames
        self.minframe = Frame(self.rframe)
        self.mins = Label(self.minframe,text="Min word lenght : ",font=("Courier",16))
        self.mincount = Entry(self.minframe,width=4,font=("Courier",16,"bold"))
        self.mins.grid(row=0,column=0)
        self.mincount.grid(row=0,column=1)

        self.maxframe = Frame(self.rframe)
        self.maxs = Label(self.maxframe,text="Max word lenght : ",font=("Courier",16))
        self.maxcount = Entry(self.maxframe,width=4,font=("Courier",16,"bold"))
        self.maxs.grid(row=0,column=0)
        self.maxcount.grid(row=0,column=1)

        #place on titleframe
        self.nums.grid(row=0,column=0,sticky="NSE")
        self.numsEnt.grid(row=0,column=1,sticky="NSW")

        #place on rframe
        self.numframe.grid(row=0,column=0,pady=10)

        self.minframe.grid(row=1,column=0,sticky="NSEW",pady=6)

        self.maxframe.grid(row=3,column=0,sticky="NSEW",pady=6)
        





app = mainWindow()

app.mainloop()