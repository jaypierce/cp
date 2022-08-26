class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        out = []
        subset = []
        
        def dfs(i):
            if i == len(nums):
                if subset not in out:
                    out.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            
            return out
             
        return dfs(0)