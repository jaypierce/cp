class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return node
            
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
                    
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left)
            else:
                return node
            
        
        return dfs(root)