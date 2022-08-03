class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for row in grid:
            l, r = 0, len(row) - 1
            
            while l <= r:
                mid = (l+r) // 2
                if row[mid] < 0:
                    if mid > 0 and row[mid-1] < 0:
                        r = mid - 1
                    else:
                        count += (len(row) - mid)
                        break
                else:
                    l = mid + 1
                    
        return count