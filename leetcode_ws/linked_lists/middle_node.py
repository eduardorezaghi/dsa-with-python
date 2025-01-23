import math
from aux import ListNode


def middle_node(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
        
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


if __name__ == '__main__':
    # Example 1:
    # Input: head = [1,2,3,4,5]
    # Output: [3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid_n = middle_node(head)  # [3,4,5]
    print(mid_n)

    # Example 2:
    # Input: head = [1,2,3,4,5,6]
    # Output: [4,5,6]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(middle_node(head))  # [4,5,6]