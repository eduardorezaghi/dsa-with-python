# Leetcode 102. Binary Tree Level Order Traversal
# link: https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

from aux import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
        levels = []

        while queue:
            num_levels = len(queue)
            level = []

            for i in range(num_levels):  # Process all nodes at the current level
                node = queue.pop() # Pop from the right
                
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            levels.append(level)  # Append the entire level

        return levels

    def recursiveLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        def helper(node, level):
            if not node:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        levels = []
        helper(root, 0)
        return levels


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root)) # [[3], [9, 20], [15, 7]]
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().levelOrder(root)) # [[1], [2, 3], [4, 5]]
    
    root = TreeNode(1)
    print(Solution().levelOrder(root)) # [[1]]
    
    root = None
    print(Solution().levelOrder(root)) # []