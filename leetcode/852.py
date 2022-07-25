class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return -1
        
        def search(l, r, arr, mx):
            mid = (l+r)//2
            if arr[mid] > mx[0]:
                    mx = (max(arr[mid], mx[0]), mid)
            if l <= r:
                mx = search(mid + 1, r, arr, mx)
                mx = search(l, mid - 1, arr, mx)
                
            return mx
        
        mx = (float('-inf'), float('inf'))
        mx = search(0, len(arr)-1, arr, mx)
        return mx[1]