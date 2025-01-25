class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = []
        
        def bfs(node: TreeNode | None):
            if not node:
                return
            
            if len(self.nodes) % 2 == 1:
                self.nodes[-1].reverse()
            else:
                self.nodes.append([])
            
            bfs(node.left)
            bfs(node.right)

        bfs(root)

        return self.nodes