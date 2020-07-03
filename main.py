def add_element_dict(dict, element):
    if any(dict) is False:
        dict[1] = element
    else:
        for i in element:
            dict[len(dict)+1] = i

class Node:
    def __init__(self, data, child, parent): # Data is the name of the person
        self.data = data
        self.child = child
        self.parent = parent

    def __repr__(self):
        return self.data



""">>> llist = LinkedList()
>>> llist
None

>>> first_node = Node("a")
>>> llist.head = first_node
>>> llist
a -> None

>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist
a -> b -> c -> None"""
