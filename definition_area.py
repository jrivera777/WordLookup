import tkinter as tk
import tkinter.font

class DefinitionArea(tk.Frame):
    wordFont = 'Arial', 24
    definitionFont = 'Arial', 10
    def __init__(self, master=None, word='word goes here'):
        tk.Frame.__init__(self, master)
        self.CreateDefinitionArea('test')
        print(self.wordFont)
    
    def CreateDefinitionArea(self, word):
        self._wordControl = tk.StringVar()
        self._definitionControl = tk.StringVar()
        self._wordLabel = tk.Label(self, textvariable=self._wordControl, 
                                   font=self.wordFont)
        self._definitionLabel = tk.Label(self, 
                                         textvariable=self._definitionControl,
                                         font=self.definitionFont)
        self._wordControl.set(word)
        self._definitionControl.set('definition goes here.')


    def Display(self):
        self._wordLabel.grid()
        self._definitionLabel.grid()
        self.grid(sticky=tk.W + tk.E)
