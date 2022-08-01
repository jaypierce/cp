class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         complements = {}
        
#         for i in range(len(numbers)):
#             if target - numbers[i] in complements:
#                 return complements[target - numbers[i]]+1, i+1
#             else:
#                 complements[numbers[i]] = i
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return l+1, r+1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        