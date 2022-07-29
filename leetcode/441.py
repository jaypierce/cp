class Solution:
    def arrangeCoins(self, n: int) -> int:
        
#####Using Binary search and using summation formula up to n#######
        l, r = 1, n
        
        while l <= r:
            mid = (l+r)//2
            summ = int(mid/2*(2*(1)+(mid-1)*1))
            
            if summ == n:
                return mid
            elif summ > n > summ - mid:
                return mid - 1
            elif summ > n:
                r = mid - 1
            else:
                l = mid + 1
              
    #####Iterative checking every number#####
        # i = 1
        # while True:
        #     if n < i:
        #         return i - 1
        #     n -= i
        #     i += 1   