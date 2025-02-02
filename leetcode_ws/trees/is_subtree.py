# Leetcode 572. Subtree of Another Tree
# link: https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def is_same_tree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        if root is None:
            return False

        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)