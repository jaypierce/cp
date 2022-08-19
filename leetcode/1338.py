class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        
        new = []
        for i in count:
            new.append((i, count[i]))
        new.sort(key = lambda x: x[1], reverse = True)
    
        out = 0
        n = len(arr)
        for i in new:
            out += 1
            n = n - i[1]
            if n <= len(arr) // 2:
                return out