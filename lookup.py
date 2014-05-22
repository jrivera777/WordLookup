import tkinter as tk
from definition_area import DefinitionArea
from wordnik import *

class LookUpApplication(tk.Frame):
    apiUrl = 'http://api.wordnik.com/v4'
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.setupWordnik()
        self.grid()
        self.CreateControlVars()
        self.CreatePrimaryTextArea(50)
        self.BindEvents()
        self._defArea = DefinitionArea(master=self)
        self._defArea.Display()

    def setupWordnik(self):
        self.__apiKey = ' 44c913e6611b3f875994500746a0302819bb02d4ba3ee7dfc'
        self.__wordnik = WordApi.WordApi(swagger.ApiClient(self.__apiKey, self.apiUrl))
    
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
            self._defArea.setWord('')
            self._defArea.setDefinition('')
            hyphenation = self.__wordnik.getHyphenation(wd)
            if hyphenation != None:
                hyphWord =  '\xb7'.join(map(lambda syl: syl.text, hyphenation))
                self._defArea.setWord(hyphWord)
            
            
            
if __name__ == "__main__":
    app = LookUpApplication()
    app.master.title('Word Lookup')
    app.master.resizable(0,0)
    app.mainloop()
