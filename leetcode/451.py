class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = defaultdict(int)
        for i in s:
            count[i] += 1
          
        lis = []
        for i in count:
            lis.append((-count[i], i))
        
        heapq.heapify(lis)
        
        out = []
        while lis:
            num, char = heapq.heappop(lis)
            out += [char] * -num
        
        return ''.join(out)