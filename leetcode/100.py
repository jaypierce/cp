class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        sameTree = True
        def dfs(one, two):
            nonlocal sameTree
            if not one and not two:
                return one, two
            if not one:
                sameTree = False
                return one
            if not two:
                sameTree = False
                return two
            
            if one.val != two.val:
                sameTree = False
            dfs(one.left, two.left)
            dfs(one.right, two.right)
            
            return
        
        dfs(p, q)
        return sameTree