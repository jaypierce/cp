class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        rsum = 0
        def dfs(root):
            nonlocal rsum
            if not root:
                return
            
            dfs(root.right)
            rsum += root.val
            root.val = rsum
            dfs(root.left)
            
            return root
        
        return dfs(root)