from sys import stdout
from sys import stdin


def readInput():
    values = stdin.readline().split()
    return values


class Node:
    def __init__(self, username, ccnumber, expDate):
        self.username = username
        self.ccs = {ccnumber: expDate}
        self.left = None
        self.right = None
        self.h = 0

    def __str__(self):
        string = "{username} {CCs}".format(username=self.username, CCs=sorted(self.ccs.items()))
        return string.replace(",", "").replace("[", "").replace("(", "").replace(")", "").replace("]", "").replace("'", "")

    def con(self):
        for i in sorted(self.ccs.items()):
            line = ""
            for h in i:
                line += str(h) + " "
            stdout.write(line.rstrip() + "\n")


class AVLtree:

    def insert(self, node, username, ccnumber, expDate):
        buff = self.search(node, username)
        if node is None:
            stdout.write("NOVO UTILIZADOR CRIADO\n")
            return Node(username, ccnumber, expDate)

        if buff is not None:
            if ccnumber in buff.ccs:
                buff.ccs[ccnumber] = expDate
                stdout.write("CARTAO ATUALIZADO\n")
            else:
                buff.ccs[ccnumber] = expDate
                stdout.write("NOVO CARTAO INSERIDO\n")

        elif username < node.username:
            node.left = self.insert(node.left, username, ccnumber, expDate)
        else:
            node.right = self.insert(node.right, username, ccnumber, expDate)

        i = self.balance(node)

        if i > 1 and username < node.left.username:
            return self.rotateRight(node)

        elif i > 1 and username > node.left.username:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        elif i < -1 and username > node.right.username:
            return self.rotateLeft(node)

        elif i < -1 and username < node.right.username:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.h

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)

    def rotateRight(self, node):
        k2 = node.right
        node.right = k2.left
        k2.left = node

        node.h = max(self.height(node.left), self.height(node.right))
        k2.h = max(self.height(k2.left), self.height(k2.right))

        return k2

    def rotateLeft(self, node):
        k2 = node.left
        node.left = k2.right
        k2.right = node

        node.h = max(self.height(node.left), self.height(node.right))
        k2.h = max(self.height(k2.left), self.height(k2.right))

        return k2

    def search(self, node, username):
        if node is None:
            return None

        elif (node.username == username):
            return node

        elif (node.username < username):
            return self.search(node.right, username)

        else:
            return self.search(node.left, username)

    def delete(self, node):
        node = None
        stdout.write("LISTAGEM APAGADA\n")
        return node

    def printTree(self, node):
        if node is None:
            return
        else:
            self.printTree(node.left)

            stdout.write(str(node) + "\n")

            self.printTree(node.right)

    def printNode(self, node, username):
        buff = self.search(node, username)
        if node is None:
            return
        if buff is None:
            stdout.write("NAO ENCONTRADO\n")
            return
        else:
            buff.con()
            stdout.write("FIM\n")


def main():
    a = AVLtree()
    arvore = None
    inp = readInput()
    while inp[0] != "FIM":
        if inp[0] == "ACRESCENTA":
            arvore = a.insert(arvore, inp[1], inp[2], inp[3])
        elif inp[0] == "CONSULTA":
            a.printNode(arvore, inp[1])
        elif inp[0] == "LISTAGEM":
            a.printTree(arvore)
            stdout.write("FIM\n")
        elif inp[0] == "APAGA":
            arvore = a.delete(arvore)
        else:
            stdout.write("INVALID INPUT\n")
        inp = readInput()


if __name__ == '__main__':
    main()
