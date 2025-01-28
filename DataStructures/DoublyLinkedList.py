class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
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
        new_node.prev = current_node

        if current_node.next:
            current_node.next.prev = new_node

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
        new_node.prev = current_node.next

    def delete_at_index(self, index):
        if self.head is None:
            print("Ошибка: Список пуст")
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        current_node = self.head
        position = 0

        while current_node and position < index:
            current_node = current_node.next
            position += 1

        if not current_node:
            print("Ошибка: Индекс выходит за пределы списка")
            return

        # Если элемент не последний
        if current_node.next:
            current_node.next.prev = current_node.prev

        # Если элемент не первый
        if current_node.prev:
            current_node.prev.next = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="")
            if current_node.next:
                print(" <-> ", end="")
            current_node = current_node.next
        print()

    def transfer_from_list_to_linked_list(self, list_data):
        if not list_data:
            self.head = None
            return

        self.head = Node(list_data[0])
        current_node = self.head

        for i in list_data[1:]:
            new_node = Node(i)
            current_node.next = new_node
            new_node.prev = current_node
            current_node = current_node.next
