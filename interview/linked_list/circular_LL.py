
class circular_Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class circular_linkedList:
    def __init__(self):
        self.head = None

    def add_last(self,data):

        new_node = circular_Node(data)
        new_node.next = self.head

        temp = self.head


        if self.head is not None:

            while temp.next != self.head :
                temp = temp.next

            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node

    def print_it(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d --> " % (temp.val),end=""),
                temp = temp.next
                if (temp == self.head):
                    print('%d'%(temp.val))
                    break


if __name__ == '__main__':

    cll = circular_linkedList()
    cll.add_last(56)
    cll.add_last(87)
    cll.add_last(27)
    cll.add_last(78)

    cll.print_it()