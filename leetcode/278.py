class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        lastBad = None
        while l <= r:
            mid = (l+r) //2
            bad = isBadVersion(mid)
            if bad:
                lastBad = mid
                r = mid - 1
            else:
                l = mid + 1
        return lastBad