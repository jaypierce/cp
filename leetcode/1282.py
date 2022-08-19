class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        
        sizes = defaultdict(list)
        
        for i in range(len(g)):
            sizes[g[i]].append(i)
        
        out = []
        
        for i, vals in zip(sizes,sizes.values()):
            tmp = []
            count = i
            for j in vals:
                tmp.append(j)
                count -= 1
                if count == 0:
                    out.append(tmp)
                    tmp = []
                    count = i
            # for idx in range(0, len(vals), i):
            #     out.append(vals[idx:idx+i])
        
        return (out)