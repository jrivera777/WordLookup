import tkinter as tk

class LookUpApplication(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.CreateControlVars()
        self.CreatePrimaryTextArea(50)
        self.BindEvents()
    
    # Create any control variables necessary
    def CreateControlVars(self):
        self.__word = tk.StringVar()
        self.__result = tk.StringVar()
    
    # Bind events to widgets
    def BindEvents(self):
        self.__wordBox.bind('<Return>', self.LookupOnReturnKey)

    #generate 
    def CreatePrimaryTextArea(self, w=30):
        self.__wordBoxLabel = tk.Label(self, text='Lookup:')
        self.__wordBox = tk.Entry(self, width=w, textvariable=self.__word)
        self.__resultLabel = tk.Label(self, textvariable=self.__result)

        self.__wordBoxLabel.grid(row=0, column=0)
        self.__wordBox.grid(row=0,column=1)


    ''' Events for different widgets
    '''

    def LookupOnReturnKey(self, event):
        wd = self.__word.get()
        self.__result.set('')
        self.__resultLabel.grid_remove()
        if wd != '':
            self.__word.set('')
            self.__result.set(wd)
            self.__resultLabel['bg'] = '#00ffff'
            self.__resultLabel.grid(columnspan=2, sticky=tk.E + tk.W)
       



if __name__ == "__main__":
    app = LookUpApplication()
    app.master.title('Word Lookup')
    app.master.resizable(0,0)
    app.mainloop()
