from collections import deque


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Percorrer a árvore até encontrar o leaf node.
        # Armazenar valores em um set, depois converter em lista.
        # Indexar k com zero e obter valor.
        if not root:
            return None

        nums = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                nums.add(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return list(sorted(nums))[k - 1]
    
    # Using Inorder traversal (smallest to largest) L -> N -> R
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.elements = []

        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            self.elements.append(node.val)
            inorder(node.right)

        inorder(root)

        return self.elements[k - 1]