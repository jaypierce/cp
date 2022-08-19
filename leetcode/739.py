class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        out = [0]*len(temperatures)
        stack = [(float('inf'), 0)]
        
        for i in range(0, len(temperatures)):
            while stack[-1][0] < temperatures[i] and len(stack) > 0:
                temp, idx = stack.pop()
                temperatures[idx] = 0
                out[idx] = i - idx
            stack.append((temperatures[i], i))
            
        return out