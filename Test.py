#import tkinter as tk

#window = tk.Tk()
#greeting = tk.Label(text="Python Rocks")
#greeting.pack()

#window.mainloop()


class Node:
    def __init__(self, val, name):
        self.val = val
        self.name = name
        self.prev = None
        self.next = None

first = Node('sup', 'John')
second = Node('bro', 'Mina')
first.next = second # first.next = Node('bro')
print(second.val)
print(second.name)
first.next.val = 'dog'
print(first.next.val)
print(first.next.name)
print(second.val)
print(second.name)

third = second
print(third.val)
third.val = 'horse'
print(third.val)
print(second.val)


