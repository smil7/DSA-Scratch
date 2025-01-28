class StacksArray:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[len(self.data) - 1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

### Testing
# stack_1 = StacksArray()
# stack_1.push("google")
# stack_1.push("udemy")
# stack_1.push("stack overflow")
# print(stack_1.data)
# print(stack_1.peek())
# stack_1.pop()
# print(stack_1.peek())
# stack_1.pop()
# print(stack_1.peek())
# print(stack_1.data)
# stack_1.pop()
# print(stack_1.data)