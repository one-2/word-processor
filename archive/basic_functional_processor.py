# This document was created by Stephen Elliott on 12/5/23.
# Libraries
from tkinter import *

# Constants
ROOT_TITLE = "Basic text editor"

# Main function
def main():
    global root 
    root = Tk() # Create the root window
    build_root()
    build_menus()


# Setup functions
def build_root():
    # Build the window 
    root.geometry("400x500")
    root.title(ROOT_TITLE)

    # Build the scrollbar
    scrollbar = Scrollbar(root, highlightbackground="green", troughcolor="red")
    scrollbar.pack(side = RIGHT, fill = Y)

    # Build the textbox
    textbox = Text(root, yscrollcommand = scrollbar.set)
    textbox.pack(fill = BOTH)

    scrollbar.config(command = textbox.yview)    # Configure the scrollbar

    build_menus(root)    # Build the menu
    root.mainloop()    # build the root


def build_menus(root):
    root.option_add("*tearOff", False)                  # kill the tearoff

    menubar = Menu(root)                                # create a menu for the root (IS A DEFAULT CREATED FOR YOU?)
    root.config(menu = menubar)                           # allocate the menubar to the root window

    file = Menu(menubar)                                # create a menu on the menubar called "file"
    menubar.add_cascade(label = "File", menu = file, )  # create a file tab
    file.add_command(label = "New", command = None) 
    file.add_command(label = "Open", command = None)
    file.add_command(label = "Save", command = None)

    edit = Menu(menubar)
    menubar.add_cascade(label = "Edit", menu = edit)

    test = Menu(menubar)
    menubar.add_cascade(label = "test", menu = test)
    test.add_command(label = "Print to console",
                     command = printusertexttoconsole)


# Helper functions
def printusertexttoconsole():
    # Print user text to console
    textbox = root.Text
    usertext = textbox.get("1.0", "end")
    print(usertext)



# Main block
main()
