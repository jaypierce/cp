class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        valid = True
        def dfs(node, lb, rb):
            nonlocal valid
            if not node:
                return
            
            if node.left:
                if lb < node.left.val < node.val:
                    dfs(node.left, lb, node.val)
                else:
                    valid = False
            if node.right:
                if node.val < node.right.val < rb:
                    dfs(node.right, node.val, rb)
                else:
                    valid = False
            return
            
        dfs(root, float('-inf'), float('inf'))
        return valid