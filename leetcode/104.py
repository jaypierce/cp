class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #BFS
        queue = deque([])
        def bfs(node):
            
            level = 0
            if not node:
                return level
            queue.append(node)
            
            while queue:
                for _ in range(len(queue)):
                    n = queue.popleft()
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                level += 1
            return level 
        
        return bfs(root)

        # #DFS
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1