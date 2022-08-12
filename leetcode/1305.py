class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs(root, lis):
            if not root:
                return lis
            
            dfs(root.left, lis)
            lis.append(root.val)
            dfs(root.right, lis)
            
            return lis
            
        l1 = dfs(root1, []) 
        l2 = dfs(root2, []) 
        out = []
        i = j = 0
        
        
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                out.append(l1[i])
                i += 1
            else:
                out.append(l2[j])
                j += 1
        
        out = out + l1[i:] + l2[j:]
        
        return out