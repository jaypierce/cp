class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        global mn, prev
        mn = prev = float('inf')
        
        def dfs(node):
            global mn, prev
            if not node:
                return node
            
            dfs(node.left)
            mn = min(mn, abs(node.val - prev))
            prev = node.val
            dfs(node.right)
            
            return mn
            
          
        return dfs(root)