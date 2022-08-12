class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return node
            
            if node.val == val:
                return node
            elif node.val > val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)