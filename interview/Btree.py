class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []  # key = 2*order -1
        self.child = []  # 2*order


# Tree
class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        self.order = order

    def insert(self,new_val):
        root = self.root

        # if all key is full
        if len(root.keys) == (2*self.order) - 1 :

            temp = BTreeNode()
            # make root null
            self.root = temp

            # insert root into temp's child
            temp.child.insert(0, root)

            # split children
            self.split_child(temp, 0)

            # insert after spliting nodes
            self.insert_non_full(temp, new_val)

        else:

            # if key is empty just add the node
            self.insert_non_full(root,new_val)


    def insert_non_full(self, root, new_val):

        # index of last key
        last_key_index = len(root.keys) -1

        # check if root has a child or not
        # if yes
        if root.leaf :

            # if root is leaf itself append new ele by ascending
            root.keys.append((None, None))

            # findinf best pos for new ele kind of insertion sort style
            while last_key_index>=0 and new_val[0] < root.keys[last_key_index][0]:

                # shift the last_key to last_key+1 for found perfect value for new_element
                root.keys[last_key_index + 1] = root.keys[last_key_index]
                print(root.keys)

                # decrement last_key_index
                last_key_index -= 1

            # add new val into root with last_key + 1
            # coz finding perfect place we alredy forwarded one place
            # remeber insertion sort
            root.keys[last_key_index+1] = new_val
        else:
            # if root has child 
            print("leaf -> false")
            
            # first find appropiate roots where new_val should be 
            # according to range like root : 10 20 30 , new val = 16
            # then it is between 20 and 30

            while last_key_index >= 0 and new_val[0] < root.keys[last_key_index][0]:
                print("else - while ")
                last_key_index -= 1

            last_key_index += 1

            print(last_key_index)
            print(root.child[last_key_index].keys)

            # find if proper root->child has space of keys

            # len of keys is full
            if len(root.child[last_key_index].keys) == (2 * self.order) - 1:

                # split children
                self.split_child(root, last_key_index)

                print(new_val[0], root.keys[last_key_index][0])

                # again check new_val[0] -0 (0,0) and roots last key pos.
                if new_val[0] > root.keys[last_key_index][0]:
                    print("last_key_index", last_key_index)
                    last_key_index += 1

            # recursion to insert_non_full with root child as root
            self.insert_non_full(root.child[last_key_index], new_val)


    # here first parameter is root and second is last index of key of that root
    def split_child(self, root, last_key_index):

         # oder of tree
         temp_order = self.order

         last_root_child = root.child[last_key_index]

         # new child
         temp_node = BTreeNode(last_root_child.leaf)

         root.child.insert(last_key_index + 1, temp_node)
         # insert median val to root node
         # child key : 0 1 2 3 4 with order=3
         root.keys.insert(last_key_index,last_root_child.keys[temp_order-1])

         # now divide the child keys to new child aka temp_node with median to rest of all
         temp_node.keys = last_root_child.keys[temp_order:(2*temp_order)-1]

         # now last_root child got 0 to median key
         last_root_child.keys = last_root_child.keys[0:temp_order-1]

         # if last_root_child also has child then we have to seprate it too
         if not last_root_child.leaf :

             # again same rule as above

             # new node got child after median to last
             temp_node.child = last_root_child.child[temp_order:(2*temp_order)-1]

             # last root child got 0 to median element
             last_root_child.child = last_root_child.child[0:temp_order - 1]

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])

        else:
            return self.search_key(k, self.root)


def main():
    B = BTree(3)

    for i in range(11):
        print(i,"-",2*i)
        B.insert((i, 2 * i))

    B.print_tree(B.root)

    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == '__main__':
    main()
