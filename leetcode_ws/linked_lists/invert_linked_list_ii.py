# Leetcode: 92. Reverse Linked List II
# link: https://leetcode.com/problems/reverse-linked-list-ii/

from aux import ListNode


def invert_linked_list_ii(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head

    # always create a dummy node to handle edge cases:
        # 1. when the head is the node to be reversed
        # 2. when the head is not the node to be reversed
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # more the pointer to the node before the start of the sublist we're reversing.
    for _ in range(left - 1):
        prev = prev.next



    current = prev.next
    # Now that we're in the position to reverse the sublist, we can use the same approach as reversing a linked list, which is:
        # 1. keep track of the next node (next_node, in this case)
        # 2. reverse the current node (current.next = prev.next)
        # 3. move the pointers to the next node (prev.next = next_node)

    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    # return the head of the linked list (pointer to the dummy node)
    return dummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    head = invert_linked_list_ii(head, 2, 4)
    print(head)