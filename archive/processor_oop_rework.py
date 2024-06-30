# This document was created by Stephen Elliott on 12/5/23.
# Libraries
import tkinter as tk
from datetime import datetime
import os

# Constants
ROOT_TITLE = "Test title: Basic text editor"
SAVEFOLDERNAME = "save_folder"




# Classes
class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("400x500")
        self.parent.title(ROOT_TITLE)

        self.scrollbar = ScrollBar()
        self.textbox = TextBox()
        self.menus = Menus(self)

        self.persistent = PersistenceOps(self)  ### myMain.persistent


class ScrollBar(tk.Frame):
    def __init__(self):     # Build the scrollbar
        self.scroll = tk.Scrollbar(root)
        self.scroll.pack(side = "right", fill = "y")

        # self.config(command = textbox.yview)    # Configure the scrollbar


class TextBox(tk.Frame):
    def __init__(self):     # Build the textbox
        self.box = tk.Text(root)                # yscrollcommand = scrollbar.set)
        self.box.pack(fill = "both")


    def retrieveInput(self):    # retrieve text from the textbox
        return self.box.get("1.0", "end-1c")
    

    def printToConsole(self):   # print user text to console
        print(self.retrieveInput())


class Menus(tk.Frame):
    def __init__(self, parent): # build the menus
        self.parent = parent

        root.option_add("*tearOff", False)                  # kill the tearoff
        self.menubar = tk.Menu(root)                        # create a menu for the root (IS A DEFAULT CREATED FOR YOU?)
        root.config(menu = self.menubar)                    # allocate the menubar to the root window

        Menus.fileMenu(self, self.parent)                                    # create the desired menus
        Menus.editMenu(self)
        Menus.testMenu(self, self.parent)


    def fileMenu(self, parent):
        self.file = tk.Menu(self.menubar)                           # create a menu object on the menubar called "file"
        self.menubar.add_cascade(label = "File", menu = self.file)  # create a file tab in the menu object

        self.file.add_command(label = "New",  command = lambda: fileOps.newFile(parent))        # add several commands to the file tab
        self.file.add_command(label = "Open", command = lambda: fileOps.openFile)
        self.file.add_command(label = "Save", command = lambda: fileOps.saveFile(myMain.persistent.currFile))

    
    
    def editMenu(self):
        self.edit = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = "Edit", menu = self.edit)


    def testMenu(self, parent):
        self.test = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = "test", menu = self.test)
        self.test.add_command(label = "Print to console", command = parent.textbox.printToConsole)               # command = printusertexttoconsole)


class fileOps(tk.Frame):
    def newFile(textBoxParent):      # create a new file to save to
                                                                                    # TODO Open a popup requesting user input
        fileName = datetime.now().strftime("%d-%m-%Y-%H-%M-%S.txt")
        path = Helpers.givePath(fileName)
        with open(path, "x") as f:
            f.write(myMain.textbox.retrieveInput())
        myMain.persistent.changeCurrFile(path)


    def openFile():
        pass


    def saveFile(fileName):
        path = Helpers.givePath(fileName)
        with open(path, "w") as f:
            f.write(myMain.textbox.retrieveInput())
        myMain.persistent.changeCurrFile(path)
    

class PersistenceOps(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.currDir = os.path.join(os.getcwd(), SAVEFOLDERNAME)
        self.currFile = "temp.txt"

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
