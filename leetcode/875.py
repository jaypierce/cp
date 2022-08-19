class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = max(piles)
        minb = n
        l, r = 1, n
        
        while l <= r:
            mid = (l + r)//2
            count = 0
            
            for p in piles:
                count += math.ceil(p/mid)
            
            if count <= h:
                minb = min(minb, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return minb