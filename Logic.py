# Found problem (Possibly):
# The person gets wrongly added to the wrong person. So, instead of Iris is the parent of Bob, Iris becomes parent of Iris (themselves)
# Guess as to why this happens:
# The search function tries to find the first name it comes across anywhere in the dictionary, and not just in the 'name' key.

# Trying out adding ID numbers.

# Create tree
tree = dict()
last_ID = 0

def add_element_dict(dict, element):
    for i in element:
        dict[len(dict) + 1] = i


def create_node(name, child, parent):
    global last_ID
    ID = last_ID + 1
    last_ID = ID
    ID = str(ID)
    if len(ID) < 5:
        ID = ID.zfill(5)
    else:
        print("Error in create_node. ID does not have a length between 1 and 5.")
    node = {"ID": ID, "name": name, "child": child, "parent": parent}
    return node


def add_to_tree(tree, node):
    tree[len(tree) + 1] = node


def createNewPerson(name):
    node = create_node(name, [], [])
    add_to_tree(tree, node)

# https://stackoverflow.com/questions/22162321/search-for-a-value-in-a-nested-dictionary-python
def findInTree(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value:  # found value
            return path
        elif hasattr(v, 'items'):  # v is a dict
            p = findInTree(v, value, path)  # recursive call
            if p is not None:
                return p


def addChild(parent, child):
    loc = findInTree(tree, parent)
    if not tree[loc[0]]['child']:
        tree[loc[0]]['child'] = child
    else:
        tree[loc[0]]['child'] = [tree[loc[0]]['child'], child]

def addParent(child, parent):
    loc = findInTree(tree, child)
    if not tree[loc[0]]['parent']:
        tree[loc[0]]['parent'] = parent
    else:
        tree[loc[0]]['parent'] = [tree[loc[0]]['parent'], parent]



def printTree():
    #return print(tree)
    for mainkey, key in tree.items():
        print(key)

def selectPerson():
#    global person
#    person = input("Enter Person: ")
#    return person
    person = input("Enter Person: ")
    global ID
    ID = findInTree(tree, person)
    return tree[loc[0]]['ID']

def printPerson():
    print(tree[findInTree(tree, person)[0]])
    return

def addPerson():
    createNewPerson(input("Enter Person: "))
    return

def addToPerson():
    def existingPersonChild():
        name = input("Name of person: ")
        addChild(person, name)
        addParent(name, person)
        return

    def existingPersonParent():
        name = input("Name of person: ")
        addParent(person, name)
        addChild(name, person)
        return

    def newPersonChild():
        name = input("Name of person: ")
        createNewPerson(name)
        addChild(person, name)
        addParent(name, person)
        return

    def newPersonParent():
        name = input("Name of person: ")
        createNewPerson(name)
        addParent(person, name)
        addChild(name, person)
        return

    def switch(argument):
        switcher = {
            1: existingPersonChild,
            2: existingPersonParent,
            3: newPersonChild,
            4: newPersonParent
        }
        return switcher.get(argument, lambda: "Invalid choice.")()

    print("Add person to", person)
    print("\t 1: Choose existing person to add as a child")
    print("\t 2: Choose existing person to add as a parent")
    print("\t 3: Create new person to add as a child")
    print("\t 4: Create new person to add as a parent")
    switch(int(input("Choice: ")))
    return


def exitProgram():
    global e
    e = 1
    return


def mainSwitch(argument):
    switcher = {
        1: printTree,
        2: selectPerson,
        3: printPerson,
        4: addPerson,
        5: addToPerson,
        6: exitProgram
    }
    func = switcher.get(argument, lambda: "Invalid choice.")()
    print(func)
    return func




def main():
    print("Selected person: ", person)
    print("Choose an option:")
    print("\t 1: Print the whole tree")
    print("\t 2: Select person in tree")
    print("\t 3: Print the currently selected person")
    print("\t 4: Add new person to tree")
    print("\t 5: Add person to existing person in tree")
    print("\t 6: Exit the program")
    mainSwitch(int(input("Choice: ")))




#print(tree)
#createNewPerson("Nina")
#createNewPerson("Bob")
#print(tree)
#print(findInTree(tree, "Bob")[0])
#print(tree[1]['child'])
#addChild("Nina", "Bob")
#print(tree[1]['child'])
#addChild("Nina", "Charles")
#print(tree)
#print(tree[1]['child'])
#addChild("Nina", "Dave")
#print(tree)
#print(tree[1]['child'])
#addChild("Nina", "James")
#print(tree)
#addParent("Bob", "Nina")
#print(tree)

person = []
e = 0
if __name__ == '__main__':
    while e == 0:
        main()