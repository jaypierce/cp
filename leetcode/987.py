class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #Verticies:val
        verticies = defaultdict(list)
        
        def dfs(root, vert):
            if not root:
                return root
        
            verticies[vert].append(root.val)
            dfs(root.left, (vert[0]+1, vert[1]-1))
            dfs(root.right, (vert[0]+1, vert[1]+1))
            
        dfs(root, (0,0))
        
        #Sorting values at same x
        for i in verticies:
            verticies[i].sort()
        
        #Sorting values at same y
        n = defaultdict(list)
        for i, j in sorted(verticies.items(), key= lambda x:(x[0], x[1])):
            n[i[1]] += j
        
        #Sorting by x
        out = []
        nn = sorted(n)
        for i in nn:
            out.append(n[i])
            
        return out