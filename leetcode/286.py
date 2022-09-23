class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        queue = deque()
        visited = set()
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append([r,c])
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]):
                    continue
                if (r,c) in visited or rooms[r][c] == -1:
                    continue
                
                visited.add((r,c))
                rooms[r][c] = dist
                for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                    queue.append([r+i,c+j])
            dist += 1