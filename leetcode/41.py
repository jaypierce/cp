class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        tmp = [-i for i in nums if i > 0]
        tmp2 = [i for i in nums if i > 0]
        heapq.heapify(tmp)
        heapq.heapify(tmp2)
        
        if tmp:
            last = -heapq.heappop(tmp)
        else:
            return 1
        
        count = Counter(set(tmp2))
        
        for i in range(1, last + 2):
            if i not in count:
                return i