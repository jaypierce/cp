class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def findLast(letter):
            for i in range(len(garbage)-1, -1, -1):
                if letter in garbage[i]:
                    return i
            return 0
        
        def count(letter):
            time = 0
            for i in range(len(garbage)):
                if letter in garbage[i]:
                    time += garbage[i].count(letter)
            return time
        
        #Prefix sum
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
        travel = [0] + travel
        
        out = 0
        for i in 'MPG':
            out += (count(i) + travel[findLast(i)])
        return out