import tkinter as tk

def add_element_dict(dict, element):
        for i in element:
            dict[len(dict)+1] = i

def create_node(name, child, parent):
    node = {"name":name, "child":child, "parent":parent}
    return node

def add_to_tree(tree, node):
    tree[len(tree)+1] = node

def handle_click():
    #if text_Name.get("1.0","end-1c") and text_Parent.get("1.0","end-1c") and text_Child.get("1.0","end-1c") is None:
    entry = create_node(text_Name.get("1.0","end-1c"), text_Child.get("1.0","end-1c"), text_Parent.get("1.0","end-1c"))
    print(entry)

window = tk.Tk()
add_node_button = tk.Button(
    text = "New Person",
    width = 15,
    height = 3,
    command = handle_click
)

label_Name = tk.Label(text="Name")
text_Name = tk.Text()
label_Child = tk.Label(text="Children")
text_Child = tk.Text()
label_Parent = tk.Label(text="Parents")
text_Parent = tk.Text()


add_node_button.pack()
label_Name.pack()
text_Name.pack()
label_Child.pack()
text_Child.pack()
label_Parent.pack()
text_Parent.pack()





#add_node_button.bind("<Button-1>", handle_click())


window.mainloop()


































# Example
child = dict()
add_element_dict(child, ["John", "Patrick", "Jane", "Shepard"])
print(child)
parent = dict()
add_element_dict(parent, ["P1", "P2", "P3"])
print(parent)
node = {"name":"Mr Fuzzyboots", "child": child, "parent": parent}
print(node)
print(node["name"])
print(node["child"])
print(node["parent"])
#create_node("Sansa Whiter")
