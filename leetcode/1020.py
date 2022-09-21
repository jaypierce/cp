class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        visited = set()
        def dfs(r, c, cur):
            if (r <= 0 or c <= 0 or r >= len(grid)-1 or c >= len(grid[0])-1) and grid[r][c] == 1:
                return (False, 0)
            if grid[r][c] == 0 or (r,c) in visited:
                return (True, 0)
            
            visited.add((r,c))
            dirs = []
            cur = 1
            
            for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                tmp = dfs(r+i, c+j, cur + 1)
                dirs.append(tmp[0])
                cur += tmp[1]
            
            valid = dirs[0]
            for d in dirs:
                valid = valid and d
                
            if valid:
                return (valid,cur)
            return (valid, 0)
        
        out = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    out += dfs(r, c, 0)[1]
        
        return out