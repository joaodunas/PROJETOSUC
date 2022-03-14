import sys


def readInput():
    values = sys.stdin.readline().split()
    return values[0], int(values[1]), int(values[2])


class Node:

    def __init__(self, cat, value, noChild):
        self.cat = cat
        self.value = value
        self.noChild = noChild
        self.childNodes = []

    def __repr__(self):
        return str(self.cat + "(" + str(self.totalValue()) + ")")


    def totalValue(self):
        if (self.noChild == 0):
            return self.value
        else:
            val = self.value
            for child in self.childNodes:
                val += child.totalValue()
            return val




def populateTree(node):
    while len(node.childNodes) < node.noChild:
        inputRead = readInput()
        newNode = Node(inputRead[0], inputRead[1], inputRead[2])
        node.childNodes.append(newNode)
        populateTree(newNode)


def printTree(node):
    sys.stdout.write(repr(node))
    sys.stdout.write("\n")
    for child in node.childNodes:
        printTree(child)

def outln(n):
    sys.stdout.write(str(n))
    sys.stdout.write("\n")

def printTreeRightOrder(root):
    listValues = [root]

    while listValues:
        listSize = len(listValues)
        buffertotal = ""
        while listSize > 0:
            buffer = listValues.pop(0)
            buffertotal += repr(buffer) + " "
            for i in buffer.childNodes:
                listValues.append(i)

            listSize -= 1


        outln(buffertotal.rstrip())







def main():
    inputRead = readInput()
    tree = Node(inputRead[0], inputRead[1], inputRead[2])
    populateTree(tree)
    printTreeRightOrder(tree)


if __name__ == '__main__':
    main()