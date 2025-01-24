import SinglyLinkedLists as sll

class DoublyNode(sll.Node):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None

class DoublyLinkedLists(sll.SinglyLinkedLists):
    def insert_at_begin(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail # pointing to the previous last node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, data):
        if index >= self.get_length()-1:
            self.insert_at_end(data)
        elif index == 0:
            self.insert_at_begin(data)
        else:
            new_node = DoublyNode(data)
            pointer = self.traverse_to_index(index)
            follower = pointer.next
            pointer.next = new_node
            new_node.next = follower
            new_node.previous = pointer # pointing to the previous node
            follower.previous = new_node

            self.length += 1

    def remove(self, index):
        if index >= self.get_length()-1:
            pointer = self.tail
            pointer.previous = None # deleting the previous last node
            self.tail = self.head
            self.tail = self.traverse_to_index(self.get_length()-1)
            self.tail.next = None
            print("tail data ", self.tail.data)
        elif index == 0:
            pointer = self.head.next
            self.head.next = None
            self.head = pointer
            self.head.previous = None
        else:
            pointer = self.traverse_to_index(index)
            deleted_node = pointer.next
            pointer.next = pointer.next.next
            deleted_node.previous = None
            deleted_node.next = None
        self.length -= 1

### Testing
# doubly_ll1 = DoublyLinkedLists()
# doubly_ll1.insert_at_begin(3)
# doubly_ll1.insert_at_begin(5)
# doubly_ll1.insert_at_end(4)
# doubly_ll1.insert_at_begin(41)
# doubly_ll1.insert(2, 6)
# doubly_ll1.remove(3)
# doubly_ll1.remove(3)
# doubly_ll1.print_ll()
# print(doubly_ll1.get_length())