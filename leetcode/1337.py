class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        numS = []
        
        #Binary search for num of soldiers in each row O(logn)
        i = 0 
        for row in mat:
            l, r = 0, len(mat[0]) - 1
            count = 0 
            while l <= r:
                mid = (l+r) // 2
                if row[mid] == 1:
                    if mid < len(row) - 1:
                        if row[mid+1] == 1:
                            l = mid + 1
                        else:
                            count = mid + 1
                            break
                    else:
                        count = mid + 1
                        break
                else:
                    r = mid - 1
            numS.append((count, i))
            i += 1
        
        #Sorting list of tuples by num of soldiers O(nlogn)
        numS = sorted(numS, key=lambda x: x[0])
        
        #Getting first k weakest (k)
        out = []
        for i in range(k):
            out.append(numS[i][1])
        return out
        #O(logn) + O(nlogn) + O(k) = O(nlogn)