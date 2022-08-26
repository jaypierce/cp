class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        rsum = 0
        subset = []
        def dfs(i):
            nonlocal rsum
            if i == len(nums):
                tmp = 0
                for i in subset:
                    tmp ^= i
                rsum += tmp
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            
            return rsum
        
        return dfs(0)