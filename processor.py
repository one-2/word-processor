# This document was created by Stephen Elliott on 12/5/23.
# Libraries
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os

import time


# Constants
ROOTTITLE = "Poetic (development build)"
SAVEFOLDER = "save_folder"
FILEPROMPTSTRING = "Please input a file path: "
TESTCWD = "/mnt/c/Users/steph/OneDrive/Documents/my_programming/word_processor"
TESTREADFILE = "test_read.txt"
TESTSAVEASFILE = "test_saveas.txt"
NOCURRFILE = None


# Classes
class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("400x500")
        self.parent.title(ROOTTITLE)

        self.scrollbar = ScrollBar(parent = self)
        self.textbox = TextBox(parent = self)
        self.textbox.scrollbarSetup()
        self.menus = Menus(parent = self)
        self.counter = Counter(self)
        
        self.persistent = PersistenceOps(parent = self)  ### myMain.persistent
        
        self.bindEvents()
    

    def bindEvents(self):
        self.textbox.box.bind("<KeyRelease>", self.counter.run)


class ScrollBar(tk.Frame):
    def __init__(self, parent):     # Build the scrollbar
        self.parent = parent
        self.scroll = tk.Scrollbar(root)
        self.scroll.pack(side = "right", fill = "y")
    
    def returnScroll(self):
        return self.scroll
    
    def textboxScrollbarConfig(self,textbox):
        self.scroll.config(command = self.parent.textbox.returnTextbox().yview)


class TextBox(tk.Frame):
    def __init__(self, parent):     # Build the textbox
        self.parent = parent
        self.box = tk.Text(root)
        self.box.pack(fill = "both")

    def scrollbarSetup(self):
        self.box.config(yscrollcommand = self.parent.scrollbar.returnScroll().set)
        self.parent.scrollbar.textboxScrollbarConfig(self)

    def retrieveContents(self):    # retrieve text from the textbox
        return self.box.get("1.0", "end-1c")
    
    def loadNewDocument(self, string):
        self.box.replace("0.0", self.box.index('end'), string)

    def printToConsole(self):   # print user text to console
        print(self.retrieveContents())

    def returnTextbox(self):
        return self.box



class Menus(tk.Frame):
    def __init__(self, parent): # build the menus
        self.parent = parent

        root.option_add("*tearOff", False)                  # kill the tearoff
        self.menubar = tk.Menu(root)                        # create a menu for the root (IS A DEFAULT CREATED FOR YOU?)
        root.config(menu = self.menubar)                    # allocate the menubar to the root window

        self.fileMenu()                                    # create the desired menus
        self.editMenu()
        self.testMenu()


    def fileMenu(self):
        self.file = tk.Menu(self.menubar)                           # create a menu object on the menubar called "file"
        self.menubar.add_cascade(label = "File", menu = self.file)  # create a file tab in the menu object

        self.file.add_command(label = "New",     command = lambda: fileOps.newFile())        # add several commands to the file tab
        self.file.add_command(label = "Open",    command = lambda: fileOps.openFile())
        self.file.add_command(label = "Save",    command = lambda: fileOps.saveFile(myMain.persistent.currFile))
        self.file.add_command(label = "Save as", command = lambda: fileOps.saveAsFile())
    
    def editMenu(self):
        self.edit = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = "Edit", menu = self.edit)

    def testMenu(self):
        self.test = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = "test", menu = self.test)
        self.test.add_command(label = "Print to console", command = self.parent.textbox.printToConsole)               # command = printusertexttoconsole)


class fileOps(tk.Frame):
    def newFile():      # create a new file to save to
        pass
    #    path = fileOps.saveAsFilePrompter()
    #    with open(path, "w") as f:
    #        f.write(myMain.textbox.retrieveContents())
    #    myMain.persistent.changeCurrFile(path)

    def openFile():
        path = os.path.join(TESTCWD, SAVEFOLDER, TESTREADFILE)          #USER PATH INPUT  path = fileOps.openFilePrompter()
        contents = fileOps.openFileContents(path)
        myMain.textbox.loadNewDocument(contents)
        myMain.persistent.changeCurrFile(path)

    def openFilePrompter():
        return filedialog.askopenfilename(initialdir = "/",
                                          title = FILEPROMPTSTRING,
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    
    def openFileContents(filepath):
        path = fileOps.openFilePrompter()
        with open(filepath, "r") as f:
            return f.read()

    def saveFile(fileName):
        if fileName == None:
            saveAsFile()
        else:
            path = Helpers.givePath(fileName)
            with open(path, "w") as f:
                f.write(myMain.textbox.retrieveContents())

    def saveAsFile():
        path = os.path.join(TESTCWD, SAVEFOLDER, TESTSAVEASFILE)          #USER PATH INPUT  path = fileOps.saveAsFilePrompter()
        with open(path, "w") as f:
            f.write(myMain.textbox.retrieveContents())
        myMain.persistent.changeCurrFile(path)

    def saveAsFilePrompter():
        return filedialog.asksaveasfilename(initialdir = "/",
                                            title = FILEPROMPTSTRING,
                                            filetypes= (("text files","*.txt"),
                                            ("all files","*.*")))
    
    def changeFileStatsReset():
        pass
    

class Counter(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.charCount = self.charCounter()
        self.wordCount = self.wordCounter()
        self.labelSetup()
    
    def run(self, event):
        self.event = event
        self.charCount = self.charCounter()
        self.wordCount = self.wordCounter()
        self.labelUpdate()

    def charCounter(self):      # Next 3 lines from (https://www.plus2net.com/python/tkinter-text.php)
        totalChars = len(self.parent.textbox.retrieveContents())            # excluding last line break
        newlineCount = self.parent.textbox.retrieveContents().count("\n")   # number of line breaks ( except last one ) 
        visibleChars = totalChars - newlineCount    # total chars excluding line breaks
        return visibleChars
    
    def wordCounter(self):
        wordCount = len(self.parent.textbox.retrieveContents().split())
        return wordCount
    
    def labelSetup(self):
        text = tk.StringVar()
        text.set("hello world! ")
        label = tk.Label(root, textvariable = text, relief="raised")
        label.pack(side = "bottom", fill = "x")
        self.label = label
        self.labelString = text

    def labelUpdate(self):
        self.labelString.set(f"Words: {self.wordCount}. "
                             f"Characters: {self.charCount}")


class PersistenceOps(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.currDir = os.path.join(os.getcwd(), SAVEFOLDER)
        self.currFile = NOCURRFILE

    def changeCurrFile(self, newFilePath):
        self.currFile = newFilePath
    
    def changeCurrDir(self, newDirPath):
        self.currDir = newDirPath
     

class Helpers(tk.Frame):
    def givePath(fileOrDirName):
        return os.path.join(myMain.persistent.currDir, fileOrDirName)
        

# Main block
if __name__ == "__main__":
    root = tk.Tk()
    myMain = MainApplication(root)
    myMain.pack(side = "top", fill = "both", expand = True)

    root.mainloop()
