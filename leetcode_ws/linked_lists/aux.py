# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        res = []
        while current:
            res.append(str(current.val))
            current = current.next
            if current:
                res.append(' -> ')
            else:
                res.append(' -> None')

        return '[' + ''.join(res) + ']'