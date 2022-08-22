class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = [i for i in range(1,1001)]
        self.canAdd = defaultdict(bool)

    def popSmallest(self) -> int:
        if self.minHeap:
            tmp = heapq.heappop(self.minHeap)
            self.canAdd[tmp] = True
            return tmp

    def addBack(self, num: int) -> None:
        if self.canAdd[num]:
            heapq.heappush(self.minHeap, num)
            self.canAdd[num] = False