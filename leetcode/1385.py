class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2.sort()
        out = 0
        
        for i in arr1:
            l, r = 0, len(arr2) - 1
            
            while l <= r:
                mid = (l+r)//2
                
                if abs(i-arr2[mid]) <= d:
                    out -= 1
                    break
                elif arr2[mid] > i:
                    r = mid - 1
                else:
                    l = mid + 1
            out += 1
        return out

    ######Iterative Solution######
#         summ = out = 0
#         for i in arr1:
#             summ = 0
#             for j in arr2:
#                 if abs(i-j) > d:
#                     summ += 1
#                 else:
#                     break
#             if summ == len(arr2):
#                 out += 1
            
#         return out   