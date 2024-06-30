# This file was written by Stephen Elliott on 24/4/23.
from tkinter import *

# Create a root widget
## Creates a graphical window with the title bar, minimize, maximize and close buttons.
root = Tk()

# Create a label widget inside the root widget
## Displays text
l1 = Label(root, text="Hello world!")

# Call the pack method on the label
## This tells the geometry manager to size the label to fit the given text and fit into a given row or column.
l1.pack()

# Call the mainloop method on the root
## Instructs Python to take all the widgets and objects we created, render them on our screen, and respond to any interactions.
root.mainloop()
