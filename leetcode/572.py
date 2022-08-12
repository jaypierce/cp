class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(one, two):
            if one and two:
                return one.val == two.val and sameTree(one.left, two.left) and sameTree(one.right, two.right)
            return one is two
        
        isSub = False
        def dfs(node):
            nonlocal isSub
            if not node:
                return node
            
            if node.val == subRoot.val and not isSub:
                isSub = sameTree(node, subRoot)
            
            dfs(node.left)
            dfs(node.right)
            
            return
        
        dfs(root)
        return isSub