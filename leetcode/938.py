class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        summ = 0
        
        def dfs(node):
            nonlocal summ
            if not node:
                return node
            
            dfs(node.left)
            if low <= node.val <= high:
                summ += node.val
            dfs(node.right)
            
            return summ
        
        return dfs(root)