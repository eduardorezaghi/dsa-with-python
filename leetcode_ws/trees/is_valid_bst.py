# Leetcode 98. Validate Binary Search Tree
# link: https://leetcode.com/problems/validate-binary-search-tree/

from aux import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            # Check bounds for right node and left node,
            # strictly less than node.val for right node and
            # strictly greater than node.val for left node
            return dfs(node.left,  lower,    node.val) and\
                   dfs(node.right, node.val, upper)
    
        return dfs(root, float('-inf'), float('inf'))