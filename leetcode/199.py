class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                
        def bfs(node):
            if not node:
                return node
            
            out = []
            queue = deque([])
            queue.append(node)
            
            while queue:
                out.append(queue[-1].val)
                for i in range(len(queue)):
                    n = queue.popleft() 
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
            
            return out
                
        
        return bfs(root)