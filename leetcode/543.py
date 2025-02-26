class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            diameter = max(diameter, left+right)
            return max(left, right) + 1
        
        diameter = 0
        dfs(root)
        return diameter