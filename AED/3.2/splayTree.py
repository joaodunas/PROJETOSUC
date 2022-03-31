from sys import stdin, stdout
from time import perf_counter


def readInput():
    values = stdin.readline().split()
    return values

class Node:
    def __init__(self, name, h4sh, val):
        self.val = val
        self.name = name
        self.h4sh = h4sh
        self.right = None
        self.left = None

    def __str__(self):
        return self.name + " " + str(self.h4sh) + " " + str(self.val)


class SplayTree:

    def insert(self, node, newNode):
        if not node:
            #stdout.write("NOVO ARTIGO INSERIDO\n")
            return newNode

        node = self.splaying(node, newNode.name)

        if node is not None:
            if node.name == newNode.name:
                #stdout.write("ARTIGO JA EXISTENTE\n")
                return node

            elif node.name > newNode.name:
                newNode.right = node
                newNode.left = node.left
                node.left = None

            else:
                newNode.left = node
                newNode.right = node.right
                node.right = None
            #stdout.write("NOVO ARTIGO INSERIDO\n")
        return newNode

    def splaying(self, node, newName):
        if not node or node.name == newName:
            return node

        if node.name > newName:
            if not node.left:
                return node

            if node.left.name > newName:
                node.left.left = self.splaying(node.left.left, newName)
                node = self.zig(node)

            elif node.left.name < newName:
                node.left.right = self.splaying(node.left.right, newName)
                if node.left.right is not None:
                    node.left = self.zag(node.left)
            if not node.left:
                return node
            else:
                return self.zig(node)

        else:  # contrario, esta do lado direito
            if not node.right:
                return node

            if node.right.name < newName:
                node.right.right = self.splaying(node.right.right, newName)
                node = self.zag(node)

            elif node.right.name > newName:
                node.right.left = self.splaying(node.right.left, newName)
                if node.right.left is not None:
                    node.right = self.zig(node.right)
            if not node.right:
                return node
            else:
                return self.zag(node)

    def search(self, node, name):
        if not node:
            #stdout.write("NODE NULL\n")
            return
        node = self.splaying(node, name)
        return node

    def zig(self, node):  # rightRotation
        k2 = node.left
        node.left = k2.right
        k2.right = node
        return k2

    def zag(self, node):  # leftRotation
        k2 = node.right
        node.right = k2.left
        k2.left = node
        return k2

    def printTree(self, node):
        if node is None:
            return
        else:
            self.printTree(node.left)

            #stdout.write(str(node) + "\n")

            self.printTree(node.right)



def main():
    f = open("resultsMode1.txt", "a")
    for i in range(3):
        stdin = open("Modo1.txt", "r")
        a = SplayTree()
        arvore = None
        inp = stdin.readline().rstrip().split()
        inputTime = 0
        start = perf_counter()
        while inp[0] != "FIM":
            if inp[0] == "ARTIGO":
                arvore = a.insert(arvore, Node(inp[1], inp[2], inp[3]))
            elif inp[0] == "CONSULTA":
                arvore = a.search(arvore, inp[1])
                if arvore.name == inp[1]:
                    #stdout.write(str(arvore) + "\n")
                    #stdout.write("FIM\n")
                    pass
                else:
                    #stdout.write("ARTIGO NAO REGISTADO\n")
                    pass
            elif inp[0] == "LISTAGEM":
                a.printTree(arvore)
                #stdout.write("FIM\n")
            elif inp[0] == "APAGA":
                #stdout.write("CATALOGO APAGADO\n")
                arvore = None
            elif inp[0] == "OFERTA":
                arvore = a.search(arvore, inp[1])
                if arvore.name == inp[1]:
                    arvore.val = inp[2]
                    pass
                    #stdout.write("OFERTA ATUALIZADA\n")
                else:
                    #stdout.write("ARTIGO NAO REGISTADO\n")
                    pass
            else:
                #stdout.write("INVALID INPUT\n")
                pass
            inputTime -= perf_counter()
            inp = stdin.readline().rstrip().split()
            inputTime += perf_counter()
        end = perf_counter()
        f.write(str(end-start-inputTime)+ "\n")


if __name__ == '__main__':
    main()
