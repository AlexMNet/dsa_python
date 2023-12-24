# Full Binary Tree: is a tree in which all nodes are either pointing to two or zero nodes
#     4
#   /  \
#   3  23
# /  \
# 1  7
#
# Perfect Binary Tree: A tree which is full and symmetrical

# Binary Search Tree
# If number is greater than head node it goes on the right
# If number is less than head node it goes on the left


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # This is an explicit way to code this but not necessary
        # If root is None the while loop won't run and contains will return false
        # Thus this code is redudant
        # if self.root is None:
        #     return False

        temp = self.root

        while temp:
            if value == temp.value:
                return True

            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.root.value)
print(my_tree.contains(17))
