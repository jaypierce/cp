class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distdict = defaultdict(list)
        dist = []
        for i in range(len(points)):
            tmp = math.sqrt(points[i][0]**2 + points[i][1]**2)
            distdict[tmp].append((points[i][0], points[i][1]))
            dist.append(tmp)
        
        heapq.heapify(dist)
        
        out = []
            
        while k > 0:
            tmp = heapq.heappop(dist)
            tmp2 = distdict[tmp]
            distdict[tmp] = tmp2[1:]
            out.append(tmp2[0])
            k -= 1
        
        return out