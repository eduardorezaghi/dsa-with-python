# LeetCode: 206. Reverse Linked List


from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: 'Node' = None

class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = head

    def from_list(self, lst: list[int]):
        if not lst:
            return None

        self.head = Node(lst[0])
        current = self.head
        for val in lst[1:]:
            current.next = Node(val)
            current = current.next

        self.tail = current

    def reverse(self):
        def _reverse_recursive(current, previous):
            if not current:
                return previous
            next_node = current.next
            current.next = previous
            return _reverse_recursive(next_node, current)

        self.tail = self.head
        self.head = _reverse_recursive(self.head, None)


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
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.from_list([1,2,3,4,5])
    print(ll)
    print(ll.head.value)
    print(ll.tail.value)
    ll.reverse()
    print(ll)