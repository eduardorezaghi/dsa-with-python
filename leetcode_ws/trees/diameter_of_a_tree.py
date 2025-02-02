# Leetcode: 543. Diameter of Binary Tree
# link: https://leetcode.com/problems/diameter-of-binary-tree/

from aux import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.diameter = 0

        def diameter(node):
            if not node:
                return 0
            left = diameter(node.left)
            right = diameter(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1  # Return height of current subtree

        diameter(root)
        return self.diameter


if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(s.diameterOfBinaryTree(t1)) # 3
    