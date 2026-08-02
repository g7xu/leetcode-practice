# binary search with hashmap

class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key]:
            return ""

        l = self.hashmap[key]

        if timestamp >= l[-1][0]:
            return l[-1][1]

        if timestamp < l[0][0]:
            return ""

        # binary search
        s = 0
        e = len(l) - 1

        while s < e - 1:
            m = (s + e) // 2
            if timestamp == l[m][0]:
                return l[m][1]

            if timestamp > l[m][0]:
                s = m
            else:
                e = m - 1

        if l[e][0] > timestamp:
            return l[s][1]
        
        return l[e][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)