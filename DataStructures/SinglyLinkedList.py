class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.next = new_node
        self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        position = 0
        new_node = Node(data)
        current_node = self.head
        while current_node and position < index - 1:
            current_node = current_node.next
            position += 1

        if not current_node:
            print("Ошибка: Индекс выходит за пределы списка")
            return

        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
