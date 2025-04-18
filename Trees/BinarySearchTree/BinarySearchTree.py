class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return new_node
                    current_node = current_node.left
                elif value > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return new_node
                    current_node = current_node.right
                else:
                    return 'The Node is already stored'

    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root
        while current_node:
            if value < current_node.data:
                current_node = current_node.left
            elif value > current_node.data:
                current_node = current_node.right
            else:
                return current_node
        return False

    def remove(self, value):
        if self.root is None:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            else:
                # Option 1: No right child
                if current_node.right is None:
                    if parent_node is None: # we are still in the root node
                        self.root = current_node.left
                    else:
                        # if the parent > current, then make the left child of current a left child of parent
                        if current_node.data < parent_node.data:
                            parent_node.left = current_node.left

                        # if the parent < current, then make the left child of current the right child of parent
                        elif current_node.data > parent_node.data:
                            parent_node.right = current_node.left

                # Option 2: Right parent doesn't have a left child
                elif current_node.right.left is None:
                    if parent_node is None: # we are still in the root node
                        self.root = current_node.left
                    else:
                        current_node.right.left = current_node.left

                        # if the parent > current, then make the right child of current a left child of parent
                        if current_node.data < parent_node.data:
                            parent_node.left = current_node.right

                        # if the parent < current, then make the right child of current the right child of parent
                        elif current_node.data > parent_node.data:
                            parent_node.right = current_node.right

                # Option 3: Right child that has a left child (Revisit this part for "comprehending")
                else:
                    # find the right's child left most child
                    left_most = current_node.right.left
                    left_most_parent = current_node.right

                    # loop until you find the left most child
                    while left_most.left is not None:
                        left_most_parent = left_most
                        left_most_parent = left_most.left

                    # parent's left subtree is now left_most's right subtree
                    left_most_parent.left = left_most.right
                    left_most.left = current_node.left
                    left_most.right = current_node.right

                    if parent_node is None:
                        self.root = left_most
                    else:
                        if current_node.data < parent_node.data:
                            parent_node.left = left_most
                        elif current_node.data > parent_node.data:
                            parent_node.right = left_most
            return True

    # def traverse(self, node):
    #     tree = node
    #     if node.left is None:
    #         tree.left = None
    #     else:
    #         self.traverse(node.left)
    #         # print(f"The current left node is {tree.data}")
    #
    #     if node.right is None:
    #         tree.right = None
    #     else:
    #         self.traverse(node.right)
    #         # print(f"The current right node is {tree.data}")
    #
    #     return tree

tree_1 = BinarySearchTree()
tree_1.insert(9)
tree_1.insert(4)
tree_1.insert(6)
tree_1.insert(20)
tree_1.insert(170)
tree_1.insert(15)
tree_1.insert(1)
print(vars(tree_1.lookup(170))) # This will return false if the variable returned is not an object
#print(vars(tree_1.traverse(tree_1.root)))