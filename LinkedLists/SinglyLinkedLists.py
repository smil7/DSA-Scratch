from contextlib import nullcontext


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, data):
        if index >= self.get_length():
            self.insert_at_end(data)
        elif index == 0:
            self.insert_at_begin(data)
        else:
            new_node = Node(data)
            pointer = self.traverse_to_index(index)
            new_node.next = pointer.next
            pointer.next = new_node
            self.length += 1

    def traverse_to_index(self, index):
        i = 0
        pointer = self.head
        while i < (index - 1):
            pointer = pointer.next
            i += 1
        return pointer

    def remove(self, index):
        if index >= self.get_length():
            self.tail = self.head
            self.tail = self.traverse_to_index(self.get_length()-1)
            self.tail.next = None
            print("tail data ", self.tail.data)
        elif index == 0:
            self.head = self.head.next
        else:
            pointer = self.traverse_to_index(index)
            pointer.next = pointer.next.next
        self.length -= 1

    def print_ll(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next
        print("head data ", self.head.data)
        print("tail data ", self.tail.data)

    def get_length(self):
        return self.length

    def reverse(self):
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = self.head.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

# ## Testing
# linked_list1 = SinglyLinkedLists()
# linked_list1.insert_at_begin(3)
# linked_list1.insert_at_begin(5)
# linked_list1.insert_at_begin(4)
# linked_list1.insert_at_begin(41)
# linked_list1.insert(2, 6)
# linked_list1.remove(3)
# linked_list1.print_ll()
# linked_list1.reverse()
# linked_list1.print_ll()
# print(linked_list1.get_length())
# print("=========================================")
# linked_list2 = SinglyLinkedLists()
# linked_list2.insert_at_end(12)
# linked_list2.insert_at_end(15)
# linked_list2.insert_at_end(31)
# linked_list2.insert_at_end(21)
# linked_list2.insert(3, 11)
# linked_list2.remove(0)
# linked_list2.remove(4)
# linked_list2.print_ll()
# linked_list2.reverse()
# linked_list2.print_ll()
# print(linked_list2.get_length())