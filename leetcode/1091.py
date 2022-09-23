class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        queue.append([0,0])
        visited = set()
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                #If off grid
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                #If seen before or is a 1 
                if (r,c) in visited or grid[r][c] == 1:
                    continue
                #If reached goal  
                if (r, c) == (len(grid)-1, len(grid[0])-1):
                    return dist
                
                visited.add((r,c))
                for i, j in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                    queue.append([r+i, c+j])
            dist += 1
        return -1