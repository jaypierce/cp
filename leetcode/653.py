class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def bfs(node):
            
            queue = deque([])
            queue.append(node)
            seen = {}
            
            while queue:
                for _ in range(len(queue)):
                    n = queue.popleft()
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                    if k - n.val in seen:
                        return True
                    seen[n.val] = 1
            return False
        
        return bfs(root)