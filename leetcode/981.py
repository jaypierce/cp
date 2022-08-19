class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = []
        self.maps[key].append([value, timestamp])
        return
    
    def get(self, key: str, timestamp: int) -> str:
        out = ''
        values = self.maps[key]
        
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l+r)//2
            time = values[mid][1]
            
            if time <= timestamp:
                out = values[mid][0]
                l = mid + 1
            elif time > timestamp:
                r = mid - 1
            
        return out