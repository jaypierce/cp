class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [i for i, j in points]
        points.sort()
        
        for i in range(len(points) - 2):
            maxW = max(maxW, points[i+1] - points[i])
        
        return maxW