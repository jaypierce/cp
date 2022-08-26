class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        leafs = defaultdict(list)
        deepest = 0
        
        def dfs(root, level):
            nonlocal deepest
            if not root:
                return root
            
            deepest = max(deepest, level)
            
            if not root.left and not root.right:
                leafs[level].append(root.val)
                return 
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        return sum(leafs[deepest])