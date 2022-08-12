class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxR = [0]*len(height)
        maxL = [0]*len(height)
        
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        for _ in range(len(height)):
            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]
            maxR[r] = rmax
            maxL[l] = lmax
            l +=1
            r -=1

        out = 0
        for i in range(len(maxL)):
            water = min(maxL[i], maxR[i]) - height[i]
            if water > 0:
                out += water
        return out