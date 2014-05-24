import tkinter as tk
import tkinter.font

class DefinitionArea(tk.Frame):
    wordFont = 'Arial', 20
    definitionFont = 'Arial', 10
    pospFont = 'Arial', 10, 'normal', 'italic'
    def __init__(self, master=None, word='word goes here', colspan=1):
        tk.Frame.__init__(self, master)
        self.__span = colspan
        self.__definitions = []
#        self['bg'] = '#00ffff'
        self.CreateDefinitionArea()
    
    def CreateDefinitionArea(self):
        self._wordControl = tk.StringVar()
        self._wordLabel = tk.Label(self, textvariable=self._wordControl, 
                                   font=self.wordFont)

    def Display(self, dsp):
        if dsp:
            self._wordLabel.grid(column=0, columnspan=2, sticky=tk.W)
            self.grid(columnspan=self.__span, sticky=tk.W + tk.E)

            for df in self.__definitions:
                df.winfo_children()[0].grid(column=1) # display part of speech
                df.winfo_children()[1].grid(column=2, sticky=tk.W + tk.E)# display definition
                df.grid(sticky=tk.W + tk.E)
        else:
            self.grid_remove()

    def setWord(self, newWord):
        self._wordControl.set(newWord)
    
    def addDefinition(self, posp, newDef):
        defnFrame = tk.Frame(self)
        poSpeech = tk.Label(defnFrame, text=posp, font=self.pospFont)
        singleDef = tk.Label(defnFrame, text=newDef, font=self.definitionFont,
                             wraplength='90m', justify=tk.LEFT)
        self.__definitions.append(defnFrame)
        
    def clearDefinitions(self):
        for df in self.__definitions:
            df.grid_forget()
            df.destroy()
        del self.__definitions[:]
                
