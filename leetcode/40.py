class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        
        out = []
        c.sort()
        
        def dfs(i, dc, total):
            if total == target:
                if dc not in out:
                    out.append(dc[::])
                return
            if total > target or pos == len(c):
                return
            
            dc.append(c[i])
            dfs(i + 1, dc, total + c[i])
            dc.pop()
            while i+1 < len(c) and c[i] == c[i+1]:
                i += 1 
            dfs(i+1, dc, total)
            
            # prev = -1
            # for i in range(pos, len(c)):
            #     if c[i] == prev: 
            #         continue
            #     dc.append(c[i])
            #     dfs(i+1, dc, total + c[i])
            #     dc.pop()
            #     prev = c[i]
            
            return out
        
        return dfs(0,[],0)