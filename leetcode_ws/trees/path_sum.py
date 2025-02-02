# Leetcode 112. Path Sum
# link: https://leetcode.com/problems/path-sum/

from collections import deque
from aux import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        queue = deque()
        
        if root is None:
            return False

        queue.append((root, root.val))

        while queue:
            node, sum_ = queue.popleft()

            if node.left is None and node.right is None and sum_ == targetSum:
                return True

            if node.left:
                queue.append((node.left, sum_ + node.left.val))
            if node.right:
                queue.append((node.right, sum_ + node.right.val))

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    print(Solution().hasPathSum(root, targetSum)) # True

    root = TreeNode(1)
    root.left = TreeNode(2)
    targetSum = 1
    print(Solution().hasPathSum(root, targetSum)) # False