class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = nums[0]
        maxN = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > cur and cur < 0:
                cur = nums[i]
            else:
                cur += nums[i]
            maxN = max(maxN, cur)
        
        return maxN