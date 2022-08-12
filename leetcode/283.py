class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 1 
        while r < len(nums) and l < r:
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
            r += 1
        
        #Backwards
#         slow, fast = len(nums) - 1, len(nums) - 2
        
#         while fast > -1 and slow > fast:
#             if nums[slow] == 0 and nums[fast] != 0:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]
#             if nums[slow] != 0:
#                 slow -= 1
#             fast -= 1