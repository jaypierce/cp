class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        ##TWO POINTERS##
        p1 = p2 = 0
        maxDist = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                maxDist = max(maxDist, (p2 - p1))
                p2 += 1
            else:
                p1 += 1
        return maxDist
            
        
        ##BINARY SEARCH##
        # maxDist = 0
        # for i in range(len(nums1)):
        #     l, r = i, len(nums2) - 1
        #     while l <= r:
        #         mid = (l+r) // 2
        #         if nums2[mid] < nums1[i]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     maxDist = max(maxDist, (r-i))
        # return maxDist