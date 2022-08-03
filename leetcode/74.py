class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #########USING TWO BINARY SEARCH#######
        m, n = len(matrix), len(matrix[0])
        
        #Search col
        l, r = 0, len(matrix) -1
        r1 = -1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                r1 = mid
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        if r1 == -1:
            return False 
        
        #Search row
        l2, r2 = 0, len(matrix[0]) -1
        while l2 <= r2:
            mid2 = (l2+r2) // 2
            
            if matrix[r1][mid2] == target:
                return True
            elif matrix[r1][mid2] < target:
                l2 = mid2 + 1
            else:
                r2 = mid2 - 1
        return False
        
        
        ######USING ONE BINARY SEARCH#####
#         for row in matrix:
#             l, r = 0, len(row) - 1
#             if target > row[r]:
#                 continue
#             while l <= r:
#                 mid = (l+r) // 2
#                 if row[mid] == target:
#                     return True
#                 elif row[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return False