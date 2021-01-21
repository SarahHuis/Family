import tkinter as tk
#from tkinter import *
#from tkinter.ttk import *

def add_element_dict(dict, element):
        for i in element:
            dict[len(dict)+1] = i

def create_node(name, child, parent):
    node = {"name":name, "child":child, "parent":parent}
    return node

def add_to_tree(tree, node):
    tree[len(tree)+1] = node

def handle_click():
    #if text_Name.get("1.0","end-1c") and text_Parent.get("1.0","end-1c") \
    # and text_Child.get("1.0","end-1c") is None:
    entry = create_node(text_Name.get("1.0","end-1c"), text_Child.get("1.0","end-1c").split('\n'), \
    text_Parent.get("1.0","end-1c").split('\n'))
    print(entry)
    add_to_tree(tree, entry)
    # Clear entry fields
    text_Name.delete("1.0", "end")
    text_Child.delete("1.0", "end")
    text_Parent.delete("1.0", "end")



window = tk.Tk()
tree = dict()

label_Name = tk.Label(text="Name")
text_Name = tk.Text()
label_Child = tk.Label(text="Children")
text_Child = tk.Text()
label_Parent = tk.Label(text="Parents")
text_Parent = tk.Text()
Canvas_Tree = tk.Canvas()

add_node_button = tk.Button(
    text = "New Person",
    width = 15,
    height = 3,
    command = handle_click
)

add_node_button.grid(row = 0, column = 1)
label_Name.grid(row = 1, column = 1)
text_Name.grid(row = 2, column = 1)
label_Child.grid(row = 3, column = 1)
text_Child.grid(row = 4, column = 1)
label_Parent.grid(row = 5, column = 1)
text_Parent.grid(row = 6, column = 1)
Canvas_Tree.grid(row = 1, column = 2)





window.mainloop()

































# Example
# child = dict()
# add_element_dict(child, ["John", "Patrick", "Jane", "Shepard"])
# print(child)
# parent = dict()
# add_element_dict(parent, ["P1", "P2", "P3"])
# print(parent)
# node = {"name":"Mr Fuzzyboots", "child": child, "parent": parent}
# print(node)
# print(node["name"])
# print(node["child"])
# print(node["parent"])
#create_node("Sansa Whiter")
