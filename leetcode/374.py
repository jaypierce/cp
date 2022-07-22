class Solution:
    def guessNumber(self, n: int) -> int:
            
        l,r = 0, n
        
        while l <= r:
            mid = (l+r)//2
            ans = guess(mid)
            
            if ans == -1:
                r = mid - 1
            elif ans == 1:
                l = mid + 1
            elif ans == 0:
                return mid
        
        