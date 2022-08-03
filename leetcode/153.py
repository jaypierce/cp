class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        out = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                out = min(out, nums[l])
                break
                
            mid = (l+r) // 2
            out = min(out, nums[mid])
            
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return out