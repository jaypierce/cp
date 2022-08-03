class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
####WORKING BINARY SEARCH(but i think its just two pointers)#######
        l, r = 0, int(sqrt(c))
        
        while l <= r:
            target = (l*l) + (r*r)
            if target == c:
                return True
            elif target < c:
                l += 1
            else:
                r -= 1
        return False

##ALMOST WORKING BINARY SEARCH - ONLY WORKING 0 - 9999##
#         def search(i):
#             l, r = 0, i
            
#             while l <= r:
#                 mid = (l+r) // 2
#                 target = mid*mid + i*i
#                 if target == c:
#                     break
#                 elif target < c:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             print(mid, i)
#             return mid, i
        
#         l, r = 0, int(c**0.5)
        
#         while l < r:
#             mid = (l+r) // 2
#             num1, num2 = search(mid)
#             target = num1*num1 + num2*num2
#             print(num1, num2, target)
#             if target == c:
#                 return True
#             elif target < c:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False