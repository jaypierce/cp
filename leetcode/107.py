class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = []
        
        def bfs(node):
            if not node:
                return node
            queue = deque([])
            queue.append(node)
            
            while queue:
                level = []
                
                for _ in range(len(queue)):
                    n = queue.popleft()
                    level.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                out.append(level)
            return out[::-1]
        
        return bfs(root)