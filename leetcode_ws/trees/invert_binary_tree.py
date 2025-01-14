class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def from_list(lst: list[int]):
        if not lst:
            return None

        root = TreeNode(lst[0])
        queue = [root]
        i = 1
        while queue and i < len(lst):
            node = queue.pop(0)
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root

    def list_repr(self):
        return [self.val, self.left.list_repr() if self.left else None, self.right.list_repr() if self.right else None]

def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root



if __name__ == '__main__':
    tree = TreeNode.from_list([4,2,7,1,3,6,9])
    print(tree.list_repr())
    tree = invert_tree(tree)
    print(tree.list_repr())