# Leetcode 141. Linked List Cycle
# Leetcode 142. Linked List Cycle II

from aux import ListNode


def detect_cycle_set(head: ListNode) -> ListNode:
    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next

    # Time complexity: O(n), because we visit each node at most once.
    # Space complexity: O(n), because we store each node in the set.

    return None

def detect_cycle_floyd(node: ListNode) -> ListNode:
    if not node or not node.next:
        return None

    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return None

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Time complexity: O(n), because we visit each node at most twice.
    # Space complexity: O(1), because we only use two pointers.

    return slow