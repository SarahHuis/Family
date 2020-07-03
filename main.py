def add_element_dict(dict, element):
        for i in element:
            dict[len(dict)+1] = i

def create_node(name, child, parent):
    node = {"name":name, "child":child, "parent":parent}
    return node

def add_to_tree(tree, node):
    tree[len(tree)+1] = node

    
# Example
child = dict()
add_element_dict(child, ['John', "Patrick", "Jane", "Shepard"])
print(child)
parent = dict()
add_element_dict(parent, ["P1", "P2", "P3"])
print(parent)
node = {"name":"Mr Fuzzyboots", "child": child, "parent": parent}
print(node)
print(node["name"])
print(node["child"])
print(node["parent"])

