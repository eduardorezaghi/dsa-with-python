class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return 1 + max(get_height(node.left), get_height(node.right))
        
        if not root:
            return True
    
        left_height = get_height(root.left)
        right_height = get_height(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)