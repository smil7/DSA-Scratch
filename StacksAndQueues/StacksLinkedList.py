class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class StacksLinkedList:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1

    def pop(self):
        if not self.top:
            return None

        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1

    def print(self):
        pointer = self.top

        print("Stack data: ")
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

    def is_empty(self):
        if self.length == 0:
            return True
        return False

### Testing
# stack_1 = StacksLinkedList()
# stack_1.push("Google")
# stack_1.push("Udemy")
# stack_1.push("Stack Overflow")
# stack_1.print()
# print(stack_1.length)
# print(f"Top of the Stack: {stack_1.peek()}")
# print("=========================================================")
# print("Pop some items")
# stack_1.pop()
# stack_1.pop()
# stack_1.pop()
# print(stack_1.length)
