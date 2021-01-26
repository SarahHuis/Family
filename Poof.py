class Node:
    def __init__(self, ID, name, child, parent):
        self.ID = ID
        self.name = name
        self.child = None
        self.parent = None

    def __repr__(self):
        return "ID: " + str(self.ID) + "\tName: " + str(self.name) + "\t Children: " + str(self.child) + "\t Parents: " + str(self.parent)


# Create tree
tree = dict()
last_ID = 0

def createNewPerson(name):
    global last_ID
    ID = last_ID + 1
    last_ID = ID
    tree[str(ID).zfill(5)+name.replace(" ", "")] = Node(str(ID).zfill(5), name, None, None)

def printTree():
    for key, node in tree.items():
        print(key, "\t", node)

def findAllInTree(search):
    return [value for key, value in tree.items() if search.replace(" ", "").lower() in key.lower()]

def printFound(found):
    if not found:
        print("None found. Try another name.")
    else:
        for node in found:
            print("name: ", node.name, "\t ID: ", node.ID)

def selectFound(found):
    if not found:
        print("None found. Try another name.")
    else:
        print("Select the correct person number: ")
        for idx, node in enumerate(found):
            print(idx+1, "\t name: ", node.name, "\t ID: ", node.ID)
    return found[int(input("Select: "))-1]

def selectPerson():
    global person
    person = selectFound(findAllInTree(input("Enter person: ")))
    return

def printPerson():
    print(person)
    return

def addPerson():
    createNewPerson(input("Enter person: "))
    return

def addChild(child):
    if not person.child:
        person.child = child.ID + child.name
        if not child.parent:
            child.parent = person.ID + person.name
        else:
            child.parent = child.parent + ", " + person.ID + person.name
    else:
        person.child = person.child + ", " + child.ID + child.name
        if not child.parent:
            child.parent = person.ID + person.name
        else:
            child.parent = child.parent + ", " + person.ID + person.name
    return

def addParent(parent):
    if not person.parent:
        person.parent = parent.ID + parent.name
        if not parent.child:
            parent.child = person.ID + person.name
        else:
            parent.child = parent.child + ", " + person.ID + person.name
    else:
        person.parent = person.parent + ", " + parent.ID + parent.name
        if not parent.child:
            parent.child = person.ID + person.name
        else:
            parent.child = parent.child + ", " + person.ID + person.name
    return

def addToPerson():
    def existingPersonChild():      # Add an existing person as a child to another person, who will be the parent
        addChild(selectFound(findAllInTree(input("Name of person: "))))
        return

    def existingPersonParent():
        addParent(selectFound(findAllInTree(input("Name of person: "))))
        return

    def newPersonChild():
        name = input("Enter person: ")
        createNewPerson(name)
        addChild(findAllInTree(name)[0])
        return

    def newPersonParent():
        name = input("Enter person: ")
        createNewPerson(name)
        addParent(findAllInTree(name)[0])
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


person = []
e = 0
if __name__ == '__main__':
    while e == 0:
        main()