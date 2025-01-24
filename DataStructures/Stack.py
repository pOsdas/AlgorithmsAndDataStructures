class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.min_stack = []

    def push(self, item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
            return

        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")

        data = self.top.data
        self.top = self.top.next

        if data == self.min_stack[-1]:
            self.min_stack.pop()

        return data

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data

    def get_min(self):
        if self.top is None:
            raise Exception("Stack is empty")

        return self.min_stack[-1]

    def print_stack(self):
        if self.top is None:
            raise Exception("Stack is empty")

        current = self.top
        while current:
            print(current.data, end="")
            if current.next:
                print(" <- ", end="")
            current = current.next
        print()
