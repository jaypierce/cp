class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums)
        
        while l <= r:
            x = (l+r) // 2
            
            count = 0
            for i in nums:
                if i >= x:
                    count += 1
            if count == x:
                return x
            elif count > x:
                l = x + 1
            else:
                r = x - 1
        return -1