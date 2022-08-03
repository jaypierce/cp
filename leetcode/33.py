class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Find max in arr
        #Count amount rotated (dist from end)
        #If num is less that last value in arr. nums[-1]
        #   search from index of max till end of list for target
        #else
        #   search from beginning to max index for target
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1                                   
        return -1
                    