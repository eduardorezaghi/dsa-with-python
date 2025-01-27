from aux import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.value == data:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            current = current.next

    def __str__(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.value))
            current = current.next
            if current:
                res.append(' -> ')
            else:
                res.append(' -> None')

        return '[' + ''.join(res) + ']'

    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.prepend(0)
    dll.prepend(-1)
    dll.prepend(-2)
    dll.delete(3)
    dll.delete(0)
    print(dll)
    dll.display()

    print()
