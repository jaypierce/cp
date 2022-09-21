class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        islands = defaultdict(list)
        visited = set()
        def dfs(r, c, idx):
            if r < 0 or c < 0 or r >= len(grid2) or c >= len(grid2[0]) \
            or grid2[r][c] == 0 or (r,c) in visited:
                return
            
            visited.add((r,c))
            islands[idx].append((r,c))
            
            for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(r+i, c+j, idx)
            
        idx = 0 
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c,idx)
                    idx+=1
                    
        out = 0
        for island in islands:
            same = True
            for i,j in islands[island]:
                if grid1[i][j] == 0:
                    same = False
            if same:
                out += 1
        return out