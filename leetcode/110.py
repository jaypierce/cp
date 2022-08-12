class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0  
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) > 1:
                balanced = False
            return max(left, right) + 1
        
        dfs(root)
        return balanced