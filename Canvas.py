import tkinter as tk
from tkinter import *

canvas_width = 1000
canvas_height = 800
box = []

for ratio in ( 0.2, 0.35 ):
   box.append( (canvas_width * ratio,
                canvas_height * ratio,
                canvas_width * (1 - ratio),
                canvas_height * (1 - ratio) ) )

root = tk.Tk()

w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()


def onRight(*args):
    # Here we fetch our X and Y coordinates of the cursor RELATIVE to the window
    cursorx = int(root.winfo_pointerx() - root.winfo_rootx())
    cursory = int(root.winfo_pointery() - root.winfo_rooty())

    # Now we define our right click menu canvas
    onRight.menu = tk.Canvas(root, width=150, height=80, highlightbackground="gray", highlightthickness=1)
    # And here is where we use our X and Y variables, to place the menu where our cursor is,
    # That's how right click menus should be placed.
    onRight.menu.place(x=cursorx, y=cursory)
    # This is for packing our options onto the canvas, to prevent the canvas from resizing.
    # This is extremely useful if you split your program into multiple canvases or frames
    # and the pack method is forcing them to resize.
    onRight.menu.pack_propagate(0)
    # Here is our label on the right click menu for deleting a row, notice the cursor
    # value, which will give us a pointy finger when you hover over the option.
    delLabel = tk.Label(onRight.menu, text="Delete Person", cursor="hand2", anchor="w")
    delLabel.pack(side="top", padx=1, pady=1, fill="x")
    addLabel = tk.Label(onRight.menu, text="Add New Person", cursor="hand2", anchor="w")
    childLabel = tk.Label(onRight.menu, text="Add Child", cursor="hand2", anchor="w")
    parentLabel = tk.Label(onRight.menu, text="Add Parent", cursor="hand2", anchor="w")
    addLabel.pack(side="top", padx=1, pady=1, fill="x")
    childLabel.pack(side="top", padx=1, pady=1, fill="x")
    parentLabel.pack(side="top", padx=1, pady=1, fill="x")

    # This function is for removing the canvas when an option is clicked.
    def destroy():
        onRight.menu.place_forget()

    # This is the function that removes the selected item when the label is clicked.
    def delete(*args):
        selection = tree.selection()
        tree.delete(selection)
        destroy()

    delLabel.bind("<Button-1>", delete)

# This is to prevent infinite right click menus; it sees if there is an existing menu
# and removes it, bringing it out in a new position.
def preClick(*args):
    try:
        onRight.menu.place_forget()
        onRight()
    except Exception:
        onRight()

# Hide menu when left clicking
def onLeft(*args):
    try:
        onRight.menu.place_forget()
    except Exception:
        pass


# Bind our functions to the Treeview.
w.bind("<Button-3>", preClick)
w.bind("<Button-1>", onLeft)



root.mainloop()