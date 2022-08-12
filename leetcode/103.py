class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = []
        queue = deque([])
        i = 0
        
        def bfs(node):
            if not node:
                return node
        
            queue.append(node)
            even = False
            
            while queue:
                l = len(queue)
                lis = []
                
                for _ in range(l):
                    n = queue.popleft()
                    lis.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                        
                if not even:
                    out.append(lis)
                else:
                    out.append(lis[::-1])
                even = not even
            return out
        
        return bfs(root)