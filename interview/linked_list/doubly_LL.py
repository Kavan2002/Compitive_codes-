class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None

    # add node to front
    def push(self, NewVal):

        new_node = Node(data=NewVal)

        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    # insert node after certain node
    def InsertAfter(self,prevNode,newVal):

        if prevNode is None:
            print("prev node doesn't exist...")
            return

        new_node = Node(data=newVal)

        #  Make next of new node as next of prev_node
        new_node.next = prevNode.next

        #  Make the next of prev_node as new_node
        prevNode.next= new_node

        #  Make previous node as prev of new_node
        new_node.prev = prevNode

        #  Change previous of new_node's next node */
        if new_node.next is not None:
            new_node.next.prev = new_node

    # insert at last
    def InsertEnd(self,newVal):

        new_node = Node(newVal)

        last = self.head

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node

        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def listprint(self, node):
        while node is not None:
            print(node.data,"-->",end=""),
            last = node
            node = node.next
        print("")

if __name__ == '__main__':
    dll = doubly_linked_list()

    dll.push(87)
    dll.listprint(dll.head)

    dll.push(56)
    dll.listprint(dll.head)

    dll.InsertEnd(23)
    dll.listprint(dll.head)

    dll.InsertAfter(dll.head.next,45)
    dll.listprint(dll.head)