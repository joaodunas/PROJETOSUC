class Node:

    def __init__(self, name, ID, val):
        self.val = val
        self.name = name
        self.ID = ID
        self.next = self.prev = None

    def __str__(self):
        return "{name} {ID} {val}\n".format(name=self.name, ID=self.ID, val=self.val)


class LinkedList:

    def __init__(self):
        self.start = None

    def isInList(self, name):
        buff = self.start
        while buff is not None:
            if buff.name == name:
                return buff
            buff = buff.next
        return None

    def insert(self, name, ID, val):
        if self.isInList(name) is not None:
            print("ARTIGO JA EXISTENTE\n")
            return
        newNode = Node(name, ID, val)

        if self.start is not None:
            buff = self.start
            while buff.next is not None:
                buff = buff.next
            newNode.prev = buff
            buff.next = newNode
        else:
            self.start = newNode
        print("NOVO ARTIGO INSERIDO\n")
        return

    def printList(self):
        node = self.start
        if node is None:
            print("lista vazia\n")
        while node is not None:
            print(node)
            node = node.next

    def selfOrganize(self, node):
        if self.start is None:
            return
        elif node and node.prev is not None:

            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            node.next = self.start
            self.start.prev = node
            self.start = node
            node.prev = None


    def search(self, name):
        b = self.isInList(name)
        if b is not None:
            print(b)
            self.selfOrganize(b)
        else:
            print("ARTIGO NAO REGISTADO\n")

    def newOffer(self, name, offer):
        b = self.isInList(name)
        if b is not None:
            b.val = offer
            print("OFERTA ATUALIZADA\n")
        else:
           print("ARTIGO NAO REGISTADO\n")

    def erase(self):
        self.start = None
        print("CATALOGO APAGADO")




def main():
    lista = LinkedList()
    lista.insert("hello", 5, 5)
    lista.insert("hi", 5, 5)
    lista.insert("j", 3, 3)
    lista.printList()
    lista.search("j")
    lista.printList()









if __name__ == '__main__':
    main()
