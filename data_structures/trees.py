from collections import deque
from aux import TreeNode


def preorder_traversal(node):
    if node is None:
        return
    print(node.value)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value)

def bfs_traversal(node):
    if node is None:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Preorder traversal:")
    preorder_traversal(root)
    print("Inorder traversal:")
    inorder_traversal(root)
    print("Postorder traversal:")
    postorder_traversal(root)
    print("BFS traversal:")
    bfs_traversal(root)