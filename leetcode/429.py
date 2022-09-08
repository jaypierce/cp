class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return
        
        queue = deque()
        queue.append(root)
        out = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                n = queue.popleft()
                for i in n.children:
                    queue.append(i)
                level.append(n.val)
            out.append(level)
        
        return out