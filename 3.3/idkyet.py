class Node:
    def __init__(self, username, ccnumber, expDate):
        self.username = username
        self.ccs = [ccnumber]
        self.expDate = expDate
        self.leftSon = None
        self.rightSon = None
        self.h = 0

    def addCard(self, card):
        self.ccs.append(card)


class AVLtree:

    def insert(self, node, username, ccnumber, expDate):
        if node is None:
            return Node(username, ccnumber, expDate)

        elif username < node.username:
            node.leftSon = self.insert(node.leftSon, username, ccnumber, expDate)
        else:
            node.rightSon = self.insert(node.rightSon, username, ccnumber, expDate)

        i = self.balance(node)

        if i > 1 and username < node.leftSon.username:
            return self.rotateRight(node)


    def balance(self, node):
        if node is None:
            return 0
        else:
            return node.leftSon.h - node.rightSon.h

    def rotateRight(self, node):
        nodeRSon = node.rightSon
        nodeRLGSon = nodeRSon.leftSon

        nodeRSon.leftSon = node
        node.rightSon = nodeRLGSon

        node.h = max(node.leftSon.h, node.rightSon.h)
        nodeRSon = max(nodeRSon.rightSon.h, nodeRSon.leftSon.h)

        return nodeRSon

    def rotateLeft(self, node):
