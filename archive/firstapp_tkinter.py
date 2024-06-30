# This file was written by Stephen Elliott on 24/4/23.

# Libraries
from tkinter import *

# Create the root window
root = Tk()

# Define the root window's title and size
root.title("My first tkinter GUI")
root.geometry("700x300")    # width * height

# Create a menu
menu = Menu(root)   ## Create a menu bar in the root window
menu_geom = Menu(menu)  ## Add the first item to the menu geometry
menu_geom.add_command(label="New")  ## Add a command with a label to the first item
menu.add_cascade(label="File", menu=menu_geom)   ## Add an item to the menu

# Assign the menu to the root window
root.config(menu=menu)

# Create a label and define its location
text1 = Label(root, text="Welcome to my first tkinter GUI.")
text1.grid()    # Note: text1.place() doesn't render any text

# Create a user entry field and add it to the grid
usertext = Entry(root, width=10)
usertext.grid(column=1, row=0)

# Define a function to display user text when a button is clicked
def clicked():
    res = "You wrote " + usertext.get()
    text1.configure(text=res)

# Create a button widget with green text inside it
btn = Button(root,
             text="Click me",
             fg="red",
             command=clicked)

# Put the button in the grid
btn.grid(column=2,  # Indexing starts at 0
         row=0)

# Render the instructions.
root.mainloop()