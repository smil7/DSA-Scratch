class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class QueuesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if not self.first:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1


    def is_empty(self):
        if self.length == 0:
            return True
        return False

### Testing
# queue_1 = QueuesLinkedList()
# queue_1.enqueue("Osama")
# queue_1.enqueue("Memo")
# queue_1.enqueue("Toty")
# queue_1.enqueue("Ahmed")
# print(queue_1.peek())
# print(queue_1.last.data)
# print(queue_1.length)
# print("====================================================")
# queue_1.dequeue()
# print(f"After dequeueing {queue_1.peek()}")
# queue_1.dequeue()
# print(f"After dequeueing {queue_1.peek()}")
# queue_1.dequeue()
# print(f"After dequeueing {queue_1.peek()}")
# print(queue_1.dequeue())
# print(queue_1.length)