import tkinter as tk
from definition_area import DefinitionArea

class LookUpApplication(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.CreateControlVars()
        self.CreatePrimaryTextArea(50)
        self._defArea = DefinitionArea(master=self)
        self._defArea.Display()
    
    # Create any control variables necessary
    def CreateControlVars(self):
        self._word = tk.StringVar()

    
    # Bind events to widgets
    def BindEvents(self):
        self._wordBox.bind('<Return>', self.LookupOnReturnKey)

    # Generate Input area and bind necessary events
    def CreatePrimaryTextArea(self, w=30):
        self._wordBoxLabel = tk.Label(self, text='Lookup:')
        self._wordBox = tk.Entry(self, width=w, textvariable=self._word)
        # self.BindEvents()
        self._wordBoxLabel.grid(row=0, column=0)
        self._wordBox.grid(row=0,column=1)

    ''' Events for different widgets
    '''

    def LookupOnReturnKey(self, event):
        wd = self._word.get()
        if wd != '':
            self._word.set('')
            
            
if __name__ == "__main__":
    app = LookUpApplication()
    app.master.title('Word Lookup')
    app.master.resizable(0,0)
    app.mainloop()
